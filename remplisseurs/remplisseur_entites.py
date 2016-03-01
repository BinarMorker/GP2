from modeles.entite import Entite

def remplir_entites(s):
    
    entite1 = Entite(
                nom = "Jonathan")
        
    entite2 = Entite(
                nom = "Simon") 
       
    entite3 = Entite(
                nom = "Sarah")
    
    s.add_all([entite1, entite2, entite3])
    
    s.commit()