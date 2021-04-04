# Exercice: se débarrasser des ifs imbriqués
def controlle_conducteur(*, sobre, accompagné, permis):
    if sobre:
        if permis:
            return True
        else:
            if accompagné:
                return True
            else:
                return False
    else:
        return False


assert controlle_conducteur(sobre=True, accompagné=False, permis=True)
assert controlle_conducteur(sobre=True, accompagné=True, permis=False)
assert not controlle_conducteur(sobre=True, accompagné=False, permis=False)
assert not controlle_conducteur(sobre=False, accompagné=False, permis=True)
