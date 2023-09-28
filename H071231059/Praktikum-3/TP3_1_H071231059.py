n = int(input())
if n < 0:
    print("Suku fibonacci tidak boleh kurang dari 0 atau bilangan negatif")
elif n == 1:
    print(0)
else:
    u1 = 0
    u2 = 1
    print(u1, u2, end=" ")
    for i in range(n-2):
        u3 = u1 + u2 
        u1, u2 = u2, u3
        print(u3, end=" ")
