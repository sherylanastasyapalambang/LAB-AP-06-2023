s1 = input("String 1 : ")
s2 = input("String 2 : ")
s2 = ''.join(reversed(s2))

s3 = ""

min_len = min(len(s1),len(s2))

for i in range(min_len):
    s3 += s1[i] + s2[i]
s3 += s1[min_len:] + s2[min_len:]

print(s3)
