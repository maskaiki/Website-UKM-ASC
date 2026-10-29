"""
UKM ASC UM - Build & Development Tool
Fungsi:
1. python build.py          -> Menghasilkan file standalone tunggal (index.standalone.html) dari semua partials
2. python build.py --serve  -> Menjalankan local server dan otomatis membuka browser
"""

import os
import sys
import http.server
import socketserver
import webbrowser
from pathlib import Path

# Ensure UTF-8 output on Windows
if sys.stdout.encoding.lower() != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


BASE_DIR = Path(__file__).resolve().parent

COMPONENTS = [
    "00_header.html",
    "01_profil.html",
    "02_visi_misi.html",
    "03_sejarah.html",
    "03_struktur_organisasi.html",
    "04_pengumuman_agenda.html",
    "05_galeri.html",
    "06_prestasi.html",
    "07_link_medsos.html"
]

def build_standalone():
    print("🔨 Mengompilasi komponen menjadi index.standalone.html...")
    parts = []
    for comp in COMPONENTS:
        fpath = BASE_DIR / comp
        if not fpath.exists():
            print(f"⚠️ Peringatan: File {comp} tidak ditemukan!")
            continue
        print(f"  + Menyertakan {comp} ({fpath.stat().st_size:,} bytes)")
        content = fpath.read_text(encoding="utf-8")
        parts.append(f"\n<!-- START COMPONENT: {comp} -->\n{content}\n<!-- END COMPONENT: {comp} -->\n")

    combined_body = "\n".join(parts)

    standalone_html = f"""<!DOCTYPE html>
<html lang="id">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=5.0">
  <title>UKM Al-Qur'an Study Club (ASC) - Universitas Negeri Malang</title>
  <meta name="description" content="Website Resmi UKM Al-Qur'an Study Club (ASC) Universitas Negeri Malang. Wadah pembinaan Al-Qur'an, tilawah, tahfidh, kaligrafi, syiar, dan prestasi mahasiswa UM.">
  <meta name="keywords" content="UKM ASC, ASC UM, Al-Qur'an Study Club, Universitas Negeri Malang, UKM UM, MTQMN">
  <meta name="theme-color" content="#0284c7">

  <!-- Open Graph / Facebook -->
  <meta property="og:type" content="website">
  <meta property="og:title" content="UKM Al-Qur'an Study Club (ASC) - UM">
  <meta property="og:description" content="Membina Generasi Qur'ani Berprestasi di Universitas Negeri Malang.">
  <meta property="og:image" content="https://ormawa.um.ac.id/wp-content/uploads/2020/09/cropped-logo-um-32x32.png">

  <!-- Favicon -->
  <link rel="icon" href="https://ormawa.um.ac.id/wp-content/uploads/2020/09/cropped-logo-um-32x32.png" type="image/png">

  <!-- Preconnect Google Fonts -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=Space+Grotesk:wght@500;600;700;800&family=Amiri:wght@400;700&display=swap" rel="stylesheet">

  <style>
    html {{
      scroll-behavior: smooth;
      -webkit-text-size-adjust: 100%;
    }}
    body {{
      margin: 0;
      padding: 0;
      background-color: #f8fafc;
      font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif;
      color: #0f172a;
      overflow-x: hidden;
    }}
  </style>
</head>
<body>

  {combined_body}

</body>
</html>
"""
    out_file = BASE_DIR / "index.standalone.html"
    out_file.write_text(standalone_html, encoding="utf-8")
    print(f"✅ Selesai! File tersimpan di {out_file.name} ({out_file.stat().st_size:,} bytes)")


def serve_local(port=8000):
    os.chdir(BASE_DIR)
    handler = http.server.SimpleHTTPRequestHandler
    with socketserver.TCPServer(("", port), handler) as httpd:
        url = f"http://localhost:{port}/index.html"
        print(f"\n🚀 Server lokal aktif di {url}")
        print("Tekan Ctrl+C untuk menghentikan server.")
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
    else:
        build_standalone()
