def kalkulator():
    print("+====================================+")
    print("|      KALKULATOR DARA SEDERHANA     |")
    print("+====================================+")
    print("Masukkan nilai a dan b")
    try:
        a = 187
        b = 50
    except ValueError:
        print("Input tidak valid! Masukkan angka.")
        return

    print("Masukkan kode (+, -, *, /):")
    op = input("kode: ")

    if op == "+":
        hasil = a + b
    elif op == "-":
        hasil = a - b
    elif op == "*":
        hasil = a * b
    elif op == "/":
        if b != 0:
            hasil = a / b
        else:
            print("Error: Pembagian dengan nol!")
            return
    else:
        print("kode tidak valid!")
        return

    print("+---------------------------+")
    print(f"| Hasil: {a} {op} {b} = {hasil}")
    print("+---------------------------+")

kalkulator()
