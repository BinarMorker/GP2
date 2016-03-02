from modeles.membre import Membre

def remplir_membres(s):
    
    membre1 = Membre(
                nom = "Jonathan")
        
    membre2 = Membre(
                nom = "Simon") 
       
    membre3 = Membre(
                nom = "Sarah")
    
    s.add_all([membre1, membre2, membre3])
    
    s.commit()