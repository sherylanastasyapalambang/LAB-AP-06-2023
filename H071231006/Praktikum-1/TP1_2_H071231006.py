print ("Konversi suhu dari Celcius ke Kelvin, Reamur dan Fahrenheit")
c = int(input("Masukkan Suhu dalam Celcius : "))

#Kelvin
K = int(c + 273)
print ("Hasil konversi dari suhu ",c, "Derajat Celcius ke Kelvin adalah :",(K),"K")

#Reamur
R = int((4/5) * c)
print ("Hasil konversi dari suhu ",c, "Derajat Celcius ke Reamur adalah :",(R),"R")

#Fahrenheit
F = int(((9/5)*c)+32)
print ("Hasil konversi dari suhu ",c, "Derajat Celcius ke Fahrenheit adalah :",(F),"F")
