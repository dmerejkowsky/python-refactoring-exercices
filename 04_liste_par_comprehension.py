# Exercice: remplacer le corps de la fonction
# par une liste par compéhension
def liste_des_carrés(n):
    résultat = []
    for i in range(n):
        résultat.append(i * i)
    return résultat


print(liste_des_carrés(5))
