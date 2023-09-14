print('Konversi detik ke jam')
s = int(input('Masukkan jumlah detik: '))

jam = s//3600
menit = (s%3600)//60
detik = s%60

print(f'{jam:02d}:{menit:02d}:{detik:02d}')
