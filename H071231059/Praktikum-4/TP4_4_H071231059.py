def CatAndMouse(CatA, CatB, MouseC):
    a = abs(CatA - MouseC)
    b = abs(CatB - MouseC)
    if a > b:
        print("Cat B")
    elif a < b:
        print("Cat A")
    elif a == b:
        print("Mouse C")

CatAndMouse(CatA = 16, CatB = 24, MouseC = 15)

