import re
pattern_IPv4 = r"^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4[0-9]|1[0-9][0-9]|[01]?[0-9][0-9]?)$"
pattern_IPv6 = r"^(([A-z0-9][A-z0-9]?[A-z0-9]?[A-z\d]?)\:){7}([A-z0-9][A-z0-9]?[A-z0-9]?[A-z0-9]?)$"
loop = int(input("Jumlah baris inputan: "))

list = []

for i in range(loop):
    j = input("Masukkan IP Address: ")
    list.append(j)
for IP_Address in list:
    if re.search(pattern_IPv4, IP_Address):
        print("IPv4")
    elif re.search(pattern_IPv6, IP_Address):
        print("IPv6")
    elif len(IP_Address) >= 500:
        print("Tidak boleh melebihi 500 karakter")
    else:
        print("Bukan IP Address")
