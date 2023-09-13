# menentukan karakter
print('Pengujian jenis karakter\n---------------------')
x = str(input("Karakter = "))

Kapital = x.isupper()
Huruf_kecil = x.islower()
Angka = x.isdigit()

print(f'Huruf Kapital? {Kapital}')
print(f'Huruf kecil? {Huruf_kecil}')
print(f'Angka? {Angka}')