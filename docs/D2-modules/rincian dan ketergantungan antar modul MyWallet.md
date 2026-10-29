#  Rincian Modul

Aplikasi My Wallet dibagi menjadi 5 modul. Rincian tiap modul ada di folder D2-modules

1. ### Sumber Uang
2. ### Pemasukan
3. ### Pengeluaran
4. ### Tabungan
5. ### Laporan & Notifikasi

# Ketergantungan Antar Modul

| Modul | Bergantung pada | Alasan |
|---|---|---|
| Pemasukan | Sumber Uang | Uang masuk dicatat ke sumber uang yang dipilih |
| Pengeluaran | Sumber Uang | Pengeluaran dicek terhadap uang tersedia di sumber yang dipilih |
| Pengeluaran | Tabungan | Saldo menggantung berasal dari modul Tabungan |
| Tabungan | Pemasukan | Tabungan masuk diambil dari saldo pemasukan |
| Tabungan | Pengeluaran | Alokasi saldo menggantung dicatat sebagai pengeluaran |
| Laporan & Notifikasi | Sumber Uang, Pemasukan, Pengeluaran, Tabungan | Laporan menjumlahkan semua saldo |
