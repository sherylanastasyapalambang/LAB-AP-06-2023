inputan_pertama = input("Masukkan Input Pertama : ")
inputan_kedua = input("Masukkan Input Kedua : ")
inputan_ketiga = input("Masukkan Input Ketiga : ")

match inputan_pertama:
    case "vertebrado":
        match inputan_kedua:
            case "ave":
                match inputan_ketiga:
                    case "carnivoro":
                        print("agula")
                    case "onivoro":
                        print("pomba")
                    case _:
                        print("Invalid input")
            case "mamifero":
                match inputan_ketiga:
                    case "onivoro":
                        print("homem")
                    case "herbivoro":
                        print("vaca")
                    case _:
                        print("Invalid input")
            case _:
                print("Invalid input")
    case "invertebrado":
        match inputan_kedua:
            case "inseto":
                match inputan_ketiga:
                    case "hematofago":
                        print("pulga")
                    case "herbivoro":
                        print("lagarta")
                    case _:
                        print("Invalid input")
            case "anelideo":
                match inputan_ketiga:
                    case "hematofago":
                        print("sanguessuga")
                    case "onivoro":
                        print("minhoca")
                    case _:
                        print("Invalid input")
            case _:
                print("Invalid input")
    case _:
        print("Invalid input")