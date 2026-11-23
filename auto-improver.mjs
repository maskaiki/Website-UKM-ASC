// File: auto-improver.mjs
// Jalankan dengan: node auto-improver.mjs
// Prasyarat: npm install playwright @google/genai

import fs from 'fs';
import path from 'path';
import { execSync } from 'child_process';
import { chromium } from 'playwright';
import { GoogleGenAI } from '@google/genai';

const ai = new GoogleGenAI({ apiKey: process.env.GEMINI_API_KEY });
const TARGET_FILE = path.resolve('./index.html');
const MAX_ITERATIONS = 10;

// Rubrik fokus per iterasi agar AI tidak mengubah hal yang sama berulang-ulang
const FOCUS_PER_STEP = [
  "1. Whitespace, proporsi padding, dan kebersihan background putih ala Effica.",
  "2. Tipografi Geist & Geist Mono: ketajaman ukuran font, letter-spacing, dan kontras teks.",
  "3. Hero Section: pastikan teks raksasa ASC proporsional di belakang foto cutout dan terlihat megah.",
  "4. Micro-interactions: kehalusan hover tombol [ BRACKET ] dan indikator kursor berkedip ala Gobo.",
  "5. Interaksi 11 Bidang Pembinaan: perjelas visual preview pane saat baris di-hover/klik.",
  "6. Bagian Program Kerja: percantik kartu Grid dan baris List serta animasi filternya.",
  "7. Struktur Kepengurusan: haluskan efek melebar (flex-grow) pada kartu Accordion Slices.",
  "8. Responsivitas Mobile (layar 390px): pastikan tidak ada teks bertumpuk atau horizontal overflow.",
  "9. Bagian Testimoni, FAQ Accordion, dan Formulir Kontak agar terlihat makin kredibel.",
  "10. Final Polish: bersihkan CSS duplikat, pastikan transisi 60fps, dan cek aksesibilitas."
];

async function captureScreenshot(htmlPath, step) {
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1440, height: 900 } });
  await page.goto(`file://${htmlPath}`, { waitUntil: 'networkidle' });
  await page.waitForTimeout(800); // Tunggu animasi awal selesai

  const dir = './iterations-log';
  if (!fs.existsSync(dir)) fs.mkdirSync(dir);
  const shotPath = `${dir}/iterasi-${step}.png`;
  await page.screenshot({ path: shotPath, fullPage: true });
  await browser.close();
  return shotPath;
}

async function runAutoImprover() {
  console.log(`🚀 Memulai Auto-Improver UKM ASC (Maksimal ${MAX_ITERATIONS} Iterasi)...`);

  for (let i = 1; i <= MAX_ITERATIONS; i++) {
    console.log(`\n========================================`);
    console.log(`🔄 MENJALANKAN ITERASI ${i} DARI ${MAX_ITERATIONS}`);
    console.log(`🎯 Fokus: ${FOCUS_PER_STEP[i - 1]}`);
    console.log(`========================================`);

    // 1. Ambil screenshot tampilan saat ini
    const shotPath = await captureScreenshot(TARGET_FILE, i);
    const currentCode = fs.readFileSync(TARGET_FILE, 'utf-8');

    // 2. Kirim ke Gemini untuk dianalisis dan diperbaiki
    const prompt = `Kamu adalah World-Class Frontend Engineer & Design Technologist.
Website ini adalah Website Resmi UKM Al-Qur'an Study Club (ASC) Universitas Negeri Malang.
ATURAN EMAS:
1. Pertahankan tema Light Editorial: background putih bersih (#FFFFFF), surface (#F7F7F5), aksen sapphire (#143B66) & cokelat PDH (#5C3A28).
2. Pertahankan 100% teks bahasa Indonesia asli dan data pengurus/bidang/prestasi.
3. Fokus iterasi ke-${i}: ${FOCUS_PER_STEP[i - 1]}
Kembalikan KODE LENGKAP index.html yang telah kamu perbaiki tanpa penjelasan atau markdown backticks, cukup kodenya saja.`;

    const response = await ai.models.generateContent({
      model: 'gemini-2.5-pro',
      contents: [
        prompt,
        {
          inlineData: {
            mimeType: 'image/png',
            data: fs.readFileSync(shotPath).toString('base64')
          }
        },
        currentCode
      ]
    });

    let newCode = response.text.trim();
    if (newCode.startsWith('```html')) newCode = newCode.slice(7);
    if (newCode.startsWith('```')) newCode = newCode.slice(3);
    if (newCode.endsWith('```')) newCode = newCode.slice(0, -3);

    fs.writeFileSync(TARGET_FILE, newCode.trim(), 'utf-8');
    console.log(`✅ Iterasi ${i} berhasil disimpan ke index.html!`);

    // Git commit per iterasi
    try {
      execSync(`git add index.html && git commit -m "chore(auto-improve): iterasi ${i} - ${FOCUS_PER_STEP[i - 1].slice(0, 40)}"`);
      console.log(`📦 Git commit tercatat untuk iterasi ${i}`);
    } catch (e) {
      console.log(`⚠️ Git commit skipped: ${e.message}`);
    }
  }

  console.log(`\n🎉 SEMUA 10 ITERASI SELESAI! Web UKM ASC kini dalam kondisi puncaknya.`);
}

runAutoImprover().catch(console.error);
