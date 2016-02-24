from modeles.division_depense import Division_Depense

def remplir_divisions_depense(s):
    
    division1 = Division_Depense(
                id_depense = 1,
                id_entite = 2,
                pourcentage = 80,
                montant_paye = 0)
    
    division2 = Division_Depense(
                id_depense = 5,
                id_entite = 2,
                pourcentage = 80,
                montant_paye = 100)
    
    division3 = Division_Depense(
                id_depense = 3,
                id_entite = 2,
                pourcentage = 80,
                montant_paye = 80)
    
    division4 = Division_Depense(
                id_depense = 4,
                id_entite = 2,
                pourcentage = 80,
                montant_paye = 850)
    
    division5 = Division_Depense(
                id_depense = 2,
                id_entite = 2,
                pourcentage = 80,
                montant_paye = 100)
    
    s.add_all([division1, division2, division3, division4, division5])
    
    s.commit()