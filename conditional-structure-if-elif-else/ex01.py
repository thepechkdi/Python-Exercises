#ex01
nb=float(input("saisir un nombre, nb = "))
v = nb % 2
if v == 0:
    print(f"{nb} est pair")
elif v == 1:
    print(f"{nb} est impair")
else:
   print("saisir un nombre entier")
 