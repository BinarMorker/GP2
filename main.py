import sys
from controlleurs.depenses import DepensesControlleur as Controlleur

def menu_principal():
    '''Affiche le menu principal'''
    while True:
        print("Que voulez-vous faire?",
              "\n    1 - Voir dépenses"
              "\n    2 - Voir dépense #"
              "\n    3 - Ajouter dépense"
              "\n    4 - Modifier dépense"
              "\n    5 - Supprimer dépense"
              "\n    0 - Quitter")
        options = {'1': lambda: Controlleur.liste_depenses(),
        		   '2': lambda: voir_depense(),
        		   '3': lambda: ajouter_depense(),
        		   '4': lambda: modifier_depense(),
        		   '5': lambda: supprimer_depense(),
                   '0': lambda: sys.exit(0)}
        choix = valider_choix(len(options))
        options[choix]()
        print("")

def voir_depense():
    depense_id = 0
    while not depense_id or depense_id == 0:
        depense_id = input('Id de la dépense: ')
    Controlleur.voir_depense(depense_id)

def modifier_depense():
    depense_id = 0
    while not depense_id or depense_id == 0:
        depense_id = input('Id de la dépense: ')
    depense_nom = input("Nom de la dépense (0 si aucun changement): ")
    if depense_nom == 0:
        depense_nom = None
    depense_montant = input('Montant de la dépense (0 si aucun changement): ')
    if depense_montant == 0 or not is_float(depense_montant):
        depense_montant = None
    depense_categorie = input('Catégorie de la dépense (0 si aucun changement): ')
    if depense_categorie == 0:
        depense_categorie = None
    depense_description = input('Description de la dépense (0 si aucun changement): ')
    if depense_description == 0:
        depense_description = None
    Controlleur.modifier_depense(depense_id, depense_nom, depense_montant, depense_categorie, depense_description)
    
def ajouter_depense():
    depense_nom = ""
    depense_montant = 0.0
    while not depense_nom:
        depense_nom = input("Nom de la dépense: ")
    while not depense_montant or depense_montant == 0 or not is_float(depense_montant):
        depense_montant = input('Montant de la dépense: ')
    depense_categorie = input('Catégorie de la dépense (Entrée si aucune): ')
    depense_description = input('Description de la dépense (Entrée si aucune): ')
    Controlleur.ajouter_depense(depense_nom, depense_montant, depense_categorie, depense_description)

def supprimer_depense():
    depense_id = 0
    while not depense_id or depense_id == 0:
        depense_id = input('Id de la dépense: ')
    Controlleur.supprimer_depense(depense_id)

def valider_choix(nb_options):
    '''
    Gere les entrees au clavier pour les menus.
    Boucle tant que l'entree n'est pas entre 0 et nb_options.
    Retourne l'entree fructueuse.
    '''
    options = [str(i) for i in range(nb_options)]
    choix = input("    Choix: ")
    while choix not in options:
        print("Entree invalide.")
        choix = input("    Choix: ")
    return(choix)

def is_float(number):
    try:
        float(number)
        return True
    except ValueError:
        return False

if __name__ == '__main__':
    menu_principal()