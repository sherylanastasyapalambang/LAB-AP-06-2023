print('Pengujian jenis karakter\n-------------------------')
karakter = input ('karakter = ')

print(f'Huruf kapital? {karakter.isupper()}')
print(f'Huruf kecil? {karakter.islower()}')
print(f'Angka? {karakter.isdigit()}')