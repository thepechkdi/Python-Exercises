#ex08
machat = float(input("saisir le montant d'achat "))
if machat < 50:
    print("Pas de Réduction")
elif machat >= 50 and machat < 100 :
    red = machat * 0.10
    print(" Tu es un Réduction de 10%, red=", red)
elif machat >= 100 :
   red = machat * 0.20
   print(" Tu es un Réduction de 20%, red=", red)

