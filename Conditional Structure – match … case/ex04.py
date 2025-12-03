#ex04
nom_animale=str(input("Entre le nome de animale : "))
match nom_animale :
    case "chien" | "chat":
        print("Mammifère")
    case "aigle" | "pigeon":
        print("Mammifère")
    case "aigle" | "pigeon":
        print("Oiseau")
    case "serpent" | "crocodile":
        print("Reptile")
    case _:
         print("Classification inconnue")