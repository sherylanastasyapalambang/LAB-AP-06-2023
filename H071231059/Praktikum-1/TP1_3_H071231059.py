print('Solusi Persamaan Kuadrat')

a = float(input('Input a = '))
b = float(input('Input b = '))
c = float(input('Input c = '))

if a == 0:
    print('Nilai a tidak boleh sama dengan 0')
else:
    x1 = (-b +((b**2)-4*a*c)**0.5)/(2*a)
    x2 = (-b -((b**2)-4*a*c)**0.5)/(2*a)
    
    print(f'x1 = {x1:.02f}')
    print(f'x2 = {x2:.02f}')