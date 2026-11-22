# ============================================================
# File   : anggota.py
# Isi    : Class Anggota perpustakaan
# ============================================================


class Anggota:
    """Mewakili anggota perpustakaan."""

    BATAS_PINJAM = 3  # atribut class: maksimal buku yang boleh dipinjam bersamaan

    # Constructor berparameter
    def __init__(self, id_anggota, nama, kontak):
        self.__id = id_anggota
        self.__nama = nama
        self.__kontak = kontak
        self.__jumlah_pinjam = 0  # jumlah buku yang sedang dipinjam

    # ---------- GETTER ----------
    def get_id(self):
        return self.__id

    def get_nama(self):
        return self.__nama

    def get_kontak(self):
        return self.__kontak

    def get_jumlah_pinjam(self):
        return self.__jumlah_pinjam

    # ---------- SETTER ----------
    def set_nama(self, nama):
        if nama.strip():
            self.__nama = nama

    def set_kontak(self, kontak):
        if kontak.strip():
            self.__kontak = kontak

    # ---------- METHOD TAMBAHAN ----------
    def bisa_meminjam(self):
        """Cek apakah anggota masih boleh meminjam."""
        return self.__jumlah_pinjam < Anggota.BATAS_PINJAM

    def tambah_pinjam(self):
        self.__jumlah_pinjam += 1

    def kurangi_pinjam(self):
        if self.__jumlah_pinjam > 0:
            self.__jumlah_pinjam -= 1

    def tampilkan_info(self):
        return (f"[{self.__id}] {self.__nama} | Kontak: {self.__kontak} | "
                f"Sedang pinjam: {self.__jumlah_pinjam}/{Anggota.BATAS_PINJAM}")