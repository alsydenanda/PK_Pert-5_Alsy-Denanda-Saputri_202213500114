#Menghitung perkalian dua bilangan tanpa operator *

def perkalian(a, b):
    hasil = 0
    for _ in range(abs(b)):
        hasil += a
    if b < 0:
        hasil = -hasil
    return hasil

a = int(input("Masukkan bilangan pertama untuk perkalian: "))
b = int(input("Masukkan bilangan kedua untuk perkalian: "))
print(f"Hasil perkalian {a} x {b} = {perkalian(a, b)}")

