import pytest
from fungsi_wallet import kurangi_saldo


# Kasus umum (sesuai D6)
def test_pengeluaran_jajan_dari_uang_tersedia():          # TC-02
    assert kurangi_saldo(50000, 20000, "uang") == 30000


def test_tabungan_keluar_dari_saldo_tabungan():           # TC-04
    assert kurangi_saldo(40000, 25000, "tabungan") == 15000


def test_alokasi_dari_saldo_menggantung():                # TC-05
    assert kurangi_saldo(25000, 15000, "menggantung") == 10000


# Kasus batas (sesuai D6)
def test_pengeluaran_melebihi_uang_tersedia():            # TC-06
    with pytest.raises(ValueError, match="Uang tidak cukup"):
        kurangi_saldo(30000, 50000, "uang")


def test_pengeluaran_sama_dengan_uang_tersedia():         # TC-07
    assert kurangi_saldo(30000, 30000, "uang") == 0


def test_alokasi_melebihi_saldo_menggantung():            # TC-08
    with pytest.raises(ValueError, match="Saldo menggantung tidak cukup"):
        kurangi_saldo(10000, 15000, "menggantung")


def test_tabungan_keluar_melebihi_saldo_tabungan():       # TC-09
    with pytest.raises(ValueError, match="Saldo tabungan tidak cukup"):
        kurangi_saldo(15000, 20000, "tabungan")


def test_nominal_kosong():                                # TC-10 (a)
    with pytest.raises(ValueError, match="Nominal wajib diisi"):
        kurangi_saldo(30000, "", "uang")


def test_nominal_nol():                                   # TC-10 (b)
    with pytest.raises(ValueError, match="Nominal harus lebih dari 0"):
        kurangi_saldo(30000, 0, "uang")


def test_nominal_negatif():                               # TC-10 (c)
    with pytest.raises(ValueError, match="Nominal harus lebih dari 0"):
        kurangi_saldo(30000, -10000, "uang")


def test_nominal_bukan_angka():                           # TC-10 (d)
    with pytest.raises(ValueError, match="Nominal harus berupa angka"):
        kurangi_saldo(30000, "dua puluh ribu", "uang")