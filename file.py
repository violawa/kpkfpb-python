def hitung_fpb(a, b):
    while b:
        a, b = b, a % b
    return a


def hitung_kpk(a, b):
    return a * b // hitung_fpb(a, b)


def main():
    print("Pilih operasi yang ingin Anda lakukan:")
    print("1. Hitung FPB")
    print("2. Hitung KPK")

    pilihan = input("Masukkan pilihan (1 atau 2): ")

    if pilihan not in ("1", "2"):
        print("Pilihan tidak valid. Silakan pilih 1 atau 2.")
        return

    try:
        a = int(input("Masukkan bilangan pertama: "))
        b = int(input("Masukkan bilangan kedua: "))
    except ValueError:
        print("Masukkan nilai yang valid!")
        return

    if pilihan == "1":
        hasil = hitung_fpb(a, b)
        print(f"FPB dari {a} dan {b} adalah {hasil}.")
    elif pilihan == "2":
        hasil = hitung_kpk(a, b)
        print(f"KPK dari {a} dan {b} adalah {hasil}.")


if __name__ == "__main__":
    main()
