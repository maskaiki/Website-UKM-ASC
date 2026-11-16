"""
UKM ASC UM - Build & Development Tool
====================================
Fitur:
1. python build.py          -> Menghasilkan index.standalone.html (dengan foto hero embedded Base64 WebP untuk Elementor Canvas)
2. python build.py --serve  -> Menjalankan server HTTP lokal di port 8000 dan membuka browser otomatis
3. python build.py --check  -> Validasi kelengkapan berkas, ukuran aset, dan integritas HTML
"""

import os
import sys
import base64
import http.server
import socketserver
import webbrowser
from pathlib import Path

# Ensure UTF-8 output on Windows
if sys.stdout.encoding and sys.stdout.encoding.lower() != "utf-8":
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

BASE_DIR = Path(__file__).resolve().parent
INDEX_HTML = BASE_DIR / "index.html"
STANDALONE_HTML = BASE_DIR / "index.standalone.html"
CUTOUT_WEBP = BASE_DIR / "assets" / "hero-asc-cutout.webp"
CUTOUT_PNG = BASE_DIR / "assets" / "hero-asc-cutout.png"

GITHUB_RAW_WEBP = "https://maskaiki.github.io/Website-UKM-ASC/assets/hero-asc-cutout.webp"
GITHUB_RAW_PNG = "https://maskaiki.github.io/Website-UKM-ASC/assets/hero-asc-cutout.png"


def get_cutout_b64():
    """Mengambil base64 dari WebP jika ada, fallback ke PNG jika diperlukan."""
    if CUTOUT_WEBP.exists():
        data = CUTOUT_WEBP.read_bytes()
        mime = "image/webp"
        print(f"  + Memuat aset WebP: {CUTOUT_WEBP.name} ({len(data):,} bytes)")
        b64 = base64.b64encode(data).decode("ascii")
        return f"data:{mime};base64,{b64}"
    elif CUTOUT_PNG.exists():
        data = CUTOUT_PNG.read_bytes()
        mime = "image/png"
        print(f"  + Memuat aset PNG: {CUTOUT_PNG.name} ({len(data):,} bytes)")
        b64 = base64.b64encode(data).decode("ascii")
        return f"data:{mime};base64,{b64}"
    else:
        print("  ⚠️ Aset cutout lokal tidak ditemukan di folder assets/")
        return None


