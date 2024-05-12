"""
print("========================")
print("Nama: Zulfadli Daniswara")
print("NIM: 064002300025")
print("========================")
import math

class BangunRuang:
    def volume(*args):
        if len(args) == 1:  # Jika satu argumen, itu kubus
            sisi = args[0]
            return sisi ** 3
        elif len(args) == 3:  # Jika tiga argumen, itu balok
            panjang, lebar, tinggi = args
            return panjang * lebar * tinggi
        elif len(args) == 2:  # Jika dua argumen, itu tabung
            jari_jari, tinggi = args
            return math.pi * jari_jari ** 2 * tinggi
        else:
            return "Jumlah argumen tidak sesuai."


print("Volume Kubus:", BangunRuang.volume(15))

print("Volume Balok:", BangunRuang.volume(4, 6, 5))

print("Volume Tabung:", BangunRuang.volume(3, 9))
"""
"""
class p9e2:
    @staticmethod
    def methodTambahInt(x, y):
        return x + y
    
    @staticmethod
    def methodTambahfloat(x, y):
        return x + y
    
myNum1 = p9e2.methodTambahInt(8, 5)
myNum2 = p9e2.methodTambahfloat(4.5, 6.5)
print("int:", myNum1)
print("float:", myNum2)
"""

class p9e2:
    @staticmethod
    def methodTambah(*args):
        if all(isinstance(arg, int) for arg in args):
            return sum(args)
        elif all(isinstance(arg, float) for arg in args):
            return sum(args)
        else:
            raise TypeError("Arguments must be all int or all float")

myNum1 = p9e2.methodTambah(8, 5)
myNum2 = p9e2.methodTambah(4.5, 6.5)
print("int:", myNum1)
print("float:", myNum2)
