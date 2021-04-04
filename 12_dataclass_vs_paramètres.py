# Exercice: introduire une classe Commande pour
# éviter las répétition des paramètres
# allongé, noisette et sans_sucre
from cuisine import *


def commande_café(allongé, noisette, sans_sucre):
    print("Je voudrais un café", end=" ")
    if allongé:
        print("allongé", end=" ")
    else:
        print("serré", end=" ")
    if noisette:
        print("noisette", end=" ")
    if sans_sucre:
        print("sans sucre", end=" ")
    print()

    faire_le_café(allongé, noisette, sans_sucre)
    servir_café()


def faire_le_café(allongé, noisette, sans_sucre):
    avec_sucre = not sans_sucre
    if allongé:
        rajouter_eau()
    if noisette:
        rajouter_lait()
    if avec_sucre:
        rajouter_sucre()


def servir_café():
    print("voici")


commande_café(False, False, False)
commande_café(False, True, False)
commande_café(True, True, False)
