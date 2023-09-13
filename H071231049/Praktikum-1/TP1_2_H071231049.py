# konversi suhu celcius
print('Konversi suhu dari Celcius ke Kelvin, Reamur, dan Fharenheit')
Celcius = int(input("masukkan suhu dalam celcius : "))

Kelvin = int(Celcius + 273)
Reamur = int(Celcius * (4/5))
Fahrenheit = int((9/5 * Celcius) + 32)

print(f'Hasil konversi suhu {Celcius} derajat Celcius ke Kelvin adalah : {Kelvin}K')
print(f'Hasil konversi suhu {Celcius} derajat Celcius ke Reamur adalah : {Reamur}R ')
print(f'Hasil konversi suhu {Celcius} derajat Celcius ke Fahrenheit adalah : {Fahrenheit}F')
