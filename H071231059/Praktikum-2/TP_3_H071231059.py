golongan = input("Golongan = ")
daya = float(input("Daya = "))
pemakaian = float(input("Pemakaian = "))

import locale
locale.setlocale(locale.LC_ALL, 'id_ID')

if golongan == "R1":
    if daya == 900:
         a = pemakaian * 1352
         format_a = locale.currency(a, grouping=True, symbol=False)
         print(f"Jumlah tagihan anda sebesar : Rp. {format_a}")
    elif daya == 1300:
         b = pemakaian * 1444.70
         format_b = locale.currency(b, grouping=True, symbol=False)
         print(f"Jumlah tagihan anda sebesar : Rp. {format_b}")
    elif daya == 2200:
         c = pemakaian * 1444.70
         format_c = locale.currency(c, grouping=True, symbol=False)
         print(f"Jumlah tagihan anda sebesar : Rp. {format_c}")
    else:
         print("Daya yang dimasukkan tidak termasuk dalam golongan R1")
elif golongan == "R2":
    if 3500 <= daya <= 5500:
          d = pemakaian * 1699.53
          format_d = locale.currency(d, grouping=True, symbol=False)
          print(f"Jumlah tagihan anda sebesar : Rp. {format_d}")
    else:
         print("Daya yang dimasukkan tidak termasuk dalam golongan R2")
elif golongan == "R3":
     if daya >= 6600:
          e = pemakaian * 1699.53
          format_e = locale.currency(e, grouping=True, symbol=False)
          print(f"Jumlah tagihan anda sebesar : Rp. {format_e}")
     else:
          print("Daya yang dimasukkan tidak termasuk dalam golongan R2")
elif golongan == "B2":
     if 6600 <= daya <= 200000:
          f = pemakaian * 1444.70
          format_f = locale.currency(f, grouping=True, symbol=False)
          print(f"Jumlah tagihan anda sebesar : Rp. {format_f}")
     else:
         print("Daya daya yang dimasukkan tidak termasuk dalam golongan B2")
elif golongan == "B3":
     if daya >= 200000:
          g = pemakaian * 1114.74
          format_g = locale.currency(g, grouping=True, symbol=False)
          print(f"Jumlah tagihan anda sebesar : Rp. {format_g}")
     else:
          print("Daya tidak termasuk golongan B3")
elif golongan == "I3":
     if daya >= 200000:
          h = pemakaian * 1314.12
          format_h = locale.currency(h, grouping=True, symbol=False)
          print(f"Jumlah tagihan anda sebesar : Rp. {format_h}")
     else:
          print("Daya yang dimasukkan tidak termasuk dalam golongan I3")
elif golongan == "P1":
     if 6600 <= daya <= 200000:
          i = pemakaian * 1523.28
          format_i = locale.currency(i, grouping=True, symbol=False)
          print(f"Jumlah tagihan anda sebesar : Rp. {format_i}")
     else:
          print("Daya yang dimasukkan tidak termasuk dalam golongan P1")
else:
     print("Golongan yang dimasukkan tidak termasuk dalam data")
          