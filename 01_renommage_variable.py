# Exercice: remplacer n, s et x avec de meilleurs noms
def calcule_moyenne(scores):
    n = len(scores)
    s = 0
    for x in scores:
        s = s + x
    return s / n


scores = [2, 3, 5, 4]
moyenne = calcule_moyenne(scores)
print(moyenne)
