print("Mencari akar-akar persamaan kuadrat")
a=float(input("Input a = "))

if a==0:
    print("a tidak bisa 0.")
    exit()
    
b=float(input("Input b = "))
c=float(input("Input c = "))

print(f"\nx1 = {((-b+(b**2-4*a*c)**0.5)/(2*a)):.2f}")
print(f"x2 = {((-b-(b**2-4*a*c)**0.5)/(2*a)):.2f}")