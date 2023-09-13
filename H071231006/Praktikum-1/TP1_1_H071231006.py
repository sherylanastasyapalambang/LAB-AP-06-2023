
print ("Menghitung Luas Permukaan dan Luas Segitiga")
x = int(input("Panjang sisi X  : "))
y = int(input("Panjang sisi Y  : "))
z = (x**2 + y**2)**0.5

luas = float(0.5 * x * y)
keliling = float(x + y + z)

print ("Luas Permukaan : ",format(luas,".2f"))
print ("Keliling : " ,format(keliling,".2f"))