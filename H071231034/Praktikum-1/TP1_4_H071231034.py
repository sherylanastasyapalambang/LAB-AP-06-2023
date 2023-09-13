print("Pengujian jenis karakter \n------------------------")
k=input("Masukkan karakter = ")

huruf_besar = k.isupper()
huruf_kecil = k.islower()
angka = k.isdigit()

print(f"\nHuruf besar? {huruf_besar}")
print(f"Huruf kecil? {huruf_kecil}")
print(f"Angka? {angka}")