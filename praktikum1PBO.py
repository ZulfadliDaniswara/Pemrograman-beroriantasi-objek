# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 09:47:38 2024

@author: Zulfadli
"""
"""
class Penjumlahan:
    def pertambahan(self):
        self.angka1 = float(input("Masukan Angka Pertama: "))
        self.angka2 = float(input("Masukan Angka Kedua: "))
        
        hasil = self.angka1 + self.angka2
    
    
        print(f"hasil Penjumlahanya: {hasil}")
        
kalkulator = Penjumlahan()
kalkulator.pertambahan()
"""

class nilai_mahasiswa:
    def grade_nilai (self):
        #input data
        nama = input("Nama anda: ")
        nim = input("NIM anda: ")
        nilai = float(input("Nilai anda: "))
        
        #ketentuan nilai
        if nilai >= 80:
            grade = "A"
        
        elif nilai >= 77 and nilai <= 79.99:
            grade = "A-"
        
        elif nilai >= 74 and nilai <= 76.99:
            grade = "B+"
        
        elif nilai >= 68 and nilai <= 73.99:
            grade = ""
        
        elif nilai >= 65 and nilai <= 67.99:
            grade = "B-"
             
        elif nilai >= 62 and nilai <= 64.99:
            grade = "C+"    
            
        elif nilai >= 56 and nilai <= 61.99:
            grade = "C"
           
        elif nilai >= 45 and nilai <= 55.99:
            grade = "D" 

        elif nilai >= 0.00 and nilai <= 44.99:
            grade = "E"
            
            
        #Tampilan untuk user 
        print("--- DATA PRAKTIKUM PBO 2024 ---")
        print(f"Nama :{nama}")
        print(f"Nim  :{nim}")
        print(f"Jadi nilai anda = {grade}")
        

nilai =  nilai_mahasiswa ()
nilai.grade_nilai ()    

            
        
    
    
    

    
        