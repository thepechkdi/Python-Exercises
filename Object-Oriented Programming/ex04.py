class CompteBancaire:
    def __init__(self):
        """Initialisation du compte avec un solde de 0."""
        self.solde = 0  

    def deposer(self, montant):
        """Ajoute un montant au solde."""
        if montant > 0:
            self.solde = self.solde + montant
            print(f"Vous avez déposé {montant} €. Solde actuel : {self.solde} €.")
        else:
            print("Le montant doit être positif.")

    def retirer(self, montant):
        """Retire un montant du solde si possible."""
        if 0 < montant <= self.solde:
            self.solde = self.solde - montant
            print(f"Vous avez retiré {montant} €. Solde actuel : {self.solde} €.")
        elif montant > self.solde:
            print("Fonds insuffisants pour effectuer ce retrait.")
        else:
            print("Le montant doit être positif.")

    def afficher_solde(self):
        """Affiche le solde actuel."""
        print(f"Solde actuel : {self.solde} €.")

# Création d'un compte bancaire
mon_compte = CompteBancaire()

# Dépôt d'argent
mon_compte.deposer(500)
mon_compte.deposer(200)

# Retrait d'argent
mon_compte.retirer(100)
mon_compte.retirer(700)  # Tentative de retrait supérieur au solde

# Affichage du solde final
mon_compte.afficher_solde()
