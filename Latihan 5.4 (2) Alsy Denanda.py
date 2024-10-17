#Menghitung pemangkatan dua bilangan tanpa operator **

def pemangkatan(a, b):
    hasil = 1
    while b > 0:
        if b % 2 == 1:
            hasil *= a
        a *= a
        b //= 2
    return hasil

a = int(input("Masukkan bilangan dasar: "))
b = int(input("Masukkan bilangan pangkat: "))
print(f"Hasil pemangkatan {a} ^ {b} = {pemangkatan(a, b)}")

