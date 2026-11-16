# Mesin Riset Taste & Auto-Improve UKM ASC (Maksimal 10 Iterasi)
Current_Iteration: 1
Max_Iteration: 10

## Aturan Kunci (Guardrails — DILARANG DILANGGAR)
1. Tema WAJIB tetap Light/White Editorial (#FFFFFF & #F7F7F5) dengan teks #0B0A0F, aksen #143B66 (Sapphire) & #5C3A28 (Cokelat PDH).
2. Font WAJIB tetap Geist & Geist Mono.
3. Dari riset web luar, AMBIL HANYA: komposisi grid, micro-interaction, cara hover, proporsi whitespace, dan kehalusan animasi.

## Siklus Kerja di Setiap Iterasi (Ulangi sampai Current_Iteration == 10)
1. **RISET**: Buka/baca referensi desain sesuai topik iterasi di bawah (gunakan pencarian web / browser).
2. **CATAT TASTE**: Tulis 2–3 detail visual/CSS keren yang kamu temukan ke bagian "Log Temuan Taste" di bawah.
3. **TERAPKAN**: Implementasikan teknik tersebut ke `index.html` UKM ASC.
4. **AUDIT & UPDATE**: Pastikan tidak ada error, centang `[x]` pada iterasi tersebut, naikkan `Current_Iteration` +1, lalu LANGSUNG lanjut ke iterasi berikutnya tanpa menunggu perintah user. Berhenti total saat `Current_Iteration: 10`.

---

## Daftar 10 Iterasi & Target Riset Taste
- [x] **Iterasi 1 (Riset Architectural Grid & Hairline Borders)**
  - *Eksplorasi*: Cari pola "Swiss editorial web design grid hairline border" atau amati gaya garis tipis Vercel/Geist.
  - *Terapkan ke ASC*: Buat garis pemisah antar seksi (`1px solid rgba(11,10,15,0.08)`) dan tanda tambah (`+`) halus di sudut-sudut perpotongan grid.
- [ ] **Iterasi 2 (Riset Hero Depth & Cutout Layering)**
  - *Eksplorasi*: Cari referensi "editorial typography behind subject cutout hero web design".
  - *Terapkan ke ASC*: Sempurnakan proporsi teks raksasa `ASC` di belakang foto dua pengurus berjaket PDH, tambahkan bayangan lembut dan efek mengambang saat mouse bergerak.
- [ ] **Iterasi 3 (Riset Kinetic Typography & Staggered Word Reveal)**
  - *Eksplorasi*: Cari referensi animasi kinetic typography ala studio Gobo / Effica.
  - *Terapkan ke ASC*: Efek word-by-word reveal dengan blur dan subtle translateY pada judul-judul utama.
- [ ] **Iterasi 4 (Riset Tactile Bracket Button & Micro-Interactions)**
  - *Eksplorasi*: Cari referensi tombol bracket hover ala Gobo `[ START A PROJECT ]` dan magnetic cursor.
  - *Terapkan ke ASC*: Micro-interaction tactile hover pada tombol bracket `[ DAFTAR SEKARANG ]`, `[ LIHAT SEMUA ]`, cursor hover badge.
- [ ] **Iterasi 5 (Riset Interactive Directory & Sticky Preview)**
  - *Eksplorasi*: Amati table directory interaktif ala editorial portfolio.
  - *Terapkan ke ASC*: 11 Bidang Pembinaan dengan interactive active marker line, preview crossfade, badge jumlah anggota/kategori.
- [ ] **Iterasi 6 (Riset Light-Mode Bento Grid untuk Metrik & Prestasi)**
  - *Eksplorasi*: Cari referensi "Bento grid light mode UI Stripe Press Linear".
  - *Terapkan ke ASC*: Tampilan bento grid modern untuk metrik (4x Juara Umum MTQMN, 11 Bidang, dsb) dengan subtle inset shadows dan typography hierarchy.
- [ ] **Iterasi 7 (Riset Filter & View Switcher [GRID] / [LIST])**
  - *Eksplorasi*: Filter bar interaktif modern dengan layout switch animatif.
  - *Terapkan ke ASC*: Sempurnakan filter Program Kerja dan Galeri dengan smooth layout transition.
- [ ] **Iterasi 8 (Riset Horizontal Accordion & Team Slices)**
  - *Eksplorasi*: Desain slice accordion pengurus/tim interaktif ala editorial studio.
  - *Terapkan ke ASC*: Sempurnakan flex-grow accordion kartu struktur kepengurusan dengan info reveal yang elegan.
- [ ] **Iterasi 9 (Riset Editorial FAQ, Testimoni, Form & Footer WIB Clock)**
  - *Eksplorasi*: Modern clean FAQ accordion, marquee/quote testimonial cards, form floating focus, live time clock.
  - *Terapkan ke ASC*: Polish visual FAQ, Testimoni, Form Hubungi Kami, dan live WIB digital clock di footer.
- [ ] **Iterasi 10 (Final 60fps Polish, Standalone Export & Verification)**
  - *Eksplorasi*: Audit performance CSS/JS, memory leak prevention, layout stability (CLS = 0).
  - *Terapkan ke ASC*: Clean up, compile `index.standalone.html`, run `build.py --check`, pastikan 100% copas-ready tanpa external asset breakdown.

---

## Log Temuan Taste
### Iterasi 1 — Swiss Grid & Hairline Borders
- **Temuan 1 (Corner Crosses `+` Architecture)**: Vercel & Swiss International Typographic Style menggunakan penanda perpotongan grid berupa tanda tambah (`+`) halus berukuran 11px monospace di titik batas seksi (`.section-hairline-bound::before` dan `::after`). Ini memberikan jangkar visual arsitektural yang presisi tanpa memberatkan halaman.
- **Temuan 2 (Hairline Guide Divider)**: Garis pemisah antar seksi dipertahankan presisi pada `1px solid var(--border)` (`rgba(11, 10, 15, 0.09)`) pada kanvas putih bersih `#FFFFFF`, menciptakan ritme spasial vertikal yang konsisten antara header seksi dan konten.
- **Temuan 3 (Technical Metadata Coordinate)**: Tag monospace indeks teknikal (`01 · PROFIL`, `02 · PEMBINAAN`, dsb.) melengkapi grid layout dengan aksen identitas terstruktur ala publikasi desain modern.
