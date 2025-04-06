
# Soal 1: Variables dan Operasi Matematika
# 1. Menghitung luas lingkaran
import math
jari_jari_lingkaran = float(input("Masukkan jari-jari lingkaran: "))
luas_lingkaran = math.pi * jari_jari_lingkaran ** 2 # Rumus luas lingkaran = pi*r^2
print(f"Luas lingkaran dengan jari-jari {jari_jari_lingkaran} adalah {luas_lingkaran:.2f}")

# 2. Menghitung jumlah total, rata-rata, maksimum, dan minimum dari tiga angka
angka_pertama = float(input("Masukkan angka pertama: "))
angka_kedua = float(input("Masukkan angka kedua: "))
angka_ketiga = float(input("Masukkan angka ketiga: "))
jumlah_total_tiga_angka = angka_pertama + angka_kedua + angka_ketiga
rata_rata_tiga_angka = jumlah_total_tiga_angka / 3
angka_maksimum = max(angka_pertama, angka_kedua, angka_ketiga)
angka_minimum = min(angka_pertama, angka_kedua, angka_ketiga)
print(f"Jumlah total: {jumlah_total_tiga_angka}, Rata-rata: {rata_rata_tiga_angka:.2f}, Maksimum: {angka_maksimum}, Minimum: {angka_minimum}")
# Penjelasan :.2f dalam String Formatting
# . (titik) → Menunjukkan bahwa kita ingin mengatur jumlah angka desimal.
# 2 → Menentukan jumlah angka setelah desimal (dalam hal ini, dua angka).
# f → Singkatan dari float, yang berarti angka ditampilkan dalam format floating-point (bilangan desimal).

# 3. Konversi jumlah hari ke tahun, bulan, dan hari
jumlah_hari = int(input("Masukkan jumlah hari: "))
jumlah_tahun = jumlah_hari // 365
jumlah_bulan_sisa = (jumlah_hari % 365) // 30
sisa_hari = (jumlah_hari % 365) % 30
print(f"{jumlah_hari} hari = {jumlah_tahun} tahun, {jumlah_bulan_sisa} bulan, {sisa_hari} hari")

# -----------------------------------------------------------------------------------------------------------------------------------------
# Soal 2: Casting (Perubahan Tipe Data)
# 1. Mengonversi string ke integer dan melakukan penjumlahan
angka_dalam_string = input("Masukkan angka dalam bentuk string: ")
angka_dalam_integer = int(angka_dalam_string)
hasil_penjumlahan_dengan_angka_tetap = angka_dalam_integer + 10
print(f"Hasil penjumlahan {angka_dalam_integer} dengan 10 adalah {hasil_penjumlahan_dengan_angka_tetap}")

# 2. Mengonversi desimal ke bilangan bulat dan pecahan
# Jawaban soal 2 no 2 versi 1 (Versi Terstruktur)
angka_desimal = float(input("Masukkan angka desimal: "))
bilangan_bulat = int(angka_desimal)
bilangan_pecahan = float(angka_desimal)
print(f"Bilangan bulat: {bilangan_bulat}, Bilangan pecahan: {bilangan_pecahan}")

# Jawaban soal 2 no 2 versi 2 (Versi singkat & langsung)
angka_desimal = float(input("Masukkan angka desimal: "))
print(f"Bilangan bulat: {int(angka_desimal)}, Bilangan pecahan: {float(angka_desimal)}")

# -----------------------------------------------------------------------------------------------------------------------------------------
# Soal 3: Conditional Statement
# 1. Menentukan kategori usia
usia_pengguna = int(input("Masukkan usia Anda: "))
if usia_pengguna < 13:
    kategori_usia = "Anak-anak"
elif 13 <= usia_pengguna <= 19:
    kategori_usia = "Remaja"
elif 20 <= usia_pengguna <= 59:
    kategori_usia = "Dewasa"
else:
    kategori_usia = "Lansia"
print(f"Kategori usia Anda: {kategori_usia}")

# 2. Mengecek angka positif/negatif dan genap/ganjil
input_angka = int(input("Masukkan sebuah angka: "))
positif_negatif = "Positif" if input_angka >= 0 else "Negatif"
ganjil_genap = "Genap" if input_angka % 2 == 0 else "Ganjil"
print(f"Angka {input_angka} adalah {positif_negatif} dan {ganjil_genap}")


# -----------------------------------------------------------------------------------------------------------------------------------------
# Soal 4: While dan For Loop
# 1. While loop untuk jumlah total
jumlah_total_angka_yang_diinput = 0
while True:
    angka_yang_diinput = int(input("Masukkan angka (negatif untuk berhenti): "))
    if angka_yang_diinput < 0:
        break
    jumlah_total_angka_yang_diinput += angka_yang_diinput
