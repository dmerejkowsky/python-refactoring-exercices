# Exercice: découper la fonction servir_le_thé() en trois
from cuisine import *

def faire_bouillir_l_eau():
    allumer_bouilloire()
    attendre_que_ca_bout()
    eteindre_bouilloire()


def servir_le_thé():
    faire_bouillir_l_eau()


    # Remplir une tasse
    ouvrir_placard()
    prendre_une_tasse()
    mettre_eau_dans_tasse()
    mettre_thé_dans_tasse()
    attendre_que_ca_infuse()
    fermer_placard()

    # Servir sur un plateau
    prendre_un_plateau()
    mettre_tasse_sur_plateau()
    mettre_sucrière_sur_plateau()
    apporter_le_plateau()


servir_le_thé()
