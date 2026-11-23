# Aplikasi Manajemen Perpustakaan (CLI)

Tugas UTS Pemrograman Berorientasi Objek (PBO) - Python.

Aplikasi berbasis terminal untuk mengelola data buku, anggota,
dan peminjaman di perpustakaan.

## Fitur
- Tambah data (buku, anggota, peminjaman)
- Tampilkan data
- Cari buku berdasarkan judul atau penulis
- Ubah data dan proses pengembalian buku
- Cek status buku dan peminjaman
- Denda otomatis (Rp1.000/hari setelah 7 hari)

## Konsep OOP yang Diterapkan
- Class dan Object
- Atribut dan Method
- Constructor berparameter
- Encapsulation (atribut private + getter/setter)
- Inheritance (Buku -> BukuFiksi, BukuNonFiksi)
- Relasi antar class (Peminjaman memiliki 1 Anggota dan 1 Buku)

## Struktur File
| File | Isi |
|---|---|
| main.py | Program utama dan menu |
| buku.py | Class Buku, BukuFiksi, BukuNonFiksi |
| anggota.py | Class Anggota |
| peminjaman.py | Class Peminjaman |

## Cara Menjalankan
1. Pastikan Python 3 sudah terinstall.
2. Simpan semua file dalam satu folder.
3. Jalankan: `py main.py` (atau `python main.py`)

## Pembuat
- Nama : Alifia Faza Khoirunnisa
- NIM : 25552011279
- Kelas : TIF RP 25B
