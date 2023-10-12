word = input("Masukkan kata : ")

if len(word) % 2 != 0: 
    x = word[0] + word[len(word)//2] + word[-1]
    print(x)
else:
    y = word[0] + word[len(word)/2-1] + word[len(word)/2] + word[-1]
    print(y)




