PESAN_SALDO = {
    "uang": "Uang tidak cukup",
    "menggantung": "Saldo menggantung tidak cukup",
    "tabungan": "Saldo tabungan tidak cukup",
}


def kurangi_saldo(saldo, nominal, jenis="uang"):
    """Mengurangi saldo jika nominal valid dan saldo cukup.

    jenis:
        "uang"        -> uang tersedia (pengeluaran biasa)
        "menggantung" -> saldo menggantung (alokasi ke kategori)
        "tabungan"    -> saldo tabungan (tabungan keluar)

    Mengembalikan saldo baru. Melempar ValueError jika input tidak valid.
    """
    if nominal is None or nominal == "":
        raise ValueError("Nominal wajib diisi")
    if isinstance(nominal, bool) or not isinstance(nominal, (int, float)):
        raise ValueError("Nominal harus berupa angka")
    if nominal <= 0:
        raise ValueError("Nominal harus lebih dari 0")
    if jenis not in PESAN_SALDO:
        raise ValueError("Jenis saldo tidak dikenal")
    if nominal > saldo:
        raise ValueError(PESAN_SALDO[jenis])
    return saldo - nominal