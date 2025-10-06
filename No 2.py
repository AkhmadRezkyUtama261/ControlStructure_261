a = int(input("Masukkan Angka pertama: "))
b = int(input("Masukkan Angka kedua: "))
c = int(input("Masukkan Angka ketiga: "))

if a > b and a > c:
    print("Angka terbesar adalah:", a)
elif b > a and b > c:
    print("Angka terbesar adalah:", b)
else:
    print("Angka terbesar adalah:", c)
