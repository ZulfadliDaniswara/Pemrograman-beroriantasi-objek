def honorific(cls):
    class HonorificCls(cls):
        def nama_lengkap(self):
            full_name = super().nama_lengkap()
            return f"Mr. {full_name}"
    
    return HonorificCls

@honorific
class Nama(object):
    def __init__(self, nama_depan, nama_belakang, nim):
        self.nama_depan = nama_depan
        self.nama_belakang = nama_belakang
        self.nim = nim

    def nama_lengkap(self):
        return " ".join([self.nama_depan, self.nama_belakang, self.nim])

result = Nama("Zulfadli", "Daniswara", "064002300025").nama_lengkap()
print("Full name: {0}".format(result))
