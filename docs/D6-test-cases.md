# D6. Test Case Design

**Skenario yang dipilih:** Mencatat pengeluaran dari sumber uang (cash atau e-money), termasuk pengeluaran dari saldo tabungan keluar yang menggantung.

**Aturan yang diuji** (dihitung terpisah untuk cash dan e-money):

- **Uang tersedia** = pemasukan − tabungan masuk − pengeluaran biasa
- **Saldo tabungan** = tabungan masuk − tabungan keluar
- **Saldo menggantung** = tabungan keluar − alokasi ke kategori pengeluaran
- **Total uang** = uang tersedia + saldo menggantung + saldo tabungan
- Pengeluaran biasa hanya diterima jika nominalnya tidak melebihi uang tersedia.
- Alokasi dari saldo menggantung hanya diterima jika nominalnya tidak melebihi saldo menggantung.
- Tabungan keluar hanya diterima jika nominalnya tidak melebihi saldo tabungan.

Minimal 10 test case: 5 kasus umum (Common) dan 5 kasus batas (Edge).

| ID | Judul | Tipe | Prasyarat | Input / Langkah | Hasil yang Diharapkan |
|---|---|---|---|---|---|
| TC-01 | Catat pemasukan dari orang tua ke cash | Umum | Login; saldo cash 0 | Pilih Cash → pemasukan "Pemberian orang tua" 50.000 → simpan | Uang tersedia cash 50.000 |
| TC-02 | Catat pengeluaran jajan dari uang tersedia | Umum | Cash tersedia 50.000 | Pilih Cash → pengeluaran "Jajan" 20.000 → simpan | Diterima; uang tersedia cash 30.000 |
| TC-03 | Tabungan masuk diambil dari pemasukan | Umum | Pemasukan cash 100.000 | Pilih Cash → tabungan masuk 40.000 → simpan | Uang tersedia cash 60.000; saldo tabungan 40.000 |
| TC-04 | Tabungan keluar menjadi saldo menggantung | Umum | Saldo tabungan cash 40.000; uang tersedia cash 30.000 | Pilih Cash → tabungan keluar 25.000 → simpan | Saldo tabungan 15.000; saldo menggantung cash 25.000; uang tersedia tetap 30.000 |
| TC-05 | Alokasi saldo menggantung ke kategori | Umum | Saldo menggantung cash 25.000 | Pilih Cash → alokasi ke "Kebutuhan bulanan" 15.000 → simpan | Tercatat sebagai pengeluaran; saldo menggantung 10.000 |
| TC-06 | Laporan menampilkan rincian dan total | Umum | Uang tersedia cash 30.000; saldo menggantung 10.000; saldo tabungan 15.000 | Buka laporan sisa uang | Cash 30.000 + menggantung 10.000 + tabungan 15.000 = total 55.000 |
| TC-07 | Pengeluaran melebihi uang tersedia | Edge | Uang tersedia cash 30.000 | Pilih Cash → pengeluaran "Jajan" 50.000 → simpan | Ditolak "Uang tidak cukup"; transaksi tidak tersimpan; uang tersedia tetap 30.000 |
| TC-08 | Pengeluaran sama persis dengan uang tersedia | Edge | Uang tersedia cash 30.000 | Pilih Cash → pengeluaran "Jajan" 30.000 → simpan | Diterima; uang tersedia 0 |
| TC-09 | Alokasi melebihi saldo menggantung | Edge | Saldo menggantung cash 10.000 | Pilih Cash → alokasi "Kebutuhan bulanan" 15.000 → simpan | Ditolak "Saldo menggantung tidak cukup"; saldo menggantung tetap 10.000 |
| TC-10 | Tabungan keluar melebihi saldo tabungan | Edge | Saldo tabungan cash 15.000 | Pilih Cash → tabungan keluar 20.000 → simpan | Ditolak "Saldo tabungan tidak cukup"; saldo tabungan tetap 15.000 |
| TC-11 | Nominal kosong, nol, negatif, atau bukan angka | Edge | Login | (a) kosong; (b) 0; (c) -10.000; (d) "dua puluh ribu" → simpan | (a) "Nominal wajib diisi"; (b) dan (c) "Nominal harus lebih dari 0"; (d) "Nominal harus berupa angka" |

## Cara Memilih Edge Case

Kasus batas dipilih dari tiga aturan inti: pengeluaran tidak boleh melebihi uang tersedia, alokasi tidak boleh melebihi saldo menggantung, dan tabungan keluar tidak boleh melebihi saldo tabungan. Ketiganya paling sering dilanggar kalau dicatat manual, jadi dicek di nilai tepat (TC-08), melewati batas (TC-07, TC-09, TC-10), dan input tidak masuk akal (TC-11). Setiap kasus punya pesan dan hasil yang jelas, sehingga bisa dicocokkan langsung dengan unit test di D7.
