# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 11:38:03 2024

@author: Zulfadli
"""
"""
class Segitiga:
    
    def hitung_luas_segitiga(alas, tinggi):
        return 0.5 * alas * tinggi 

    
    def hitung_keliling_segitiga(sisi_a, sisi_b, sisi_c):
        return sisi_a + sisi_b + sisi_c 

def main():
    print("Program Menghitung Luas dan Keliling Segitiga")
    print("=============================================")
    pilihan = input("Pilih mode:\n1. Hitung Luas\n2. Hitung Keliling\nPilihan: ")

    if pilihan == '1': 
        alas = float(input("Masukkan panjang alas segitiga: "))
        tinggi = float(input("Masukkan tinggi segitiga: "))
        luas = Segitiga.hitung_luas_segitiga(alas, tinggi)
        print("Luas segitiga adalah:", luas)
    elif pilihan == '2':
        sisi_a = float(input("Masukkan panjang sisi A segitiga: "))
        sisi_b = float(input("Masukkan panjang sisi B segitiga: "))
        sisi_c = float(input("Masukkan panjang sisi C segitiga: "))
        keliling = Segitiga.hitung_keliling_segitiga(sisi_a, sisi_b, sisi_c)
        print("Keliling segitiga adalah:", keliling)
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()
"""
class AngkaTanpaNIM:
    def __init__(self):
        self.nim = ""
    
    def input_nim(self):
        self.nim = input("Masukkan NIM Anda: ")

    def generate_numbers(self):
        last_two_digits = self.nim[-2:]
        print("Deret angka dari 1 sampai 50 (kecuali 2 digit terakhir dari NIM):")

        for i in range(1, 51):
            if str(i) == last_two_digits:
                continue
            print(i, end=" ")

# Membuat instance dari kelas AngkaTanpaNIM
angka_tanpa_nim = AngkaTanpaNIM()

# Meminta input NIM dari pengguna
angka_tanpa_nim.input_nim()

# Menampilkan deret angka tanpa 2 digit terakhir NIM
angka_tanpa_nim.generate_numbers()