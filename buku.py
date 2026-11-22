# ============================================================
# File   : buku.py
# Isi    : Superclass Buku, serta subclass BukuFiksi & BukuNonFiksi
# ============================================================


class Buku:
    """SUPERCLASS: mewakili data buku secara umum."""

    # Constructor berparameter: dipanggil saat objek Buku dibuat
    def __init__(self, kode, judul, penulis, tahun):
        # Atribut private (diawali __) -> tidak bisa diakses langsung dari luar class
        self.__kode = kode
        self.__judul = judul
        self.__penulis = penulis
        self.__tahun = tahun
        self.__tersedia = True  # status ketersediaan buku

    # ---------- GETTER (akses baca atribut private) ----------
    def get_kode(self):
        return self.__kode

    def get_judul(self):
        return self.__judul

    def get_penulis(self):
        return self.__penulis

    def get_tahun(self):
        return self.__tahun

    def is_tersedia(self):
        return self.__tersedia

    # ---------- SETTER (ubah atribut private dengan validasi) ----------
    def set_judul(self, judul):
        if judul.strip():  # judul tidak boleh kosong
            self.__judul = judul

    def set_penulis(self, penulis):
        if penulis.strip():
            self.__penulis = penulis

    def set_tahun(self, tahun):
        if tahun > 0:  # tahun harus positif
            self.__tahun = tahun

    # ---------- METHOD TAMBAHAN ----------
    def pinjam(self):
        """Tandai buku dipinjam. Return False jika sedang dipinjam."""
        if not self.__tersedia:
            return False
        self.__tersedia = False
        return True

    def kembalikan(self):
        """Tandai buku sudah dikembalikan."""
        self.__tersedia = True

    def get_kategori(self):
        """Kategori buku (akan di-override oleh subclass)."""
        return "Umum"

    def tampilkan_info(self):
        """Mengembalikan informasi buku dalam bentuk teks."""
        status = "Tersedia" if self.__tersedia else "Dipinjam"
        return (f"[{self.__kode}] {self.__judul} | {self.__penulis} | "
                f"{self.__tahun} | {self.get_kategori()} | {status}")


class BukuFiksi(Buku):
    """SUBCLASS: buku fiksi (novel, cerpen, dsb) - mewarisi Buku."""

    def __init__(self, kode, judul, penulis, tahun, genre):
        super().__init__(kode, judul, penulis, tahun)  # panggil constructor superclass
        self.__genre = genre  # atribut private milik subclass

    def get_genre(self):
        return self.__genre

    def set_genre(self, genre):
        if genre.strip():
            self.__genre = genre

    # Method overriding: mengubah perilaku method superclass
    def get_kategori(self):
        return f"Fiksi ({self.__genre})"

    def rekomendasi_pembaca(self):
        """Method tambahan khusus buku fiksi."""
        return f"Cocok untuk pecinta cerita bergenre {self.__genre}."


class BukuNonFiksi(Buku):
    """SUBCLASS: buku non-fiksi (ilmiah, biografi, dsb) - mewarisi Buku."""

    def __init__(self, kode, judul, penulis, tahun, bidang):
        super().__init__(kode, judul, penulis, tahun)
        self.__bidang = bidang

    def get_bidang(self):
        return self.__bidang

    def set_bidang(self, bidang):
        if bidang.strip():
            self.__bidang = bidang

    # Method overriding
    def get_kategori(self):
        return f"Non-Fiksi ({self.__bidang})"

    def rekomendasi_pembaca(self):
        """Method tambahan khusus buku non-fiksi."""
        return f"Cocok untuk yang ingin belajar tentang {self.__bidang}."