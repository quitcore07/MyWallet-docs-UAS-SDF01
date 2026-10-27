## 📝 Nama Aplikasi & Deskripsi

**My Wallet** adalah aplikasi pencatat keuangan untuk mahasiswa. Pengguna mencatat sendiri uang masuk, uang keluar, dan tabungan dari berbagai sumber uang (cash dan e-money), mengelompokkan tabungan ke beberapa impian, lalu melihat sisa uangnya dalam bentuk laporan yang juga dikirim otomatis lewat notifikasi setiap tanggal 1.

## ⚠️ Pernyataan Masalah

Mahasiswa yang mengelola uangnya sendiri biasanya memegang uang di banyak tempat sekaligus: cash di dompet, rekening bank, dan e-wallet seperti Dana, GoPay, dan ShopeePay. Pemasukannya pun datang dari berbagai sumber, misalnya pemberian orang tua, gaji kerja, pengembalian hutang dari teman, atau uang tak terduga seperti dikasih teman.

Saat ini, kebanyakan mahasiswa mencatatnya seadanya: lewat aplikasi catatan di HP, mengandalkan ingatan, atau tidak mencatat sama sekali. Catatan seperti itu tidak memisahkan cash dan e-money, tidak mengelompokkan pengeluaran per kategori, dan tidak menghitung sisa uang secara otomatis.

Akibatnya, mahasiswa sulit mengetahui sisa uang di tiap tempat dan ke mana uangnya pergi. Uang tabungan juga mudah tercampur dengan uang sehari-hari, sehingga tabungan untuk tujuan tertentu, seperti motor atau HP, sulit dipantau perkembangannya.

## 👤 Pengguna Target / Aktor

| Aktor | Peran |
|---|---|
| **Mahasiswa (Pengguna)** | Memilih sumber uang, mencatat pemasukan, pengeluaran, dan tabungan, serta melihat laporan sisa uang kapan saja (misalnya meminta laporan di tanggal 2 tanpa menunggu tanggal 1 bulan berikutnya). |
| **Sistem Notifikasi** | Mengirim laporan sisa uang secara otomatis setiap tanggal 1 pukul 00:00. |

## 🎯 Ruang Lingkup

### Yang akan dilakukan aplikasi

**1. Sumber uang.** Pengguna memilih sumber uang yang dipakai:
- **Cash**
- **E-money**: bank, Dana, GoPay, ShopeePay

**2. Fitur utama**

| Fitur | Isi |
|---|---|
| **Pemasukan** | Pemberian orang tua, gaji, pengembalian hutang, **lainnya** (misalnya dikasih teman atau menemukan uang) |
| **Pengeluaran** | Kebutuhan bulanan, kebutuhan harian, jajan, memberi hutang, **lainnya** (di luar kategori yang tersedia). Pengeluaran ditolak jika melebihi uang tersedia. |
| **Tabungan** | Tabungan masuk dan tabungan keluar, dibagi ke beberapa tabungan impian |

**Alur tabungan:**
- **Tabungan masuk** berasal dari pemasukan.
- **Tabungan keluar** diambil dari tabungan impian tertentu dan disimpan sebagai **saldo menggantung**, lalu pengguna sendiri yang menentukan masuk ke kategori pengeluaran yang mana. Tabungan keluar tidak boleh melebihi saldo tabungan impian tersebut.

**Tabungan impian:**
Pengguna bisa punya **beberapa tabungan sekaligus**, masing-masing untuk satu impian, misalnya tabungan motor atau tabungan HP.
- Setiap tabungan punya **catatan sendiri**, jadi uang untuk motor tidak tercampur dengan uang untuk HP.
- Setiap tabungan menampilkan **jumlah yang sudah terkumpul**. Tabungan yang baru dibuat dimulai dari nol, lalu bertambah setiap kali ada tabungan masuk.
- **Target nominal bersifat opsional**, tergantung pengguna:
  - Jika pengguna hanya menyebut barang yang diinginkan (misalnya "motor") tanpa harga, tabungan hanya menampilkan jumlah terkumpul, tanpa persentase.
  - Jika pengguna mengisi harga (misalnya Rp20.000.000), aplikasi menampilkan **persentase progres** dari jumlah terkumpul terhadap harga tersebut.
- Tabungan keluar juga dicatat per tabungan, sehingga jumlah terkumpul selalu menunjukkan sisa yang ada.

**3. Laporan sisa uang**
- Menampilkan rincian **cash** dan **e-money**, termasuk saldo menggantung dan saldo tabungan impian, lalu **total** keseluruhan.
- Dikirim otomatis lewat **notifikasi setiap tanggal 1 pukul 00:00**.
- Bisa dilihat kapan saja oleh pengguna.

**4. Pencatatan manual.** Seluruh data diinput sendiri oleh pengguna.

### Yang tidak akan dilakukan aplikasi

1. **Tidak terhubung otomatis ke bank atau e-wallet.** Saldo tidak disinkronkan, semua data diinput manual oleh pengguna.
2. **Tidak menyediakan anggaran (budget) bulanan.** Aplikasi mencatat dan melaporkan, tidak menetapkan batas pengeluaran.
3. **Tidak memindahkan uang sungguhan.** Aplikasi hanya mencatat, bukan untuk transfer, top-up, atau pembayaran.

## ✅ Keunggulan

- **Sumber uang terpisah.** Cash dan e-money dicatat sendiri-sendiri, jadi sisa uang di tiap tempat jelas.
- **Tabungan terpisah dari uang harian.** Tabungan punya alur masuk dan keluar sendiri, sehingga tidak tercampur.
- **Tabungan terstruktur per impian.** Tiap impian (motor, HP, dan lainnya) punya jumlah terkumpul sendiri, jadi progresnya mudah dilihat, dengan persentase jika pengguna mengisi target harga.
- **Laporan otomatis dan bisa dilihat kapan saja.** Notifikasi sisa uang datang tiap tanggal 1, dan pengguna tetap bisa membukanya sewaktu-waktu.
- **Pencatatan fleksibel.** Ada opsi "Lainnya" untuk pemasukan dan pengeluaran yang tidak terduga.
- **Tidak perlu menghubungkan akun bank atau e-wallet.** Pengguna hanya menginput data sendiri.

## ⚠️ Kekurangan

- **Bergantung pada kedisiplinan pengguna.** Karena manual, transaksi yang lupa dicatat membuat laporan tidak akurat.
- **Saldo tidak otomatis sama dengan saldo asli.** Tidak ada sinkronisasi dengan bank atau e-wallet, jadi bisa berbeda kalau pencatatan terlewat.
- **Belum ada anggaran atau batas pengeluaran.** Aplikasi mencatat dan melaporkan, tetapi tidak membatasi pengeluaran.
- **Laporan otomatis hanya sebulan sekali.** Untuk melihat kondisi di tengah bulan, pengguna harus membukanya sendiri.
