<div align="center">

  <!-- BADGE HEADER -->
  <img src="https://ormawa.um.ac.id/wp-content/uploads/2020/09/cropped-logo-um-32x32.png" alt="Logo UM" width="72" height="72" style="margin-bottom: 12px;" />

  # 🌟 Portal Resmi UKM Al-Qur'an Study Club (ASC)
  ### **Universitas Negeri Malang (UM)**

  <p align="center">
    <em>"Membina Generasi Qur'ani yang Berkarakter, Berprestasi, dan Berkontribusi Nyata."</em>
  </p>

  <!-- SHIELDS.IO BADGES -->
  <p align="center">
    <a href="https://maskaiki.github.io/Website-UKM-ASC/"><img src="https://img.shields.io/badge/Demo%20Live-GitHub%20Pages-0284c7?style=for-the-badge&logo=githubpages&logoColor=white" alt="Live Demo" /></a>
    <img src="https://img.shields.io/badge/Tech-HTML5%20%7C%20CSS3%20%7C%20JS%20ES6+-38bdf8?style=for-the-badge&logo=javascript&logoColor=white" alt="Tech Stack" />
    <img src="https://img.shields.io/badge/Architecture-Modular%20Blade%20Pattern-0f172a?style=for-the-badge&logo=laravel&logoColor=white" alt="Modular Architecture" />
    <img src="https://img.shields.io/badge/WordPress-100%25%20Compatible-21759b?style=for-the-badge&logo=wordpress&logoColor=white" alt="WordPress Ready" />
    <img src="https://img.shields.io/badge/Status-Production%20Ready-10b981?style=for-the-badge" alt="Status Ready" />
  </p>

  <!-- QUICK ACTION BUTTONS -->
  <p align="center">
    <a href="https://maskaiki.github.io/Website-UKM-ASC/"><b>🌐 Buka Live Website »</b></a> •
    <a href="#-arsitektur-modular-blade-system"><b>🧩 Arsitektur Komponen</b></a> •
    <a href="#-cara-menjalankan-secara-lokal"><b>💻 Quick Start</b></a> •
    <a href="#-deployment-ke-github-pages"><b>🚀 Panduan Deploy</b></a>
  </p>

</div>

---

## 📖 Tentang Proyek

Repositori ini memuat kode sumber resmi untuk **Portal Web UKM Al-Qur'an Study Club (ASC) Universitas Negeri Malang**. Dibangun dengan estetika modern **Sky Blue Glassmorphism**, terinspirasi dari standar desain web modern generasi terbaru (*Aeline & Plarium interactive dynamics*).

Website dirancang dengan sistem **Modular Self-Contained Section**:
1. **GitHub Pages Ready:** Menggunakan *Master Blade Loader* di `index.html` yang ringan (~13 KB) dan memuat setiap modul secara asinkron.
2. **WordPress Copas Ready:** Setiap komponen mandiri (HTML + CSS + JS terisolasi) sehingga dapat langsung di-copas ke dalam modul **Divi (Code Module)** atau **Elementor (HTML Widget)** tanpa konflik style dengan tema WordPress.

---

## ✨ Fitur-Fitur Unggulan

* 💎 **Ultra-Clean Floating Capsule Navbar:** Navbar melayang dengan efek glassmorphism, morphing saat di-scroll, offset smooth scrolling (85px), dan indikator *Dynamic Scroll Spy*.
* 📱 **Mobile Drawer Navigation:** Menu mobile interaktif lengkap dengan navigasi roadmap per-section dan tombol escape/click-outside listener.
* ☁️ **Hero Sky Floating Experience:** Latar gradasi langit dinamis berpadu dengan animasi awan melayang (*parallax drift*) dan kartu informasi berfitur *3D Mouse Tilt*.
* 📜 **Kinetic Scroll Visi & Misi:** Tipografi interaktif yang kata-katanya menyala dan muncul bertahap seiring pergerakan scroll pembaca.
* 🗺️ **Interactive Journey Timeline Sejarah:** Rekam jejak perjalanan ASC sejak 2010 disajikan di atas kurva garis interaktif dengan kamera *SVG path tracking*.
* 🏛️ **3D Bagan Struktur Organisasi & Stepper:** Visualisasi hierarki BPH, Divisi, hingga LSO dengan detail kartu program kerja yang berubah dinamis saat discroll.
* 📖 **10 Bidang Pembinaan (Scroll Story 520vh):** Galeri horizontal bertingkat menampilkan kelas Tilawah, Tahfidh, Kaligrafi, KTIA, dsb.
* 🖼️ **Galeri Kegiatan & Modal Dialog:** Dokumentasi foto kegiatan bersistem *pinned layout 480vh* dengan pop-up modal aksesibel (mendukung tombol ESC & fokus trap).
* 🏆 **Trophy Showcase Prestasi:** Menampilkan pencapaian kafilah ASC di ajang MTQ Mahasiswa Nasional & regional dengan kartu medali emas, perak, dan perunggu.
* ✨ **Plarium Social Media Cards & Particle Canvas:** Animasi kartu media sosial dengan efek partikel cahaya kanvas interaktif dan hub kontak narahubung lengkap.

