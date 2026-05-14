# 🐾 QwenPaw Persistent: Perpetual AI Workspace on Hugging Face

Unlock the full power of **QwenPaw** on Hugging Face Spaces tanpa takut kehilangan data. Repositori ini menyediakan integrasi mulus dengan **Supabase Storage** untuk memastikan riwayat chat, API keys, konfigurasi agen, dan file proyek Anda tersimpan selamanya.

## 🚀 Quick Deploy
Gunakan tombol di bawah ini untuk langsung menduplikasi workspace ini ke akun Hugging Face Anda:

[![Deploy on Spaces](https://huggingface.co/datasets/huggingface/badges/resolve/main/deploy-on-spaces-lg.svg)](https://huggingface.co/spaces/jualhosting/qwenpaw-free?duplicate=true)

> **Penting:** Setelah melakukan duplikasi, Anda wajib mengonfigurasi Supabase Secrets (lihat Langkah 2) agar fitur auto-save berfungsi.

## 🌟 Mengapa Menggunakan Proyek Ini?
Secara default, Hugging Face Spaces menggunakan penyimpanan efemeral—artinya setiap kali Space restart atau *sleep*, semua data Anda akan terhapus. Proyek ini mengatasi masalah tersebut dengan menyinkronkan seluruh workspace Anda ke bucket Supabase setiap 5 menit.

Ini adalah solusi **Zero-Cost SaaS Architecture**, memanfaatkan tier gratis dari Hugging Face dan Supabase untuk mendapatkan AI workspace yang tangguh tanpa biaya bulanan.

## ✨ Fitur Utama
* **Automated State Sync:** Mengunggah perubahan workspace ke cloud secara otomatis setiap 5 menit.
* **Auto-Restore on Boot:** Mengunduh backup terbaru dari Supabase saat Space dinyalakan.
* **Zero-Cost Infrastructure:** Berjalan sepenuhnya di layanan cloud tier gratis.
* **Secure Secrets:** Menggunakan variabel rahasia Hugging Face untuk melindungi kredensial database Anda.

## 🛠️ Langkah 1: Persiapan Supabase (Cloud Hard Drive Anda)
1.  **Buat Proyek:** Daftar di [Supabase.com](https://supabase.com) dan buat proyek baru.
2.  **Buat Bucket:** Buka menu **Storage** -> **New Bucket**. Beri nama `qwenpaw-data`.
3.  **Ambil API Keys:** Buka **Project Settings** -> **API**. Anda akan membutuhkan:
    * `Project URL`
    * `service_role` key (Jangan bagikan key ini kepada siapapun!)

## 📦 Langkah 2: Konfigurasi Hugging Face
Pada Space yang sudah Anda duplikasi, lakukan pengaturan berikut:
1.  Buka tab **Settings** -> **Variables and Secrets**.
2.  Tambahkan **Secrets** berikut:
    * `SUPABASE_URL`: URL Proyek Supabase Anda.
    * `SUPABASE_KEY`: `service_role` key Supabase Anda.
    * `QWENPAW_AUTH_ENABLED`: `true`
    * `QWENPAW_AUTH_USERNAME`: Username pilihan Anda (contoh: `admin`).
    * `QWENPAW_AUTH_PASSWORD`: Password yang aman.

## 📂 File yang Disertakan
* `Dockerfile`: Script build khusus untuk menangani auto-restore dan sinkronisasi berkala.
* `sync.py`: Mesin sinkronisasi inti antara lingkungan HF dan Supabase.
* `requirements.txt`: Driver Python yang dibutuhkan untuk koneksi Supabase.

## 💡 Cara Penggunaan
Setelah dideploy, QwenPaw akan otomatis mengunduh backup terbaru saat startup. Setiap 5 menit, sistem akan menyimpan kondisi terbaru (chat, agen, atau file baru) kembali ke Supabase.

Untuk memicu backup secara manual kapan saja, cukup ketik perintah ini di chat QwenPaw:
> "Run shell command: `python3 /app/sync.py upload`"

## 🛡️ Catatan Keamanan
Pastikan Space Anda diatur ke **Private** jika Anda menginginkan keamanan maksimal. Semua kunci sensitif disimpan di Hugging Face Secrets yang terenkripsi dan tersembunyi dari pengguna yang tidak berwenang.

---
*Dibuat untuk komunitas AI oleh [JualHosting](https://jualhosting.com).*
