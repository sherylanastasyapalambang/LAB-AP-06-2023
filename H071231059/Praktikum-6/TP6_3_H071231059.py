angka = list(map(int, (input("Masukkan beberapa angka: ").split())))

genap, ganjil, kelipatan_5 = [], [], []

for i in angka:
    if i % 2 == 0:
        genap.append(i)
    if i % 2 != 0:
        ganjil.append(i)
    if i % 5 == 0:
        kelipatan_5.append(i)

print(f"Angka Genap:{genap}\nAngka Ganjil: {ganjil}\nAngka yang habis dibagi 5: {kelipatan_5}")
