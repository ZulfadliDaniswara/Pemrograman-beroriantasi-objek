print('====================')
print('Nama : Zulfadli Daniswara')
print('NIM : 064002300025')
print('====================')
class Masyarakatkampus:
    def __init__(self, nama):
        self.nama = nama

    def Gaji(self):
        pass

class Dosen(Masyarakatkampus):
    def __init__(self):
        super().__init__("Dosen")

    def Gaji(self):
        return "Golongan Dosen mendapatkan gaji: 450000"

class Karyawan(Masyarakatkampus):
    def __init__(self):
        super().__init__("STAFF")

    def Gaji(self):
        return "Golongan STAFF mendapatkan gaji: 300000"

class Lain(Masyarakatkampus):
    def __init__(self):
        super().__init__("Lain")

    def Gaji(self):
        return "Golongan Lain mendapatkan gaji: 150000"

def main():
    dosen = Dosen()
    karyawan = Karyawan()
    lain = Lain()

    print(dosen.Gaji())
    print(karyawan.Gaji())
    print(lain.Gaji())

if __name__ == "__main__":
    main()
