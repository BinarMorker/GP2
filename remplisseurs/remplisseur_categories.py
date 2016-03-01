from modeles.categorie import Categorie

def remplir_categories(s):
    
    categorie1 = Categorie(
                nom = "Essence",
                description = "Poste d'essence")
        
    categorie2 = Categorie(
                nom = "Restaurant",
                description = "BOUFFEEEEEEEE") 
       
    categorie3 = Categorie(
                nom = "Renovation",
                description = "Travaux effectues sur la maison")
    
    s.add_all([categorie1, categorie2, categorie3])
    
    s.commit()