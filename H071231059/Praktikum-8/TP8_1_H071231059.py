import re
string = input()

pattern = r"^[A-z24680]{40}[\s13579]{5}$"
result = re.match(pattern, string)

if result:
    print(True)
else:
    print(False)