---

## 🧩 Arsitektur Modular (Blade System)

Website ini menggunakan prinsip *Single Responsibility Component*. Setiap section disimpan di file terpisah agar memudahkan tim dalam mengedit tanpa takut merusak section lain:

| No | File Komponen | Target DOM ID | Fungsi & Interaktivitas |
|:---:|:---|:---|:---|
| **00** | [`00_header.html`](00_header.html) | `#asc-header-navbar` | Floating Glass Capsule, Mobile Drawer, & Dynamic Scroll Spy |
| **01** | [`01_profil.html`](01_profil.html) | `#asc-hero-profil` | Hero Section, Awan Parallax, & Kartu 3D Tilt |
| **02** | [`02_visi_misi.html`](02_visi_misi.html) | `#asc-vm` | Kinetic Typography Scroll & Audio Waveform aesthetic |
| **03** | [`03_sejarah.html`](03_sejarah.html) | `#asc-sj` | Milestone Garis Waktu Interaktif (2010 - Sekarang) |
| **03** | [`03_struktur_organisasi.html`](03_struktur_organisasi.html) | `#asc-struktur` | Bagan Hierarki, Stepper Navigasi, Kartu Departemen & LSO |
| **04** | [`04_pengumuman_agenda.html`](04_pengumuman_agenda.html) | `#asc-pb` | 10 Bidang Pembinaan (Pinned Horizontal Track 520vh) |
| **05** | [`05_galeri.html`](05_galeri.html) | `#asc-galeri` | Pinned Galeri Foto (480vh) & Accessible Modal Detail |
| **06** | [`06_prestasi.html`](06_prestasi.html) | `#asc-prestasi` | Statistik Juara, Kartu Trofi MTQMN, & Medali |
| **07** | [`07_link_medsos.html`](07_link_medsos.html) | `#asc-kontak` | Plarium Interactive Cards, Particle Canvas, & Hub Sekretariat |

> **💡 Mengapa sangat praktis?**  
> Jika Anda mengedit konten di `03_struktur_organisasi.html` atau file modul lainnya, **halaman `index.html` otomatis menampilkan versi terbaru** tanpa perlu Anda salin-tempel ulang manual!

---

## 💻 Cara Menjalankan Secara Lokal

### Prasyarat
* Komputer dengan Python 3.x (atau ekstensi Live Server di VS Code).

### Langkah Menjalankan:
1. **Clone repository ini:**
   ```bash
   git clone https://github.com/maskaiki/Website-UKM-ASC.git
   cd Website-UKM-ASC
   ```

2. **Jalankan development server bawaan:**
   ```bash
   python build.py --serve
   ```
   *Browser Anda akan otomatis terbuka di `http://localhost:8000/index.html`!*

3. **Ingin mengompilasi menjadi satu file tunggal untuk WordPress?**
   Jalankan:
   ```bash
   python build.py
   ```
   Perintah ini akan menggabungkan seluruh komponen menjadi `index.standalone.html` yang siap di-copas ke Elementor/Divi.

---

## 🚀 Deployment ke GitHub Pages

Repositori ini sudah dioptimalkan untuk langsung tayang di **GitHub Pages**:

