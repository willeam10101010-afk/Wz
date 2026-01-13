# Telegram Bot - Wz

Bot Telegram sederhana yang menyimpan pesan unik ke file Excel (XLSX) dan memeriksa duplikasi pesan.

## 📋 Deskripsi

Bot ini dirancang untuk menerima pesan teks dari pengguna Telegram dan menyimpannya ke dalam file Excel. Setiap pesan yang diterima akan diperiksa terlebih dahulu untuk memastikan tidak ada duplikasi. Jika pesan sudah ada dalam database, bot akan memberitahu pengguna. Jika pesan baru, bot akan menyimpannya dan mengonfirmasi bahwa data dapat digunakan.

## ✨ Fitur

- ✅ Menerima pesan teks dari pengguna Telegram
- ✅ Menyimpan pesan unik ke file Excel (XLSX)
- ✅ Memeriksa duplikasi pesan sebelum menyimpan
- ✅ Memberikan respons otomatis kepada pengguna
- ✅ Logging untuk monitoring aktivitas bot
- ✅ Konfigurasi melalui environment variables
- ✅ Error handling yang baik

## 🛠️ Persyaratan

- Python 3.8 atau lebih tinggi
- Library Python yang diperlukan (lihat `requirements.txt`)

## 📦 Instalasi

### 1. Clone Repository

```bash
git clone https://github.com/willeam10101010-afk/Wz.git
cd Wz
```

### 2. Buat Virtual Environment (Opsional tapi Disarankan)

```bash
python -m venv venv
```

Aktifkan virtual environment:
- **Windows:**
  ```bash
  venv\Scripts\activate
  ```
- **Linux/Mac:**
  ```bash
  source venv/bin/activate
  ```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

## ⚙️ Konfigurasi

### 1. Buat Bot Telegram

1. Buka Telegram dan cari [@BotFather](https://t.me/botfather)
2. Kirim perintah `/newbot`
3. Ikuti instruksi untuk membuat bot baru
4. Simpan **token bot** yang diberikan

### 2. Konfigurasi Environment Variables

Salin file `.env.example` menjadi `.env`:

```bash
cp .env.example .env
```

Edit file `.env` dan masukkan token bot Telegram Anda:

```env
TELEGRAM_BOT_TOKEN=1234567890:ABCdefGHIjklMNOpqrsTUVwxyz
XLSX_FILE=data.xlsx
```

**Catatan:** Jangan pernah membagikan token bot Anda kepada siapa pun!

## 🚀 Cara Penggunaan

### Menjalankan Bot

```bash
python telegram_bot.py
```

Bot akan mulai berjalan dan siap menerima pesan. Anda akan melihat pesan:
```
INFO - Bot started successfully!
```

### Berinteraksi dengan Bot

1. Buka Telegram dan cari bot Anda (berdasarkan username yang Anda buat)
2. Kirim pesan teks apa saja ke bot
3. Bot akan merespons:
   - **"Data dapat digunakan."** - Jika pesan baru dan berhasil disimpan
   - **"Pesan sudah ada di database."** - Jika pesan sudah pernah dikirim sebelumnya

### Menghentikan Bot

Tekan `Ctrl + C` di terminal untuk menghentikan bot.

## 📊 Struktur Data

Bot menyimpan data dalam file Excel (`data.xlsx`) dengan struktur:

| Message |
|---------|
| Pesan 1 |
| Pesan 2 |
| Pesan 3 |

## 📁 Struktur Proyek

```
Wz/
├── .github/
│   └── workflows/
│       └── autocommit.yml    # GitHub Actions workflow
├── .env.example              # Template konfigurasi environment
├── .gitignore               # File yang diabaikan Git
├── requirements.txt         # Dependencies Python
├── telegram_bot.py          # Kode utama bot
├── README.md               # Dokumentasi (file ini)
└── data.xlsx               # File data (dibuat otomatis)
```

## 🔒 Keamanan

- **Jangan commit file `.env`** - File ini berisi token rahasia
- File `.env` sudah ditambahkan ke `.gitignore`
- Gunakan `.env.example` sebagai template tanpa data sensitif
- File `data.xlsx` juga diabaikan oleh Git untuk menjaga privasi data

## 🐛 Troubleshooting

### Bot tidak bisa dimulai

- Pastikan token bot sudah diisi dengan benar di file `.env`
- Periksa koneksi internet Anda
- Pastikan semua dependencies sudah terinstall

### Error saat menyimpan data

- Pastikan Anda memiliki hak akses untuk menulis file di direktori saat ini
- Periksa apakah file `data.xlsx` sedang dibuka di aplikasi lain

### Bot tidak merespons

- Pastikan bot sudah berjalan (tidak ada error di terminal)
- Periksa log untuk melihat pesan error
- Restart bot dengan menekan `Ctrl + C` dan jalankan kembali

## 🤝 Kontribusi

Kontribusi selalu diterima! Jika Anda ingin berkontribusi:

1. Fork repository ini
2. Buat branch baru (`git checkout -b feature/AmazingFeature`)
3. Commit perubahan Anda (`git commit -m 'Add some AmazingFeature'`)
4. Push ke branch (`git push origin feature/AmazingFeature`)
5. Buat Pull Request

## 📝 Lisensi

Proyek ini adalah open source dan tersedia untuk digunakan secara bebas.

## 👤 Author

**willeam10101010-afk**

## 📞 Dukungan

Jika Anda memiliki pertanyaan atau masalah, silakan buka [issue](https://github.com/willeam10101010-afk/Wz/issues) di repository ini.

---

**Selamat menggunakan! 🎉**
