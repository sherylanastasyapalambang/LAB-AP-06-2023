array1 = set(map(int, (input("Input array ke-1: ").split())))
array2 = set(map(int,(input("input array ke-2: ").split())))

iris = array1 & array2

iris_tupple = tuple(iris)

x = len(iris_tupple)

if x > 1:
    print(f"Terdapat {x} buah duplikat yaitu {iris_tupple}")
elif x == 1:
    print(f"Terdapat {x} buah duplikat yaitu ({iris_tupple[0]})")
else:
    print("Tidak ada duplikasi ditemukan.")
