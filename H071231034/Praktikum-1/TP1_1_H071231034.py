print("Menghitung luas permukaan dan keliling segitiga")
x=float(input("Panjang sisi X : "))
y=float(input("Panjang sisi Y : "))

print(f"\nLuas permukaan : {(1/2)*x*y:.2f}")
print(f"Keliling : {(x**2+y**2)**0.5+x+y:.2f}") # (x**2+y**2)**0.5 itu sisi miringnya