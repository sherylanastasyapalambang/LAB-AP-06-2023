# konversi detik menjadi jam 
print('Konversi detik ke jam')
detik = int(input("Masukkan jumlah detik : "))
detik = detik % (24 * 3600)
jam = detik // 3600
detik %= 3600
menit = detik // 60
detik %= 60 

print("%d:%02d:%02d" % (jam, menit, detik))