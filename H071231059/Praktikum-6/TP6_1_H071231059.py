dictionary = {"nama" : "", "umur" : "", "alamat" : ""}
print("Selamat datang untuk memulai silahkan input data anda")

a = input("Input nama : ").title()
dictionary["nama"] = a

b = input("Input umur : ")
dictionary["umur"] = b

c = input("Input alamat : ")
dictionary["alamat"] = c

while True:
    print(f"""==================================================
Selamat datang {dictionary['nama']} silahkan pilih opsi
==================================================
1. Detail Anda
2. Ubah Nama
3. Ubah Umur
4. Ubah Alamat
5. Keluar
==================================================""")
    opsi = input("Input opsi: ")
    match opsi:
        case "1": 
            print(f"""
==================================================
Data anda adalah
Nama : {dictionary["nama"]}
Umur : {dictionary["umur"]}
Alamat : {dictionary["alamat"]}\n""")
        case "2":
            inputan = input("Silahkan Input nama baru : ").title()
            dictionary["nama"] = inputan
            print("Data anda sukses diperbarui\n")
        case "3":
            inputan = input("Silahkan Input umur baru : ")
            dictionary["umur"] = inputan
            print("Data anda sukses diperbarui\n")
        case "4":
            inputan = input("Silahkan Input alamat baru : ")
            dictionary["alamat"] = inputan
            print("Data anda sukses diperbarui\n")
        case "5":
            print(f"Selamat Tinggal {dictionary['nama']}")
            break
        case _:
            print("Invalid Input")

