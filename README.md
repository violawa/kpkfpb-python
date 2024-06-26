# FPB dan KPK Calculator

Program ini adalah kalkulator sederhana untuk menghitung Faktor Persekutuan Terbesar (FPB) dan Kelipatan Persekutuan Terkecil (KPK) dari dua bilangan bulat. Program ini meminta pengguna untuk memilih operasi yang diinginkan dan memasukkan dua bilangan bulat, kemudian menghitung dan menampilkan hasilnya.

## Fungsi

### `hitung_fpb(a, b)`

Fungsi ini digunakan untuk menghitung FPB dari dua bilangan bulat `a` dan `b` menggunakan algoritma Euclid.

**Parameter:**
- `a` (int): Bilangan bulat pertama
- `b` (int): Bilangan bulat kedua

**Mengembalikan:**
- int: FPB dari `a` dan `b`

**Contoh:**
```python
hitung_fpb(12, 15) # Output: 3
```

### `hitung_kpk(a, b)`

Fungsi ini digunakan untuk menghitung KPK dari dua bilangan bulat `a` dan `b`.

**Parameter:**
- `a` (int): Bilangan bulat pertama
- `b` (int): Bilangan bulat kedua

**Mengembalikan:**
- int: KPK dari `a` dan `b`

**Contoh:**
```python
hitung_kpk(12, 15) # Output: 60
```

### `main()`

Fungsi ini adalah fungsi utama yang mengatur alur program. Fungsi ini meminta pengguna untuk memilih operasi (FPB atau KPK) dan memasukkan dua bilangan bulat. Berdasarkan pilihan pengguna, fungsi ini akan memanggil `hitung_fpb` atau `hitung_kpk` dan menampilkan hasilnya.

## Cara Menggunakan
1. Jalankan program.
2. Pilih operasi yang ingin dilakukan:
   - Ketik `1` untuk menghitung FPB.
   - Ketik `2` untuk menghitung KPK.
3. Masukkan dua bilangan bulat.
4. Hasil akan ditampilkan di layar.

## Contoh Penggunaan

```
Pilih operasi yang ingin Anda lakukan:
1. Hitung FPB
2. Hitung KPK
Masukkan pilihan (1 atau 2): 1
Masukkan bilangan pertama: 12
Masukkan bilangan kedua: 15
FPB dari 12 dan 15 adalah 3.
```

## Catatan

- Jika pengguna memasukkan pilihan yang tidak valid, program akan menampilkan pesan kesalahan dan keluar.
- Jika pengguna memasukkan nilai non-angka, program akan menampilkan pesan kesalahan dan keluar.

## Menjalankan Program

Untuk menjalankan program, pastikan Anda memiliki Python terinstal di komputer Anda. Simpan kode program di file dengan ekstensi `.py` dan jalankan menggunakan perintah berikut di terminal atau command prompt:

```bash
python file.py
```
