"""
=============================================================================
UKM ASC UNIVERSITAS NEGERI MALANG - MASTER BUILD TOOL (MODULAR EDITION)
=============================================================================
Fungsi:
1. python build.py          -> Mengompilasi seluruh file di folder 'sections/'
                               menjadi file statis utuh 'index.html' untuk GitHub Pages
                               dan 'index.standalone.html' (embedded assets).
2. python build.py --check  -> Memeriksa kelengkapan file komponen dan integritas HTML.
3. python build.py --serve  -> Menjalankan server lokal di port 8000.
=============================================================================
"""

import os
import sys
import base64
import http.server
import socketserver
import webbrowser
from pathlib import Path

# Ensure UTF-8 output on Windows
if sys.stdout.encoding and sys.stdout.encoding.lower() != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    except Exception:
        pass

BASE_DIR = Path(__file__).resolve().parent
SECTIONS_DIR = BASE_DIR / "sections"

SECTION_FILES = [
    "00_header.html",
    "01_profil.html",
    "02_scroll_asc.html",
    "02_visi_misi.html",
    "03_pembinaan.html",
    "04_struktur_organisasi.html",
    "05_prestasi.html",
    "06_kabinet.html",
    "07_faq_kontak.html",
    "08_link_medsos.html",
    "09_footer.html"
]

def check_integrity():
    print("🔍 Menjalankan pemeriksaan integritas proyek...")
    errors = 0
    warnings = 0

    if not SECTIONS_DIR.exists():
        print("❌ Error: Folder 'sections/' tidak ditemukan!")
        return 1

    for s in SECTION_FILES:
        sp = SECTIONS_DIR / s
        if not sp.exists():
            print(f"❌ Error: Komponen {s} tidak ditemukan di sections/!")
            errors += 1
        else:
            print(f"  ✅ {s} ({sp.stat().st_size:,} bytes)")

    cutout = BASE_DIR / "assets" / "hero-asc-cutout.webp"
    if not cutout.exists():
        cutout = BASE_DIR / "hero-asc-cutout.webp"
    if not cutout.exists():
        print("⚠️ Warning: hero-asc-cutout.webp tidak ditemukan.")
        warnings += 1
    else:
        print(f"  ✅ hero-asc-cutout.webp ({cutout.stat().st_size:,} bytes)")

    print(f"\nHasil: {errors} error, {warnings} warning.")
    return errors


