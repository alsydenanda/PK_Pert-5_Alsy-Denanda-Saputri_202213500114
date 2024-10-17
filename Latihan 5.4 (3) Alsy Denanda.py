#Memeriksa apakah suatu bilangan adalah prima?

def cek_prima(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

n = int(input("Masukkan bilangan untuk dicek apakah prima: "))
if cek_prima(n):
    print(f"{n} adalah bilangan prima.")
else:
    print(f"{n} bukan bilangan prima.")
    