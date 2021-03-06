from modeles.depense import Depense

def remplir_depenses(s):

    depense1 = Depense(
                nom = "McDo",
                id_categorie = 2,
                description = "",
                montant = "54")
    
    depense2 = Depense(
                nom = "Hydro-Quebec",
                id_categorie = 3,
                description = "",
                montant = "120")
    
    depense3 = Depense(
                nom = "La Capitale",
                id_categorie = 3,
                description = "",
                montant = "250")
    
    depense4 = Depense(
                nom = "Tim Hortons",
                id_categorie = 2,
                description = "",
                montant = "40.75")
    
    depense5 = Depense(
                nom = "Walt Mart",
                id_categorie = 2,
                description = "",
                montant = "15")
    
    depense6 = Depense(
                nom = "Costco",
                id_categorie = 2,
                description = "",
                montant = "101.79")
    
    depense7 = Depense(
                nom = "Shell",
                id_categorie = 1,
                description = "",
                montant = "54")
    
    depense8 = Depense(
                nom = "Irving",
                id_categorie = 1,
                description = "",
                montant = "47.98")
    
    depense9 = Depense(
                nom = "Ville",
                id_categorie = 3,
                description = "",
                montant = "1012")
    
    depense10 = Depense(
                nom = "Canadian Tire",
                id_categorie = 2,
                description = "",
                montant = "15")
        
    s.add_all([depense1, depense2, depense3, depense4, depense5, depense6, depense7, depense8, depense9, depense10])
    
    s.commit()
