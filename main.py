import sys
from controllers.depenses import DepensesControlleur as Controlleur

def menu_principal():
    '''Affiche le menu principal'''
    while True:
        print("Que voulez-vous faire?",
              "\n    1 - Voir d�penses"
              "\n    2 - Voir d�pense #"
              "\n    3 - Ajouter d�pense"
              "\n    4 - Modifier d�pense"
              "\n    5 - Supprimer d�pense"
              "\n    0 - Quitter")
        options = {'1': lambda: Controlleur.voir_depenses(),
        		   '2': lambda: voir_depense(),
        		   '3': lambda: Controlleur.ajouter_depense(),
        		   '4': lambda: modifier_depense(),
        		   '5': lambda: supprimer_depense(),
                   '0': lambda: sys.exit(0)}
        choix = valider_choix(len(options))
        options[choix]()
        print("")

def voir_depense():
	print('� venir')

def modifier_depense():
	print('� venir')

def supprimer_depense():
	print('� venir')

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

if __name__ == '__main__':
	menu_principal()