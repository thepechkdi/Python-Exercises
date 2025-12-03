#ex05
note = float(input("saisir la note, note = "))
if note >= 0 and note <=20 :
    if note < 10:
        print("échec")
    elif note >= 10 and note < 12:
        print("passable ")
    elif note >= 12 and note < 14:
        print("assez bien") 
    elif note >= 14 and note < 16:
        print(" bien") 
    elif note >= 16 and note <= 20:
        print(" Tré bien") 
else :
    print("Entre un nomber entre 0 et 20 svp")

