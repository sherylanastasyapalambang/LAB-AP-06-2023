def stringPermutation(n):
    for i in range(len(n)):
        n = n[-1] + n[:-1]
        print(n, end=" | ")
try:
    stringPermutation("Mobil")
except TypeError:
    print("Invalid input")