# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 16:19:09 2024
@author: Zulfadli
"""
"""
class praktikan:
    def __init__(self, nama, nim, fakultas, hobi):
        self.nama = nama
        self.nim = nim
        self.fakultas = fakultas
        self.hobi = hobi

    def Hasil(self):
        return f"Nama saya adalah {self.nama}, NIM saya {self.nim}, saya dari fakultas {self.fakultas}, dan hobi saya adalah {self.hobi}."

praktikan1 = praktikan("Zulfadli Daniswara", "064002300025", "Teknik Informatika", "Main PUBG")  

print("----Program menampilkan identitas---")
print(praktikan1.Hasil())
"""
class Persegi:

    def __init__(self):
          #Identitas
        self.nama  = "Zulfadli Daniswara"
        self.nim   = "064002300025"
        self.studi = "Teknik Informatika"
        self.panjang = int(input("Masukkan angka : "))
        self.lebar = int(input("Masukkan angka : "))

    def segitiga(self):
        return self.panjang * self.lebar  #rumus persegi 
    
    def tampilan(self):  #tampilan user 
        print(self.nama , self.nim , self.studi)  
        print("---->PROGRAM MENGHITUNG PERSEGI PANJANG<----")
        print("Persegi panjang dengan panjang", self.panjang, "cm lebar", self.lebar, "memiliki luas sekitar", self.segitiga(), "cm^2")

def main():  #Pemanggilan fungsi 
    obj_persegi = Persegi()
    obj_persegi.tampilan()

if __name__ == "__main__":
    main()