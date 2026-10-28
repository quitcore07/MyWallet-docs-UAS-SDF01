# MyWallet-docs-UAS-SDF01

# My Wallet

My Wallet adalah aplikasi web pencatat keuangan untuk mahasiswa. Aplikasi ini membantu mahasiswa mencatat pemasukan dan pengeluaran, mengelompokkannya per kategori, dan memantau sisa anggaran bulanan.

Proyek ini dibuat untuk UAS mata kuliah **Software Development Fundamentals** (take-home project kelompok).

## Anggota Tim

| Nama | NIM | GitHub |
|---|---|---|
| Ubay Abdillah | 26110300020 | @quitcore07 |
| Muhammad Irsyad Syafei | 26110300007 | @KyroCode-001 |
| Muhammad Rafie Fahmy | 26110300030 | @rafiefahmi2905-dev |

## Tautan Deliverable
| Deliverable | File |
|---|---|
| D1 – Problem Statement | [docs/D1-problem-statement.md](docs/D1-problem-statement.md) |
| D2 – Modul | [docs/D2-modules/](docs/D2-modules/) |
| D3 – Use Case | [docs/D3-use-case/](docs/D3-use-case/) |
| D4 – Sequence | [docs/D4-squence](docs/D4-squence) |
| D5 – Kolaborasi | [ACTIVITY_LOG.md](ACTIVITY_LOG.md) |
| D6 – Test Case | [docs/D6-test-cases.md](docs/D6-test-cases.md) |
| D7 – Kode & Unit Test | [docs/src](docs/src) |

## Cara Menjalankan Test

Fungsi yang diuji ada di `docs/src/fungsi_wallet.py`, dan unit test-nya ada di `docs/src/test_wallet.py`.

1. Install pytest (cukup sekali):

pip install pytest

2. Jalankan test dari folder utama repo:

pytest docs/src


Hasil yang diharapkan: `11 passed`. Screenshot hasil test: [docs/src/Hasil-test-fungsi.jpg](docs/src/Hasil-test-fungsi.jpg)
## Penggunaan AI

| Anggota | AI yang dipakai | Dipakai untuk |
|---|---|---|
| Ubay Abdillah | Claude | D1: draft awal nama aplikasi dan deskripsi |
| Muhammad Rafie Fahmi | Gemini | D1: menyusun latar belakang masalah dan membuat user |
| Ubay Abdillah | Claude | D2: membuat modules, yang berisi 5 modul.md |
| Ubay Abdillah | Claude | D6: membuat desain test, berisi 10 test |
| Muhammad Rafie Fahmi | Gemini | D3: membuat use case diagram (code puml) |
| Muhammad Rafie Fahmi | Gemini | D4: membuat skenario 2 squence-pengeluaran |
| Ubay Abdillah | Claude | D4:  membuat skenario 1 squence-pemasukan |
| Muhammad Irsyad Syafei | ZCode | D1: membuat ruang lingkup dan keunggulan serta kekurangan dari my wallet |
| Muhammad Irsyad Syafei | ZCode | D4: membuat skenario 3 sequence-tabungan |
| Muhammad Irsyad Syafei | ZCode | D5: draft tabel tautan deliverable di README, lalu direvisi sendiri |
| Muhammad Irsyad Syafei | ZCode | D5: menelaah kesesuaian repo dengan spec dan menyusun draf entri activity log |
