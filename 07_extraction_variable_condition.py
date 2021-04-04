# Exercice: rendre la fonction peut_voter() plus lisible
# et plus explicite
class Personne:
    def __init__(self, age, nationalité, inscrite):
        self.age = age
        self.nationalité = nationalité
        self.inscrite = inscrite


def peut_voter(personne):
    return (
        personne.age >= 18 and personne.nationalité == "Française" and personne.inscrite
    )


martine = Personne(42, "Française", True)
assert peut_voter(martine)

kevin = Personne(12, "Française", True)
assert not peut_voter(kevin)
