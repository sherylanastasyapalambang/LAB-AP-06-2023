gender = int(input("Pilih Gender Anda\n1. Pria\n2. Wanita\n= "))
height = float(input("Masukkan tinggi badan (cm) : "))
weight = float(input("Masukkan berat badan (kg) : "))

BMI = weight / ((height / 100)** 2)

if gender == 1:
    if BMI < 18:
        print(f"Anda tergolong Underweight dengan BMI {BMI:.2f}")
    elif 18 <= BMI <= 23.9:
        print(f"Anda tergolong Normal dengan BMI {BMI:.2f}")
    elif 24<= BMI <=26.9:
        print(f"Anda tergolong Overweight dengan BMI {BMI:.2f}")
    else:
        print(f"Anda tergolong Obese dengan BMI {BMI:.2f}")
elif gender == 2:
    if BMI < 17:
        print(f"Anda tergolong Underweight dengan BMI {BMI:.2f}")
    elif 17 <= BMI <= 23.9:
        print(f"Anda tergolong Normal dengan BMI {BMI:.2f}")
    elif 24<= BMI <=27.9:
        print(f"Anda tergolong Overweight dengan BMI {BMI:.2f}")
    else:
        print(f"Anda tergolong Obese dengan BMI {BMI:.2f}")
else:
    print("Nomor yang anda masukkan tidak termasuk dalam pilihan")