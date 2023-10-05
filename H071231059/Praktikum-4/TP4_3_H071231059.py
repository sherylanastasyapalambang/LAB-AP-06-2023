def maksimum(x):
    maksimum = x[0]
    for i in x:
        if maksimum < i:
            maksimum = i
    return maksimum

x = [1, 2, 4, 6, 9, 1, 9, 10]
print(">>", maksimum(x))