def build_standalone():
    print("🔨 Mengompilasi index.standalone.html (White-First Editorial Edition)...")
    if not INDEX_HTML.exists():
        print(f"❌ Error: {INDEX_HTML.name} tidak ditemukan!")
        sys.exit(1)

    html = INDEX_HTML.read_text(encoding="utf-8")
    b64_uri = get_cutout_b64()

    if b64_uri:
        # Ganti tag picture di index.html dengan data URI mandiri
        # Gambar langsung ter-embed tanpa perlu hosting eksternal
        old_picture_pattern = (
            '<source srcset="assets/hero-asc-cutout.webp" type="image/webp" />'
        )
        if old_picture_pattern in html:
            html = html.replace(
                old_picture_pattern,
                f'<source srcset="{b64_uri}" type="image/webp" />'
            )
            html = html.replace(
                'src="assets/hero-asc-cutout.png"',
                f'src="{b64_uri}"'
            )
            print("  + Meng-embed foto hero cutout sebagai Base64 Data URI (100% standalone untuk WordPress Elementor)")
        else:
            # Fallback jika pattern berbeda
            html = html.replace("assets/hero-asc-cutout.webp", b64_uri)
            html = html.replace("assets/hero-asc-cutout.png", b64_uri)
    else:
        # Fallback ke CDN GitHub Pages
        print("  ℹ️ Menggunakan fallback URL GitHub Pages untuk aset hero cutout")
        html = html.replace("assets/hero-asc-cutout.webp", GITHUB_RAW_WEBP)
        html = html.replace("assets/hero-asc-cutout.png", GITHUB_RAW_PNG)

    # Tambahkan komentar panduan Elementor di bagian atas file standalone
    banner = f"""<!--
================================================================================
 UKM AL-QUR'AN STUDY CLUB (ASC) - UNIVERSITAS NEGERI MALANG
 DESAIN: WHITE-FIRST EDITORIAL (GOBO KINETIC x EFFICA CONVERSION)
 TIPE: STANDALONE SINGLE-FILE HTML (SIAP COPAS KE ELEMENTOR CANVAS)
================================================================================
 CARA PEMASANGAN DI WORDPRESS ELEMENTOR (ormawa.um.ac.id):
 1. Login ke Dashboard WordPress ormawa.um.ac.id/wp-admin
 2. Buat / Edit Halaman (Pages -> Edit with Elementor)
 3. Pada Settings (ikon gear kiri bawah) -> Ubah 'Page Layout' menjadi 'Elementor Canvas'
 4. Tarik widget 'HTML' (Custom HTML) ke dalam canvas halaman
 5. Salin (copy) SELURUH isi file index.standalone.html ini
 6. Tempel (paste) ke dalam widget HTML tersebut
 7. Klik 'Publish' / 'Update' -> Website UKM ASC langsung live!
================================================================================
-->
"""
    standalone_output = banner + html

    STANDALONE_HTML.write_text(standalone_output, encoding="utf-8")
    print(f"✅ Selesai! File tersimpan di {STANDALONE_HTML.name} ({STANDALONE_HTML.stat().st_size:,} bytes)")
    print(f"   Lokasi: {STANDALONE_HTML.resolve()}")


def check_integrity():
    print("🔍 Menjalankan pemeriksaan integritas proyek...")
    errors = 0
    warnings = 0

    if not INDEX_HTML.exists():
        print(f"❌ Error: {INDEX_HTML.name} tidak ada!")
        errors += 1
    else:
        print(f"✅ {INDEX_HTML.name} ada ({INDEX_HTML.stat().st_size:,} bytes)")

    if not CUTOUT_WEBP.exists():
        print(f"⚠️ Warning: {CUTOUT_WEBP.name} tidak ada!")
        warnings += 1
    else:
        print(f"✅ {CUTOUT_WEBP.name} ada ({CUTOUT_WEBP.stat().st_size:,} bytes)")

    if not CUTOUT_PNG.exists():
        print(f"⚠️ Warning: {CUTOUT_PNG.name} tidak ada!")
        warnings += 1
    else:
        print(f"✅ {CUTOUT_PNG.name} ada ({CUTOUT_PNG.stat().st_size:,} bytes)")

    if not STANDALONE_HTML.exists():
        print(f"⚠️ Warning: {STANDALONE_HTML.name} belum di-compile! Jalankan 'python build.py'")
        warnings += 1
    else:
        print(f"✅ {STANDALONE_HTML.name} ada ({STANDALONE_HTML.stat().st_size:,} bytes)")

    print(f"\nHasil: {errors} error, {warnings} warning.")


def serve_local(port=8000):
    os.chdir(BASE_DIR)
    socketserver.TCPServer.allow_reuse_address = True
    handler = http.server.SimpleHTTPRequestHandler
    with socketserver.TCPServer(("", port), handler) as httpd:
        url = f"http://localhost:{port}/index.html"
        print(f"\n🚀 Server lokal aktif di {url}")
        print(f"📂 Direktori root: {BASE_DIR}")
        print("🌐 Membuka browser default...")
        print("Tekan Ctrl+C untuk menghentikan server.\n")
        try:
            webbrowser.open(url)
        except Exception:
            pass
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n🛑 Server dihentikan.")


if __name__ == "__main__":
    if "--serve" in sys.argv or "-s" in sys.argv:
        serve_local()
    elif "--check" in sys.argv or "-c" in sys.argv:
        check_integrity()
    else:
        build_standalone()
