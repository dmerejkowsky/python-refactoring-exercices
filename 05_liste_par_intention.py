# Exercice: remplacer le corps de la fonction
# par une liste par intention
def garde_les_positifs(nombres):
    résultat = []
    for nombre in nombres:
        if nombre > 0:
            résultat.append(nombre)
    return résultat


nombres = [1, -3, 2, -5, 2, 4]
print(garde_les_positifs(nombres))
