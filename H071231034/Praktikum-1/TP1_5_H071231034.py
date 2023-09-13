print("Konversi detik ke jam")
detik = int(input("Masukkan jumlah detik: "))

menit = detik // 60  # 1 menit = 60 detik
detik %= 60  # Hitung sisanya kemudian masukkan ke detik
jam = menit // 60  # 1 jam = 60 menit
menit %= 60  # Hitung sisanya kemudian masukkan ke menit

print(f"\n{jam:02}:{menit:02}:{detik:02}")