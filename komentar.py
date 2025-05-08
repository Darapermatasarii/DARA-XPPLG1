# Program sederhana untuk menyapa pengguna
# Ditulis oleh: [dara]
# Materi: Penggunaan komentar dalam Python

# Menyimpan nama pengguna
nama = "Dara"  # Variabel untuk menyimpan nama

# Fungsi untuk menyapa pengguna
def sapa(pengguna):
    """
    Fungsi ini menyapa pengguna dengan kata 'Halo'.
    Parameter:
    pengguna (str): nama orang yang ingin disapa
    """
    # Menampilkan sapaan ke layar
    print("Halo, " + pengguna + "!")

# Memanggil fungsi sapa
sapa(nama)

# Komentar juga bisa dipakai untuk menonaktifkan kode sementara
# print("Ini tidak akan tampil karena dikomentari")
