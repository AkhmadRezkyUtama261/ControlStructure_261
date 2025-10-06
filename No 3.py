Nilai = int(input("Masukkan Nilai: "))

a, b = 0, 1

print("Deret Fibonacci sampai", Nilai, ":")

while a <= Nilai:
    print(a, end=" ")
    a, b = b, a + b
