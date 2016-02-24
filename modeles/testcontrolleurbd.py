from modeles.depense import Depense

def tester_modeles(s):
    
    depense = Depense(
                id_categorie = 1,
                nom = "Canadian Tire",
                description = "",
                montant = "15247.25")
    
    
    s.add(depense)
    
    s.commit()