from modeles.depense import Depense
from modeles.distribution_depense import Distribution_Depense
from modeles.membre import Membre
from modeles.categorie import Categorie

def tester_modeles(s):
    
    categorie = Categorie(
                nom = "Autres")
    
    depense = Depense(
                id_categorie = 1,
                nom = "Canadian Tire",
                description = "",
                montant = "15247.25")
    
    membre = Membre(
                nom = "Francois")
    
    distribution = Distribution_Depense(
                id_depense = 1,
                id_membre = 1,
                pourcentage = 80,
                montant_paye = 10.00)
    
    
    s.add_all([categorie, depense, membre, distribution])
    
    s.commit()