# mencari solusi persamaan akar kuadrat ax^2 + bx + c = 0
a = float(input("masukkan nilai a : "))
b = float(input("masukkan nilai b : "))
c = float(input("masukkan nilai c : "))
D = (b*b) - (4*a*c)

print('(akar real dan berbeda)');
x1 = ((-b + (D**0.5)) / (2*a))
x2 = ((-b - (D**0.5)) / (2*a))
print('x1 = ',format(x1,".2f"))
print('x2 = ',format(x2,".2f"))
