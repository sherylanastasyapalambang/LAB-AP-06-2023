# menghitung luas dan keliling segitiga siku-siku
print("Menghitung luas permukaan dan keliling segitiga")
x = float(input("Panjang sisi x : "))
y = float(input("Panjang sisi y : "))
z = (x ** 2 + y ** 2) ** 0.5

Luas = 1/2 * y * x
Keliling = x + y + z

luasfix = format(Luas, ".2f")
kelilingfix = format(Keliling, ".2f")

print(f'luas permukaan : {luasfix}')
print(f'keliling : {kelilingfix} ')