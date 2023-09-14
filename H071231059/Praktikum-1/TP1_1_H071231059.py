print('Menghitung luas permukaan dan keliling segitiga')
x = float(input('Masukkan panjang sisi X : '))
y = float(input('Masukkan panjang sisi Y : '))
z = ((x*x + y*y))**0.5

luas = (x*y)/2 
keliling = x+y+z

print(f'Luas Permukaan = {luas:.2f}')
print(f'Keliling = {keliling:.2f}')