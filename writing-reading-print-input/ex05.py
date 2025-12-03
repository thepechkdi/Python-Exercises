#ex05
print("donner le prix ht")
prix_ht=float(input("prix_ht = "))
print("donner le taux de TVA")
TVA=float(input("TVA = "))
prix_ttc= prix_ht+(prix_ht*TVA/100)
print(" prix_ttc=",prix_ttc)

