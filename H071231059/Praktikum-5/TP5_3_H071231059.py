kata1 = input("Masukkan Kata Pertama : ").lower()
kata2 = input("Masukkan Kata Kedua : ").lower()

kata1 = kata1.replace(" ", "")
kata2 = kata2.replace(" ", "")

x1 = []
x2 = []

for i in kata1:
    x, y = kata1.count(i), kata2.count(i)
    x1.append(x)
    x2.append(y)

if  len(kata1) != len(kata2):
    print("False")
elif x1 == x2:
    print("True") 
else:
    print("False")

