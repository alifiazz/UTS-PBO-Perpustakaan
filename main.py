# ============================================================
# File   : main.py
# Isi    : Program utama - Aplikasi Manajemen Perpustakaan (CLI)
# Jalankan: python main.py
# ============================================================
from buku import Buku, BukuFiksi, BukuNonFiksi
from anggota import Anggota
from peminjaman import Peminjaman

# Penyimpanan data sementara (in-memory) berupa list of object
daftar_buku = []
daftar_anggota = []
daftar_pinjam = []


# ---------------- FUNGSI BANTU ----------------
def input_angka(pesan):
    """Minta input angka; ulangi sampai valid."""
    while True:
        try:
            return int(input(pesan))
        except ValueError:
            print("  ! Harap masukkan angka.")


def cari_buku(kode):
    for b in daftar_buku:
        if b.get_kode().lower() == kode.lower():
            return b
    return None


def cari_anggota(id_anggota):
    for a in daftar_anggota:
        if a.get_id().lower() == id_anggota.lower():
            return a
    return None


def cari_pinjam(kode):
    for p in daftar_pinjam:
        if p.get_kode().lower() == kode.lower():
            return p
    return None


def isi_data_awal():
    """Data contoh supaya program langsung bisa dicoba."""
    daftar_buku.append(BukuFiksi("B001", "Laskar Pelangi", "Andrea Hirata", 2005, "Novel"))
    daftar_buku.append(BukuFiksi("B002", "Bumi", "Tere Liye", 2014, "Fantasi"))
    daftar_buku.append(BukuNonFiksi("B003", "Algoritma dan Pemrograman", "Rinaldi Munir", 2016, "Informatika"))
    daftar_buku.append(BukuNonFiksi("B004", "Atomic Habits", "James Clear", 2018, "Pengembangan Diri"))
    daftar_anggota.append(Anggota("A001", "Budi Santoso", "081234567890"))
    daftar_anggota.append(Anggota("A002", "Siti Aminah", "085678901234"))


# ---------------- 1. TAMBAH DATA ----------------
def tambah_buku():
    print("\n-- Tambah Buku --")
    kode = input("Kode buku      : ").strip()
    if cari_buku(kode):
        print("  ! Kode sudah dipakai.")
        return
    judul = input("Judul          : ")
    penulis = input("Penulis        : ")
    tahun = input_angka("Tahun terbit   : ")
    jenis = input("Jenis (1=Fiksi, 2=Non-Fiksi): ")
    # Polimorfisme: list menyimpan objek dari subclass berbeda
    if jenis == "1":
        genre = input("Genre          : ")
        daftar_buku.append(BukuFiksi(kode, judul, penulis, tahun, genre))
    elif jenis == "2":
        bidang = input("Bidang ilmu    : ")
        daftar_buku.append(BukuNonFiksi(kode, judul, penulis, tahun, bidang))
    else:
        print("  ! Jenis tidak valid.")
        return
    print("  Buku berhasil ditambahkan.")


def tambah_anggota():
    print("\n-- Tambah Anggota --")
    id_a = input("ID anggota : ").strip()
    if cari_anggota(id_a):
        print("  ! ID sudah dipakai.")
        return
    nama = input("Nama       : ")
    kontak = input("Kontak     : ")
    daftar_anggota.append(Anggota(id_a, nama, kontak))
    print("  Anggota berhasil ditambahkan.")


def tambah_peminjaman():
    print("\n-- Tambah Peminjaman --")
    anggota = cari_anggota(input("ID anggota : ").strip())
    if anggota is None:
        print("  ! Anggota tidak ditemukan.")
        return
    if not anggota.bisa_meminjam():
        print("  ! Anggota sudah mencapai batas peminjaman.")
        return
    buku = cari_buku(input("Kode buku  : ").strip())
    if buku is None:
        print("  ! Buku tidak ditemukan.")
        return
    if not buku.pinjam():  # pinjam() mengembalikan False jika sedang dipinjam
        print("  ! Buku sedang dipinjam.")
        return
    anggota.tambah_pinjam()
    kode = f"P{len(daftar_pinjam) + 1:03d}"
    daftar_pinjam.append(Peminjaman(kode, anggota, buku))
    print(f"  Peminjaman {kode} berhasil dicatat. Jatuh tempo {daftar_pinjam[-1].get_jatuh_tempo()}.")


def menu_tambah():
    print("\n1. Tambah Buku\n2. Tambah Anggota\n3. Tambah Peminjaman")
    pilih = input("Pilih: ")
    if pilih == "1":
        tambah_buku()
    elif pilih == "2":
        tambah_anggota()
    elif pilih == "3":
        tambah_peminjaman()
    else:
        print("  ! Pilihan tidak valid.")