1. Pastikan seluruh perubahan sudah di-commit dan di-push:
   ```bash
   git add .
   git commit -m "feat: publish updated portal"
   git push origin <nama-branch>
   ```
2. Buka menu **Settings** di repositori GitHub Anda.
3. Masuk ke tab **Pages** (di sidebar kiri).
4. Di bagian **Build and deployment > Branch**:
   * Pilih branch yang ingin dideploy (misalnya `dev-asyam` atau `main`).
   * Pilih folder `/ (root)`.
   * Klik **Save**.
5. Tunggu sekitar 1-2 menit, website resmi akan online di:
   ```
   https://<username-github>.github.io/Website-UKM-ASC/
   ```

*(Catatan: File `.nojekyll` sudah disediakan di root folder agar seluruh file HTML termuat tanpa hambatan parser).*

---

## 📂 Struktur Direktori

```plaintext
Website-UKM-ASC/
├── .nojekyll                   # Menjamin GitHub Pages menyajikan raw static assets
├── build.py                    # Dev server & standalone compiler tool
├── index.html                  # Master Template (Blade Component Loader Engine)
├── index.standalone.html       # Hasil kompilasi bundel offline all-in-one
├── 00_header.html              # Komponen 00: Navbar Melayang & Drawer
├── 01_profil.html              # Komponen 01: Hero Profil & Bento Stats
├── 02_visi_misi.html           # Komponen 02: Visi & Misi Kinetic Scroll
├── 03_sejarah.html             # Komponen 03: Sejarah Perjalanan ASC
├── 03_struktur_organisasi.html # Komponen 03: Bagan Struktur Organisasi 3D
├── 04_pengumuman_agenda.html   # Komponen 04: 10 Bidang Pembinaan (Scroll Track)
├── 05_galeri.html              # Komponen 05: Galeri Kegiatan & Lightbox Modal
├── 06_prestasi.html            # Komponen 06: Prestasi MTQMN & Trophy Cards
├── 07_link_medsos.html         # Komponen 07: Follow Us, Partikel Canvas, & Footer
├── galeri/                     # Aset gambar & dokumentasi tangkapan layar
└── referensi/                  # Aset inspirasi layout & materi pendukung
```

---

## 🛠️ Standar Kode & Kompatibilitas

* **Zero Dependencies:** 100% Native Vanilla JavaScript & Modern CSS Grid/Flexbox tanpa framework besar (tidak membutuhkan React, Vue, atau Tailwind) sehingga waktu muat halaman mendekati instan.
* **WordPress Theme Shield:** Dilengkapi aturan CSS reset `#asc-... *` dan *auto-fix overflow* untuk mencegah bug layout saat disematkan ke dalam tema WordPress (Divi, Elementor, Astra, GeneratePress, dll).
* **Hardware Accelerated:** Animasi scroll memanfaatkan `translate3d`, `scale`, dan `opacity` untuk menjamin performa stabil di 60 FPS pada desktop maupun perangkat seluler.

---

## 👥 Kontribusi & Pemeliharaan

Kontribusi dan saran perbaikan sangat disambut baik!
1. **Fork** repositori ini.
2. Buat branch fitur baru (`git checkout -b fitur/nama-fitur`).
3. Commit perubahan Anda (`git commit -m 'feat: menambahkan fitur baru'`).
4. Push ke branch Anda (`git push origin fitur/nama-fitur`).
5. Buat **Pull Request**.

---

## 🏛️ Hubungi Kami

**Unit Kegiatan Mahasiswa Al-Qur'an Study Club (UKM ASC)**  
**Universitas Negeri Malang (UM)**  
* 📍 **Sekretariat:** Gedung UKM Bersama, Kampus 1 Universitas Negeri Malang, Jl. Semarang No. 5, Malang, Jawa Timur.  
* 📸 **Instagram:** [@ukmascum](https://instagram.com/ukmascum)  
* 🎥 **YouTube:** [UKM ASC UM Official](https://youtube.com)  
* 🌐 **Website Ormawa:** [ormawa.um.ac.id](https://ormawa.um.ac.id)  

---

<div align="center">
  <sub>Dikelola dengan ❤️ dan dedikasi oleh Pengurus & Kafilah <b>UKM ASC Universitas Negeri Malang</b>.</sub>
</div>
