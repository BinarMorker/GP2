'''
@author: Marc-Antoine Renaud et François Allard
'''

import sys
from controlleurs.depenses import DepensesControlleur
from outils.nombre import Nombre

def menu_principal(controlleur):
    '''
    Affiche le menu principal
    @param controlleur: Le controlleur à appeler
    '''
    while True:
        print("Que voulez-vous faire?",
              "\n    1 - Voir dépenses"
              "\n    2 - Voir dépense #"
              "\n    3 - Ajouter dépense"
              "\n    4 - Modifier dépense"
              "\n    5 - Supprimer dépense"
              "\n    0 - Quitter")
        options = {'1': lambda: controlleur.liste_depenses(),
        		   '2': lambda: voir_depense(controlleur),
        		   '3': lambda: ajouter_depense(controlleur),
        		   '4': lambda: modifier_depense(controlleur),
        		   '5': lambda: supprimer_depense(controlleur),
                   '0': lambda: sys.exit(0)}
        choix = valider_choix(len(options))
        options[choix]()
        print("")

def voir_depense(controlleur):
    '''
    Affiche le formulaire d'affichage d'une dépense
    @param controlleur: Le controlleur à appeler
    '''
    depense_id = 0
    while not depense_id or depense_id == 0:
        depense_id = input('Id de la dépense: ')
    controlleur.voir_depense(depense_id)

def modifier_depense(controlleur):
    '''
    Affiche le formulaire de modification d'une dépense
    @param controlleur: Le controlleur à appeler
    '''
    depense_id = 0
    while not depense_id or depense_id == 0:
        depense_id = input('Id de la dépense: ')
    depense_nom = input("Nom de la dépense (0 si aucun changement): ")
    if depense_nom == '0':
        depense_nom = None
    depense_montant = input('Montant de la dépense (0 si aucun changement): ')
    if depense_montant == '0' or not Nombre.is_float(depense_montant):
        depense_montant = None
    depense_description = input('Description de la dépense (0 si aucun changement): ')
    if depense_description == '0':
        depense_description = None
    controlleur.modifier_depense(depense_id, depense_nom, depense_montant, depense_description)
    
def ajouter_depense(controlleur):
    '''
    Affiche le formulaire d'ajout d'une dépense
    @param controlleur: Le controlleur à appeler
    '''
    depense_nom = ""
    depense_montant = 0.0
    while not depense_nom or depense_nom.strip() == "":
        depense_nom = input("Nom de la dépense: ")
    while not depense_montant or depense_montant == 0 or not Nombre.is_float(depense_montant):
        depense_montant = input('Montant de la dépense: ')
    depense_description = input('Description de la dépense (Entrée si aucune): ')
    controlleur.ajouter_depense(depense_nom, depense_montant, depense_description)

def supprimer_depense(controlleur):
    '''
    Affiche le formulaire de suppression d'une dépense
    @param controlleur: Le controlleur à appeler
    '''
    depense_id = 0
    while not depense_id or depense_id == 0:
        depense_id = input('Id de la dépense: ')
    controlleur.supprimer_depense(depense_id)

def valider_choix(nb_options):
    '''
    Gere les entrees au clavier pour les menus.
    Boucle tant que l'entree n'est pas entre 0 et nb_options.
    @param nb_options: Le nombre d'options
    @return: L'entree fructueuse.
    '''
    options = [str(i) for i in range(nb_options)]
    choix = input("    Choix: ")
    while choix not in options:
        print("Entree invalide.")
        choix = input("    Choix: ")
    return(choix)

if __name__ == '__main__':
    controlleur = DepensesControlleur()
    menu_principal(controlleur)
    