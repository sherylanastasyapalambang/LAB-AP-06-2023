print ("Pengujian jenis karakter")
print ("------------------------")
input = input("Karakter = ")

huruf_kapital = input.isupper()
huruf_kecil = input.islower()
angka = input.isdigit()

print ("Huruf kapital?", huruf_kapital)
print ("Huruf kecil?", huruf_kecil)
print ("Angka?", angka)
