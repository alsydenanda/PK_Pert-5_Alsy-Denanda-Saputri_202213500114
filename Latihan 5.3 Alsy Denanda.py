#Latihan 5.38

def konversi_nilai_ke_poin(nilai):
    if nilai == 'A':
        return 4.0
    elif nilai == 'B':
        return 3.0  
    elif nilai == 'C':
        return 2.0
    elif nilai == 'D':
        return 1.0 
    else:
        return 0.0
    
def hitung_IPS():
    total_poin = 0
    jumlah_mata_kuliah = int(input("Masukkan jumlah mata kuliah: "))

    for i in range(jumlah_mata_kuliah):
        nilai = input(f"Masukkan nilai (A,B, C, D) untuk mata kuliah ke-{i+1}: ").upper()
        poin = konversi_nilai_ke_poin(nilai)
        total_poin += poin

    IPS = total_poin / jumlah_mata_kuliah
    return IPS

IPS = hitung_IPS()
print(f"IPS yang didapatkan adalah: {IPS:.2f}")  