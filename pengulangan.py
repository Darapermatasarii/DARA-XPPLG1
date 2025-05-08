# While Loop: Minta nama hingga input "Dara"
nama = ""
while nama != "Dara":
    nama = input("Masukkan nama: ")

print("Hai Dara, selamat datang!")

# For Loop: Menampilkan "Halo Dara!" sebanyak 3 kali
for i in range(3):
    print("Halo Dara!")

# Nested Loop: Menampilkan pola segitiga dengan nama "Dara"
for i in range(1, 5):  # Baris
    for j in range(i):  # Kolom per baris
        print("Dara", end=" ")
    print()  # Pindah baris setelah setiap baris selesai
