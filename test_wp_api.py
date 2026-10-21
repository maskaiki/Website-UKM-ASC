import requests
import json

# Konfigurasi Kredensial dan Endpoint
WP_URL = "https://ormawa.um.ac.id/wp-json/wp/v2/pages"
USERNAME = "ASC" # Username dari profil WordPress kamu
APP_PASSWORD = "VR20juhMyc5pq70LyE3ZyVCs"

# Contoh output dari Agent AI (HTML + Tailwind)
ai_generated_html = """
<div class="p-8 bg-blue-500 text-white rounded-lg shadow-lg text-center">
    <h1 class="text-3xl font-bold">Halo dari Antigravity!</h1>
    <p class="mt-4 text-lg">Halaman ini di-generate otomatis via Python & MCP.</p>
</div>
"""

# Membungkus HTML dengan shortcode Code Module dari Divi Builder
divi_content = f"""
[et_pb_section fb_built="1" theme_builder_area="post_content"]
    [et_pb_row theme_builder_area="post_content"]
        [et_pb_column type="4_4" theme_builder_area="post_content"]
            [et_pb_code theme_builder_area="post_content"]
                {ai_generated_html}
            [/et_pb_code]
        [/et_pb_column]
    [/et_pb_row]
[/et_pb_section]
"""

# Payload Data untuk WordPress
data = {
    "title": "Test Antigravity Agent",
    "content": divi_content,
    "status": "draft" 
}

# Tambahkan User-Agent palsu agar menyerupai browser Chrome di Windows
custom_headers = {
    "Content-Type": "application/json",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

print("Mengirim request ke WordPress dengan penyamaran browser...")
# Eksekusi HTTP POST Request
response = requests.post(
    WP_URL,
    auth=(USERNAME, APP_PASSWORD),
    headers=custom_headers,
    data=json.dumps(data)
)

# Cek Hasil
if response.status_code == 201:
    print(f"Sukses! Halaman berhasil dibuat. Cek dashboard WordPress kamu.")
    print(f"Link Draft: {response.json().get('link')}")
else:
    print(f"Gagal: {response.status_code}")
    print(response.text)