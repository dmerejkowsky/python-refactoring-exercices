# Rien à changer ici :)
import time


def pause(f):
    def res():
        f()
        time.sleep(0.3)

    return res


@pause
def allumer_bouilloire():
    print("Bouilloire allumée")


@pause
def ouvrir_placard():
    print("Placard ouvert")


@pause
def fermer_placard():
    print("Placard fermé")


@pause
def attendre_que_ca_bout():
    print("...")


@pause
def eteindre_bouilloire():
    print("Bouilloire éteinte")


@pause
def prendre_une_tasse():
    print("Tasse en main")


@pause
def mettre_eau_dans_tasse():
    print("Versement de l'eau dans la tasse")


@pause
def mettre_thé_dans_tasse():
    print("Ajout du thé dans la tasse")


@pause
def attendre_que_ca_infuse():
    print("...")


@pause
def prendre_un_plateau():
    print("Plateau en main")


@pause
def mettre_tasse_sur_plateau():
    print("Le plateau contient une tasse")


@pause
def mettre_sucrière_sur_plateau():
    print("Le plateau contient une sucrière")


@pause
def apporter_le_plateau():
    print("Le plateau arrive sur la table")


@pause
def rajouter_eau():
    print("Rajouter eau")


@pause
def rajouter_lait():
    print("Rajouter lait")


@pause
def rajouter_sucre():
    print("Rajouter sucre")
