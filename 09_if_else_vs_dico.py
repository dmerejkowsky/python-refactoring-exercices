# Exercice: remplacer tous les if/else
# avec un dictionnaire
def conversion(mesure, unité):
    if unité == "m":
        return mesure
    elif unité == "km":
        return mesure * 1000
    elif unité == "miles":
        return mesure * 1609


print("3 km =", conversion(3, "km"), "m")
print("2 miles =", conversion(2, "miles"), "m")