def build_pages():
    print("🔨 Mengompilasi komponen modular menjadi index.html untuk GitHub Pages...")
    parts = []

    for s in SECTION_FILES:
        sp = SECTIONS_DIR / s
        if not sp.exists():
            print(f"⚠️ Peringatan: {s} tidak ditemukan, dilewati.")
            continue
        print(f"  + Menyertakan {s} ({sp.stat().st_size:,} bytes)")
        content = sp.read_text(encoding="utf-8")
        parts.append(f"\n<!-- START COMPONENT: {s} -->\n{content}\n<!-- END COMPONENT: {s} -->\n")

    body_content = "\n".join(parts)

    master_html = f"""<!DOCTYPE html>
<html lang="id">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=5.0" />
  <title>UKM Al-Qur'an Study Club (ASC) - Universitas Negeri Malang</title>
  
  <!-- SEO & Meta Tags -->
  <meta name="description" content="Website Resmi UKM Al-Qur'an Study Club (ASC) Universitas Negeri Malang. Wadah pembinaan Al-Qur'an, tilawah, tahfidz, kaligrafi, syiar, dan prestasi mahasiswa UM." />
  <meta name="keywords" content="UKM ASC, ASC UM, Al-Qur'an Study Club, Universitas Negeri Malang, MTQMN, Mahasiswa UM, Generasi Qurani" />
  <meta name="author" content="UKM ASC Universitas Negeri Malang" />
  <meta name="theme-color" content="#0d5c3f" />

  <!-- Open Graph / Facebook -->
  <meta property="og:type" content="website" />
  <meta property="og:title" content="UKM Al-Qur'an Study Club (ASC) - Universitas Negeri Malang" />
  <meta property="og:description" content="Membina Generasi Qur'ani yang Berkarakter, Berprestasi, dan Berkontribusi Nyata." />
  <meta property="og:image" content="https://ormawa.um.ac.id/wp-content/uploads/2020/09/cropped-logo-um-32x32.png" />

  <!-- Favicon -->
  <link rel="icon" href="https://ormawa.um.ac.id/wp-content/uploads/2020/09/cropped-logo-um-32x32.png" type="image/png" />

  <!-- Preconnect Google Fonts -->
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Geist+Mono:wght@500;700;800&family=Geist:wght@800;900&family=Poppins:wght@300;400;500;600;700;800&display=swap" rel="stylesheet" />

  <style>
    /* =========================================================================
       GLOBAL DESIGN SYSTEM & RESET (WHITE-FIRST EDITORIAL)
       ========================================================================= */
    :root {{
      --bg: #ffffff;
      --surface: #f7f7f5;
      --ink: #09131c;
      --ink-mid: #1e2d3b;
      --ink-muted: #5a6876;
      --emerald-500: #10b981;
      --emerald-600: #0d5c3f;
      --emerald-700: #0a4731;
      --emerald-900: #063726;
      --pdh-brown: #5c3a28;
      --gold: #b8860b;
      --border: rgba(9, 19, 28, 0.08);
      --pad-x: clamp(20px, 4vw, 48px);
      --font-body: 'Poppins', -apple-system, BlinkMacSystemFont, sans-serif;
      --font-heading: 'Geist', sans-serif;
      --font-mono: 'Geist Mono', monospace;
    }}

    *, *::before, *::after {{
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }}

    html {{
      scroll-behavior: smooth;
      -webkit-text-size-adjust: 100%;
      background-color: var(--bg);
      color: var(--ink);
    }}

    body {{
      min-height: 100vh;
      background-color: var(--bg);
      font-family: var(--font-body);
      color: var(--ink);
      overflow-x: hidden;
      line-height: 1.5;
      -webkit-font-smoothing: antialiased;
      -moz-osx-font-smoothing: grayscale;
    }}

    img {{
      display: block;
      max-width: 100%;
      height: auto;
    }}

    a {{
      color: inherit;
    }}

    /* Global SVG Safety Guard */
    svg:not([width]):not([class]) {{
      max-width: 100%;
      height: auto;
    }}
  </style>
</head>
<body>

  {body_content}

</body>
</html>
"""
    out_standalone = BASE_DIR / "index.standalone.html"
    out_standalone.write_text(master_html, encoding="utf-8")
    print(f"✅ Selesai! Versi standalone tersimpan di {out_standalone.name} ({out_standalone.stat().st_size:,} bytes)")


def serve_local(start_port=8000):
    os.chdir(BASE_DIR)
    
    # Gunakan ThreadingHTTPServer multi-thread agar request paralel (fetch) tidak saling memblokir
    port = start_port
    httpd = None
    while port < start_port + 20:
        try:
            httpd = http.server.ThreadingHTTPServer(("", port), http.server.SimpleHTTPRequestHandler)
            break
        except OSError:
            port += 1
            
    if not httpd:
        print(f"❌ Gagal mengaktifkan server: Port {start_port}-{start_port+20} sedang terpakai.")
        return

    with httpd:
        url_sections = f"http://localhost:{port}/sections/index.html"
        url_standalone = f"http://localhost:{port}/index.standalone.html"
        print("\n" + "=" * 65)
        print(f"  🚀 SERVER LOKAL UKM ASC UM AKTIF!")
        print(f"  🌐 Modular View  : {url_sections}")
        print(f"  📄 Standalone View : {url_standalone}")
        print("=" * 65)
        print("  💡 Halaman website otomatis terbuka di browser.")
        print("  🛑 Tekan Ctrl + C di terminal ini untuk menghentikan server.\n")
        try:
            webbrowser.open(url_sections)
        except Exception:
            pass
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n🛑 Server dihentikan dengan aman.")


if __name__ == "__main__":
    if "--check" in sys.argv or "-c" in sys.argv:
        err = check_integrity()
        sys.exit(err)
    elif "--build-only" in sys.argv or "-b" in sys.argv:
        build_pages()
    elif "--serve" in sys.argv or "-s" in sys.argv:
        build_pages()
        serve_local()
    else:
        # Default: kompilasi lalu otomatis jalankan server lokal
        build_pages()
        print("\n💡 Tips: Untuk hanya kompilasi tanpa server, gunakan: python build.py --build-only")
        serve_local()
