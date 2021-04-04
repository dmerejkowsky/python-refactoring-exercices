# Exercice: renommer demander_si_ca_va() en
# demander_des_nouvelles() et être_poli()
# en démarrer_conversation()
def dire_bonjour(appelation):
    print("Bonjour", appelation)


def demander_si_ca_va():
    print("Ça va?")


def être_poli(appelation):
    dire_bonjour(appelation)
    demander_si_ca_va()


être_poli("Jeanne")
