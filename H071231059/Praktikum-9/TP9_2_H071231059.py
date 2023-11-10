class Mahasiswa:
    def __init__(self, Nama, Nim, Jurusan, Ipk):
        self.nama = Nama
        self.nim = Nim
        self.jurusan = Jurusan
        self.ipk = Ipk
    
    def Tampilkan_info(self):
        print('\nNama     : ',self.nama)
        print('NIM      : ',self.nim)
        print('Jurusan  : ',self.jurusan)
        print('IPK      : ',self.ipk)
    
    def Hitung_predikat(self):
        if self.ipk >= 3.5:
            print("\nPredikat dari IPK kamu adalah Cumlaude")
        elif self.ipk >= 3.0:
            print("\nPredikat dari IPK kamu adalah sangat memuaskan")
        elif self.ipk >= 2.5:
            print("\nPredikat dari IPK kamu adalah memuaskan")
        elif self.ipk >= 2.0:
            print("\nPredikat dari IPK kamu adalah cukup")
        elif self.ipk < 2.0:
            print("\nPredikat dari IPK kamu adalah kurang")


nama = input("Masukkan nama anda: ").title()
nim = input("Masukkan nim anda: ")
jurusan = input("Masukkan jurusan anda: ")
ipk = float(input("Masukkan ipk anda: "))

data = Mahasiswa(nama, nim, jurusan, ipk)
data.Tampilkan_info()
data.Hitung_predikat()