print(f"Jumlah total angka yang dimasukkan: {jumlah_total_angka_yang_diinput}")

# Penjelasan:
# - Loop akan terus berjalan hingga pengguna memasukkan angka negatif.

# 2. For loop untuk menghitung total dan rata-rata dalam list
list_angka = [5, 10, 15, 20, 25]
total_list_angka = sum(list_angka)
rata_rata_list_angka = total_list_angka / len(list_angka)
print(f"Total angka dalam list: {total_list_angka}, Rata-rata: {rata_rata_list_angka}")


# -----------------------------------------------------------------------------------------------------------------------------------------
# Soal 5: Collection Data Types
# 1. List untuk nama teman
list_nama_teman = []
for i in range(5):
    nama_teman = input(f"Masukkan nama teman ke-{i + 1}: ")
    list_nama_teman.append(nama_teman)
print("Nama teman yang dimasukkan:")
for nama in list_nama_teman:
    print(nama)
# Penjelasan: Input dimasukkan ke dalam list dengan metode `append` dan diiterasi menggunakan for loop.

# 2. Tuple untuk nama dan tanggal lahir
nama_saya = "Liswatun Naimah"
tanggal_lahir_saya = "5 Oktober 2001"
data_diri = (nama_saya, tanggal_lahir_saya)
print(f"Nama saya {data_diri[0]}, lahir pada {data_diri[1]}.")

# 3. Dictionary untuk nama dan umur
data_nama_dan_umur = {}
for i in range(5):
    nama_orang = input(f"Masukkan nama orang ke-{i + 1}: ")
    umur_orang = int(input(f"Masukkan umur {nama_orang}: "))
    data_nama_dan_umur[nama_orang] = umur_orang
print("Data nama dan umur yang diinput:")
for nama, umur in data_nama_dan_umur.items():
    print(f"Nama: {nama}, Umur: {umur}")

# 4. Set untuk union dan intersection
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
union_set = set1 | set2
intersection_set = set1 & set2
subset_check = set1.issubset(set2)
print(f"Union: {union_set}")
print(f"Intersection: {intersection_set}")
print(f"Apakah set1 subset dari set2? {subset_check}")

# -----------------------------------------------------------------------------------------------------------------------------------------
# Soal 6: All the Concept
# Program kasir untuk mencatat daftar belanjaan pelanggan, menghitung total harga, dan memberikan diskon otomatis jika pelanggan membeli dalam jumlah tertentu. 
jumlah_jenis_barang = int(input("Masukkan jumlah jenis barang: "))
daftar_belanjaan = []

total_harga_belanjaan = 0
for i in range(jumlah_jenis_barang):
    nama_barang = input(f"Masukkan nama barang ke-{i + 1}: ")
    harga_barang_per_unit = float(input(f"Masukkan harga per unit {nama_barang}: "))
    jumlah_barang_yang_dibeli = int(input(f"Masukkan jumlah pembelian untuk {nama_barang}: "))
    subtotal_barang = harga_barang_per_unit * jumlah_barang_yang_dibeli
    daftar_belanjaan.append((nama_barang, harga_barang_per_unit, jumlah_barang_yang_dibeli, subtotal_barang))
    total_harga_belanjaan += subtotal_barang

if total_harga_belanjaan > 200000:
    persentase_diskon = 0.2
elif total_harga_belanjaan > 100000:
    persentase_diskon = 0.1
else:
    persentase_diskon = 0

total_diskon = total_harga_belanjaan * persentase_diskon
total_harga_setelah_diskon = total_harga_belanjaan - total_diskon

print("\nDaftar Belanjaan Pelanggan:")
for barang in daftar_belanjaan:
    print(f"Nama Barang: {barang[0]}, Harga: {barang[1]}, Jumlah: {barang[2]}, Subtotal: {barang[3]}")
print(f"Total belanja sebelum diskon: {total_harga_belanjaan}")
print(f"Diskon: {total_diskon}")
print(f"Total belanja setelah diskon: {total_harga_setelah_diskon}")

jumlah_uang_pelanggan = float(input("Masukkan jumlah uang pelanggan: "))
while jumlah_uang_pelanggan < total_harga_setelah_diskon:
    print("Uang tidak cukup, silakan masukkan jumlah yang cukup.")
    jumlah_uang_pelanggan = float(input("Masukkan jumlah uang pelanggan: "))
jumlah_kembalian = jumlah_uang_pelanggan - total_harga_setelah_diskon
print(f"Kembalian: {jumlah_kembalian}")

