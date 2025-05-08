# 1. Integer (int): Bilangan bulat
umur = 15
saldo = -1000
print(f"Integer: {umur}, Saldo: {saldo}, Tipe: {type(umur)}")

# 2. Float: Bilangan desimal
tinggi = 1.75
berat = 65.5
print(f"Float: {tinggi}, Berat: {berat}, Tipe: {type(tinggi)}")

# 3. Complex: Bilangan kompleks
bil_kompleks = 3 + 4j
print(f"Complex: {bil_kompleks}, Riil: {bil_kompleks.real}, Imajiner: {bil_kompleks.imag}")

# 4. Boolean (bool): Nilai benar atau salah
is_student = True
is_employed = False
print(f"Boolean (Mahasiswa): {is_student}, Bekerja: {is_employed}, Tipe: {type(is_student)}")

# 5. String (str): Teks atau karakter
nama = "Dara"
alamat = 'Karawang'
print(f"String: {nama}, Alamat: {alamat}, Tipe: {type(nama)}")

# 6. List: Daftar yang dapat diubah
buah = ["apel", "mangga", "jeruk"]
buah.append("pisang")
print(f"List: {buah}, Tipe: {type(buah)}")

# 7. Tuple: Daftar tetap (tidak dapat diubah)
koordinat = (10, 20, 30)
print(f"Tuple: {koordinat}, Tipe: {type(koordinat)}")

# 8. Set: Kumpulan elemen unik
angka_unik = {1, 2, 3, 3, 4}
angka_unik.add(5)
print(f"Set: {angka_unik}, Tipe: {type(angka_unik)}")

# 9. Dictionary (dict): Pasangan kunci-nilai
mahasiswa = {
    "nama": "Budi",
    "usia": 16,
    "jurusan": "Informatika"
}
mahasiswa["usia"] = 14 # Mengubah nilai
print(f"Dictionary: {mahasiswa}, Tipe: {type(mahasiswa)}")

# Contoh Operasi pada Tipe Data
print("\nOperasi pada Tipe Data:")
print(f"Penjumlahan int: {umur + 5}")
print(f"Penggabungan string: {nama + ' Permatasari'}")
print(f"Negasi boolean: {not is_student}")
print(f"Menambah elemen list: {buah + ['anggur']}")
print(f"Akses elemen tuple: {koordinat[1]}")
print(f"Angka unik setelah penambahan: {angka_unik}")

# Mengakses dan memodifikasi dictionary
print(f"Nama Mahasiswa: {mahasiswa['nama']}")
mahasiswa["alamat"] = "Karawang"
print(f"Data Mahasiswa (Updated): {mahasiswa}")
