from modeles.categorie import Categorie

def remplir_categories(s):
    
    categorie1 = Categorie(
                nom = "Essence")
        
    categorie2 = Categorie(
                nom = "Restaurant") 
       
    categorie3 = Categorie(
                nom = "Renovation")
    
    s.add_all([categorie1, categorie2, categorie3])
    
    s.commit()