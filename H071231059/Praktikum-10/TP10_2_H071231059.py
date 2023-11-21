from abc import ABC, abstractmethod

'''Encapsulation'''
class Hololive:
    def __init__(self, name, generation, gender):
        self._name = name 
        self._generation = generation 
        self.__gender = gender 

    def get_name(self):
        return self._name
    def set_name(self, name):
        self._name = name
    
    def get_generation(self):
        return self._generation
    def set_generation(self,  generation):
        if 0 <= generation <= 6:
            self._generation = generation
        else:
            print("There is no Hololive generation more than 6")
    
    def get_gender(self):
        return self.__gender
    def set_gender(self, gender):
        self.__gender = gender

member1 = Hololive("Hoshimachi Suisei", 0, "Female")

print("Sebelum diubah : ")
print("Name       :", member1.get_name())
print("Generation :", member1.get_generation())
print("Gender     :", member1.get_gender())

member1.set_name("Minato Aqua")
member1.set_generation(2)
member1.set_gender("Famale")

print("\nSesudah diubah: ")
print("Name       :", member1.get_name())
print("Generation :", member1.get_generation())
print("Gender     :", member1.get_gender())





'''Abstract Class, Inheritance, dan Polymorphism'''
class Bentuk(ABC):
    @abstractmethod
    def Hitung_Luas(self):
        pass

class Persegi_Panjang(Bentuk):
    def __init__(self, panjang, lebar):
        self.panjang = panjang
        self.lebar = lebar
    
    def Hitung_Luas(self):
        return self.panjang * self.lebar

class Belah_Ketupat(Bentuk):
    def __init__(self, diagonal1, diagonal2):
        self.diagonal1 = diagonal1
        self.diagonal2 = diagonal2
    
    def Hitung_Luas(self):
        return 0.5 * self.diagonal1 * self.diagonal2
    

persegi_panjang = Persegi_Panjang(7, 3)
belah_ketupat = Belah_Ketupat(4, 8)

print("\n\n\nLuas persegi panjang :", persegi_panjang.Hitung_Luas())
print("Luas belah ketupat :", belah_ketupat.Hitung_Luas())
