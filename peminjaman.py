# ============================================================
# File   : peminjaman.py
# Isi    : Class Peminjaman (relasi Association)
#          Peminjaman memiliki 1 Anggota dan 1 Buku
# ============================================================
from datetime import date, timedelta


class Peminjaman:
    """Class relasi (association) antara Anggota dan Buku."""

    LAMA_PINJAM = 7       # hari
    DENDA_PER_HARI = 1000  # rupiah

    # Constructor berparameter; menerima OBJEK Anggota dan OBJEK Buku
    def __init__(self, kode, anggota, buku, tgl_pinjam=None):
        self.__kode = kode
        self.__anggota = anggota   # relasi: 1 Anggota
        self.__buku = buku         # relasi: 1 Buku
        self.__tgl_pinjam = tgl_pinjam or date.today()
        self.__tgl_kembali = None  # None = belum dikembalikan

    # ---------- GETTER ----------
    def get_kode(self):
        return self.__kode

    def get_anggota(self):
        return self.__anggota

    def get_buku(self):
        return self.__buku

    def get_tgl_pinjam(self):
        return self.__tgl_pinjam

    def get_tgl_kembali(self):
        return self.__tgl_kembali

    # ---------- METHOD TAMBAHAN ----------
    def get_jatuh_tempo(self):
        """Tanggal batas pengembalian."""
        return self.__tgl_pinjam + timedelta(days=Peminjaman.LAMA_PINJAM)

    def is_selesai(self):
        return self.__tgl_kembali is not None

    def hitung_denda(self):
        """Denda = hari terlambat x tarif per hari."""
        acuan = self.__tgl_kembali or date.today()
        terlambat = (acuan - self.get_jatuh_tempo()).days
        return max(0, terlambat) * Peminjaman.DENDA_PER_HARI

    def selesaikan(self):
        """Proses pengembalian: update status buku & anggota."""
        if self.is_selesai():
            return False
        self.__tgl_kembali = date.today()
        self.__buku.kembalikan()
        self.__anggota.kurangi_pinjam()
        return True

    def cek_status(self):
        """Status peminjaman dalam bentuk teks."""
        if self.is_selesai():
            return f"Sudah dikembalikan pada {self.__tgl_kembali}"
        denda = self.hitung_denda()
        if denda > 0:
            return f"TERLAMBAT! Denda saat ini Rp{denda}"
        return f"Masih dipinjam, jatuh tempo {self.get_jatuh_tempo()}"

    def tampilkan_info(self):
        return (f"[{self.__kode}] {self.__anggota.get_nama()} meminjam "
                f"'{self.__buku.get_judul()}' ({self.__tgl_pinjam}) -> {self.cek_status()}")