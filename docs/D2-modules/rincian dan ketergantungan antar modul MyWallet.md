#  Rincian Modul

Aplikasi My Wallet dibagi menjadi 5 modul. Rincian tiap modul ada di folder [D2-modules](D2-modules).

1. [Sumber Uang](D2-modules/modul.1-sumber-uang.md)
2. [Pemasukan](D2-modules/modul.2-pemasukan.md)
3. [Pengeluaran](D2-modules/modul.3-pengeluaran.md)
4. [Tabungan](D2-modules/modul.4-tabungan.md)
5. [Laporan & Notifikasi](D2-modules/modul.5-laporan&notif.md)

## Ketergantungan Antar Modul

| Modul | Bergantung pada | Alasan |
|---|---|---|
| Pemasukan | Sumber Uang | Uang masuk dicatat ke sumber uang yang dipilih |
| Pengeluaran | Sumber Uang | Pengeluaran dicek terhadap uang tersedia di sumber yang dipilih |
| Pengeluaran | Tabungan | Saldo menggantung berasal dari modul Tabungan |
| Tabungan | Pemasukan | Tabungan masuk diambil dari saldo pemasukan |
| Tabungan | Pengeluaran | Alokasi saldo menggantung dicatat sebagai pengeluaran |
| Laporan & Notifikasi | Sumber Uang, Pemasukan, Pengeluaran, Tabungan | Laporan menjumlahkan semua saldo |
