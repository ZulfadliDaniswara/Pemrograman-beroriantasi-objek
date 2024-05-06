from abc import ABC, abstractmethod
import math

class BangunDatar(ABC):
    @abstractmethod
    def luas(self):
        pass

class Persegi(BangunDatar):
    def __init__(self, sisi):
        self.sisi = sisi
    
    def luas(self):
        return self.sisi ** 2

class PersegiPanjang(BangunDatar):
    def __init__(self, panjang, lebar):
        self.panjang = panjang
        self.lebar = lebar
    
    def luas(self):
        return self.panjang * self.lebar

class Lingkaran(BangunDatar):
    def __init__(self, jari_jari):
        self.jari_jari = jari_jari
    
    def luas(self):
        return math.pi * self.jari_jari ** 2

class Segitiga(BangunDatar):
    def __init__(self, alas, tinggi):
        self.alas = alas
        self.tinggi = tinggi
    
    def luas(self):
        return 0.5 * self.alas * self.tinggi

class JajarGenjang(BangunDatar):
    def __init__(self, alas, tinggi):
        self.alas = alas
        self.tinggi = tinggi
    
    def luas(self):
        return self.alas * self.tinggi

def main():
    bangun_datar = [
        Persegi(5),
        PersegiPanjang(4, 6),
        Lingkaran(3),
        Segitiga(4, 5),
        JajarGenjang(4, 6)
    ]

    for bangun in bangun_datar:
        print("Luas:", bangun.luas())

if __name__ == "__main__":
    main()
