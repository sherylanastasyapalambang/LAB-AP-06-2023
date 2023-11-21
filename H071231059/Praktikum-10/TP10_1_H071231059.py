import os
import re

class Detail:
    def __init__(self):
        self.nama = None
        self.email = None
        self.password = None
    
    def Buat_nama(self, nama):
        self.nama = nama

    def Buat_email(self, email):
        self.email = email

    def Buat_password(self, password):
        self.password = password

    def SimpanKeFile(self, nama_file):
        with open(nama_file, mode="a") as file:
            file.write(f"Nama          : {self.nama}\n")
            file.write(f"Email         : {self.email}\n")
            file.write(f"Password      : {self.password}\n")
            file.write(f"+{'=' * 100}\n")

def Welcome():
    print("=" * 50)
    print("Selamat Datang Silahkan Pilih Opsi Menu Anda")
    print("1. Detail Anda\n2. Ubah Nama\n3. Jumlah Data pada File\n4. Save Data pada File\n5. Buat Data Baru\n6. Keluar")

def Nama():
    nama = input("Silahkan Masukkan Nama: ")
    pattern_nama = r"[A-z\s]*"
    if re.fullmatch(pattern_nama, nama):
        return nama
    else:
        print(f"{'=' * 50}\nFormat nama hanya berupa huruf kapital maupun kecil")
        return Nama()

def Email(): 
    email = input("Silahkan Masukkan Email Anda: ")
    pattern_email = r"^[a-z]+([0-9]{2,})?@[a-z]+\.(com|co\.id|ac\.id|unhas\.ac\.id)$"
    if re.fullmatch(pattern_email, email):
        return email
    else:
        print(f"{'=' * 50}\nEmail yang anda masukkan salah\n{'=' * 50}")
        return Email()
    
def Password():
    password = input("Silahkan Masukkan Password Anda: ")
    pattern_pw = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,20}$" 
    if re.fullmatch(pattern_pw, password):
        return password
    elif len(password) < 8 or len(password) > 20:
        print(f"{'=' * 50}\nPassword Harus Memiliki Panjang 8-20\n{'=' * 50}")
        return Password()
    else:
        print(f"{'=' * 50}\nPassword yang anda masukkan terlalu lemah\nGunakan Minimal 1 Huruf Kapital, Huruf Kecil, dan Angka\n{'=' * 50}")
        return Password()

detail_akun = Detail()
while True:
    Welcome()
    opsi = input("Silahkan Pilih Opsi Anda : ")
    match opsi:
        case "1":
            if detail_akun.nama is None and detail_akun.email is None and detail_akun.password is None:
                print(f"{'=' * 50}\nData Saat Ini Kosong")
            else:
                print(f"{'=' * 50}\nData anda adalah\nNama     : {detail_akun.nama}\nEmail    : {detail_akun.email}\nPassword : {detail_akun.password}")
        case "2":
            if detail_akun.nama is None:
                print(f"{'=' * 50}\nData Saat Ini Kosong")
            else:
                nama_baru = input(f"{'=' * 50}\nSilahkan Input Nama Baru : ")
                detail_akun.Buat_nama(nama_baru)
                print("Nama berhasil diubah.")
        case "3":
            print(f"{'=' * 50}") 
            nama_file = input("Silahkan Masukkan Nama File: ") 
            nama_file += ".txt"
            if not os.path.exists(nama_file): 
                print(f"{'=' * 50}")
                print(f"Tidak Terdapat File Dengan Nama {nama_file[:-4]}") 
                print("Jumlah Data Pada File : 0 data")
            else:
                with open(nama_file, mode="r") as cari:
                    pattern_jumlah = re.findall(r"Nama          : ", cari.read())
                    print(f"{'=' * 50}")
                    print("File Ditemukan")
                    print(f"Jumlah Data Pada File : {len(pattern_jumlah)} data")
        case "4":
            if detail_akun.nama is None and detail_akun.email is None and detail_akun.password is None:
                print(f"{'=' * 50}\nData Saat Ini Kosong")
            else:
                print(f"{'=' * 50}")
                nama_file = input("Silahkan Masukkan Nama File : ") + ".txt"
                if not os.path.exists(nama_file):
                    with open(nama_file, mode="a") as file:
                        file.write(f"+{'='*99}\n")
                        file.write(f"|Data yang tersimpan\n")
                        file.write(f"+{'='*99}\n")
                detail_akun.SimpanKeFile(nama_file)
                print("Berhasil")
                detail_akun = Detail()
        case "5":
            print(f"{'=' * 50}")
            nama = Nama()
            email = Email()
            password = Password()
            detail_akun.Buat_nama(nama=nama)
            detail_akun.Buat_email(email)
            detail_akun.Buat_password(password)
        case "6":
            print(f"{'=' * 50}\nSampai Jumpa Lagi")
            break
        case _:
            print("INVALID INPUT")
            break
