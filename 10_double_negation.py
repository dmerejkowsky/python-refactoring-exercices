# Exercice: ne pas utiliser la double négation
def faire_le_café(sans_sucre):
    if not sans_sucre:
        print("avec du sucre")
    else:
        print("sans sucre")


 faire_le_café(sans_sucre=True)
 faire_le_café(sans_sucre=False)
