from modeles.depense import Depense
from modeles.division_depense import Division_Depense
from modeles.entite import Entite
from modeles.categorie import Categorie

def tester_modeles(s):
    
    categorie = Categorie(
                nom = "Autres")
    
    depense = Depense(
                id_categorie = 1,
                nom = "Canadian Tire",
                description = "",
                montant = "15247.25")
    
    entite = Entite(
                nom = "Francois")
    
    division = Division_Depense(
                id_depense = 1,
                id_entite = 1,
                pourcentage = 80,
                montant_paye = 10.00)
    
    
    s.add_all([categorie, depense, entite, division])
    
    s.commit()