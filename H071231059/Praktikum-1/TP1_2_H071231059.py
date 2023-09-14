print('Koversi Suhu dari Celcius ke Kelvin, Reamur, dan Farenheit')
C = int(input('Masukkan suhu dalam celcius : '))

K = C + 273
R = int((4/5)*C)
F = int((9/5)*C + 32)

print(f'Hasil konversi dari suhu {C} derajat celcius ke Kelvin adalah : {K}K')
print(f'Hasil konversi dari suhu {C} derajat celcius ke Reamur adalah : {R}R')
print(f'Hasil konversi dari suhu {C} derajat celcius ke Farenheit adalah : {F}F')