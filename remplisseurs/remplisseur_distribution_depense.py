from modeles.distribution_depense import Distribution_Depense

def remplir_distributions_depense(s):
    
    distribution1 = Distribution_Depense(
                id_depense = 1,
                id_entite = 2,
                pourcentage = 80,
                montant_paye = 0)
    
    distribution2 = Distribution_Depense(
                id_depense = 5,
                id_entite = 2,
                pourcentage = 80,
                montant_paye = 100)
    
    distribution3 = Distribution_Depense(
                id_depense = 3,
                id_entite = 2,
                pourcentage = 80,
                montant_paye = 80)
    
    distribution4 = Distribution_Depense(
                id_depense = 4,
                id_entite = 2,
                pourcentage = 80,
                montant_paye = 850)
    
    s.add_all([distribution1, distribution2, distribution3, distribution4])
    
    s.commit()