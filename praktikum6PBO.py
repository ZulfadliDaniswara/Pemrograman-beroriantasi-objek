import math

class BangunRuang:
    def __init__(self):
        pass

    def luas(self):
        pass

    def volume(self):
        pass

class Kubus(BangunRuang):
    def __init__(self, sisi):
        self.sisi = sisi

    def luas(self):
        return 6 * self.sisi * self.sisi

    def volume(self):
        return self.sisi ** 3

class Balok(BangunRuang):
    def __init__(self, panjang, lebar, tinggi):
        self.panjang = panjang
        self.lebar = lebar
        self.tinggi = tinggi

    def luas(self):
        return 2 * (self.panjang * self.lebar + self.panjang * self.tinggi + self.lebar * self.tinggi)

    def volume(self):
        return self.panjang * self.lebar * self.tinggi

class Bola(BangunRuang):
    def __init__(self, jari_jari):
        self.jari_jari = jari_jari

    def luas(self):
        return 4 * math.pi * self.jari_jari * self.jari_jari

    def volume(self):
        return (4/3) * math.pi * self.jari_jari ** 3

class Tabung(BangunRuang):
    def __init__(self, jari_jari, tinggi):
        self.jari_jari = jari_jari
        self.tinggi = tinggi

    def luas(self):
        return 2 * math.pi * self.jari_jari * (self.jari_jari + self.tinggi)

    def volume(self):
        return math.pi * self.jari_jari ** 2 * self.tinggi

class LimasSegitiga(BangunRuang):
    def __init__(self, alas, tinggi):
        self.alas = alas
        self.tinggi = tinggi

    def luas(self):
        return math.sqrt(3) * self.alas * self.alas / 4 + 3 * self.alas * self.tinggi / 2

    def volume(self):
        return (math.sqrt(3) * self.alas * self.alas * self.tinggi) / 12

# Contoh penggunaan
kubus = Kubus(5)
print("Luas Kubus:", kubus.luas())
print("Volume Kubus:", kubus.volume())

balok = Balok(3, 4, 5)
print("Luas Balok:", balok.luas())
print("Volume Balok:", balok.volume())

bola = Bola(4)
print("Luas Bola:", bola.luas())
print("Volume Bola:", bola.volume())

tabung = Tabung(3, 7)
print("Luas Tabung:", tabung.luas())
print("Volume Tabung:", tabung.volume())

limas = LimasSegitiga(6, 8)
print("Luas Limas Segitiga:", limas.luas())
print("Volume Limas Segitiga:", limas.volume())