# ---------------- 2. TAMPILKAN DATA ----------------
def tampilkan_data():
    print("\n1. Data Buku\n2. Data Anggota\n3. Data Peminjaman")
    pilih = input("Pilih: ")
    if pilih == "1":
        print("\n== DAFTAR BUKU ==")
        for b in daftar_buku:
            print(" ", b.tampilkan_info())
    elif pilih == "2":
        print("\n== DAFTAR ANGGOTA ==")
        for a in daftar_anggota:
            print(" ", a.tampilkan_info())
    elif pilih == "3":
        print("\n== DAFTAR PEMINJAMAN ==")
        if not daftar_pinjam:
            print("  (belum ada peminjaman)")
        for p in daftar_pinjam:
            print(" ", p.tampilkan_info())
    else:
        print("  ! Pilihan tidak valid.")


# ---------------- 3. CARI DATA ----------------
def cari_data():
    print("\n-- Cari Buku (berdasarkan judul/penulis) --")
    kata = input("Kata kunci: ").lower()
    hasil = [b for b in daftar_buku
             if kata in b.get_judul().lower() or kata in b.get_penulis().lower()]
    if not hasil:
        print("  Tidak ada buku yang cocok.")
    for b in hasil:
        print(" ", b.tampilkan_info())
        # hanya subclass yang punya rekomendasi_pembaca()
        if hasattr(b, "rekomendasi_pembaca"):
            print("    ->", b.rekomendasi_pembaca())


# ---------------- 4. UBAH DATA ----------------
def ubah_data():
    print("\n1. Ubah Data Buku\n2. Ubah Data Anggota\n3. Kembalikan Buku")
    pilih = input("Pilih: ")
    if pilih == "1":
        b = cari_buku(input("Kode buku: ").strip())
        if b is None:
            print("  ! Buku tidak ditemukan.")
            return
        # Kosongkan input jika tidak ingin mengubah field tersebut
        judul = input(f"Judul baru [{b.get_judul()}]: ")
        penulis = input(f"Penulis baru [{b.get_penulis()}]: ")
        tahun = input(f"Tahun baru [{b.get_tahun()}]: ")
        if judul:
            b.set_judul(judul)
        if penulis:
            b.set_penulis(penulis)
        if tahun.isdigit():
            b.set_tahun(int(tahun))
        print("  Data buku diperbarui.")
    elif pilih == "2":
        a = cari_anggota(input("ID anggota: ").strip())
        if a is None:
            print("  ! Anggota tidak ditemukan.")
            return
        nama = input(f"Nama baru [{a.get_nama()}]: ")
        kontak = input(f"Kontak baru [{a.get_kontak()}]: ")
        if nama:
            a.set_nama(nama)
        if kontak:
            a.set_kontak(kontak)
        print("  Data anggota diperbarui.")
    elif pilih == "3":
        p = cari_pinjam(input("Kode peminjaman: ").strip())
        if p is None:
            print("  ! Peminjaman tidak ditemukan.")
        elif p.selesaikan():
            print(f"  Buku dikembalikan. Denda: Rp{p.hitung_denda()}")
        else:
            print("  ! Peminjaman ini sudah selesai.")
    else:
        print("  ! Pilihan tidak valid.")


# ---------------- 5. CEK STATUS ----------------
def cek_status():
    print("\n1. Cek Status Buku\n2. Cek Status Peminjaman")
    pilih = input("Pilih: ")
    if pilih == "1":
        b = cari_buku(input("Kode buku: ").strip())
        if b is None:
            print("  ! Buku tidak ditemukan.")
        else:
            print("  Status:", "Tersedia" if b.is_tersedia() else "Sedang dipinjam")
    elif pilih == "2":
        p = cari_pinjam(input("Kode peminjaman: ").strip())
        if p is None:
            print("  ! Peminjaman tidak ditemukan.")
        else:
            print(" ", p.tampilkan_info())
    else:
        print("  ! Pilihan tidak valid.")


# ---------------- PROGRAM UTAMA ----------------
def main():
    isi_data_awal()
    while True:
        print("\n===== APLIKASI MANAJEMEN PERPUSTAKAAN =====")
        print("1. Tambah Data")
        print("2. Tampilkan Data")
        print("3. Cari Data")
        print("4. Ubah Data")
        print("5. Cek Status Data")
        print("0. Keluar")
        pilih = input("Pilih menu: ").strip()
        if pilih == "1":
            menu_tambah()
        elif pilih == "2":
            tampilkan_data()
        elif pilih == "3":
            cari_data()
        elif pilih == "4":
            ubah_data()
        elif pilih == "5":
            cek_status()
        elif pilih == "0":
            print("Terima kasih. Program selesai.")
            break
        else:
            print("  ! Menu tidak valid.")


if __name__ == "__main__":
    main()