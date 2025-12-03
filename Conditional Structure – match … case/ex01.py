#ex01
nbr=int(input("Entre un nomber entre 1 et 7, nbr = "))

match nbr:
    case 1:
        print("Lundi")
    case 2:
        print("Mardi")
    case 3:
        print("Mercredi")
    case 4:
        print("Juedi")
    case 5:
        print("Venderedi")
    case 6:
        print("Samedi")
    case 7:
        print("Dimench")
    case _:
        print("Jeuer inavlide")
