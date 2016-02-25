'''
@author: Marc-Antoine Renaud et François Allard
'''

import sys
from controlleurs.depenses import DepensesControlleur
from controlleurs.entites import EntitesControlleur
from controlleurs.categories import CategoriesControlleur
from outils.nombre import Nombre

def menu_principal():
    '''
    Affiche le menu principal
    '''
    depensescontrolleur = DepensesControlleur()
    entitescontrolleur = EntitesControlleur()
    categoriescontrolleur = CategoriesControlleur()
    
    while True:
        print("Que voulez-vous faire?",
              "\n    1 - Menu dépenses"
              "\n    2 - Menu entités"
              "\n    3 - Menu catégories"
              "\n    0 - Quitter")
        options = {'1': lambda: menu_depenses(depensescontrolleur),
                   '2': lambda: menu_entites(entitescontrolleur),
                   '3': lambda: menu_categories(categoriescontrolleur),
                   '0': lambda: sys.exit(0)}
        choix = valider_choix(len(options))
        options[choix]()
        print("")

def menu_depenses(controlleur):
    '''
    Affiche le menu des dépenses
    @param controlleur: Le controlleur à appeler
    '''
    choix = True
    while choix != '0':
        print("Que voulez-vous faire?",
              "\n    1 - Voir dépenses"
              "\n    2 - Voir dépense #"
              "\n    3 - Ajouter dépense"
              "\n    4 - Modifier dépense"
              "\n    5 - Supprimer dépense"
              "\n    0 - Retour")
        options = {'1': lambda: controlleur.liste_depenses(),
                   '2': lambda: voir_depense(controlleur),
                   '3': lambda: ajouter_depense(controlleur),
                   '4': lambda: modifier_depense(controlleur),
                   '5': lambda: supprimer_depense(controlleur),
                   '0': lambda: False}
        choix = valider_choix(len(options))
        options[choix]()
        print("")

def menu_entites(controlleur):
    '''
    Affiche le menu des entités
    @param controlleur: Le controlleur à appeler
    '''
    choix = True
    while choix != '0':
        print("Que voulez-vous faire?",
              "\n    1 - Voir entités"
              "\n    0 - Retour")
        options = {'1': lambda: controlleur.liste_entites(),
                   '0': lambda: False}
        choix = valider_choix(len(options))
        options[choix]()
        print("")

def menu_categories(controlleur):
    '''
    Affiche le menu des catégories
    @param controlleur: Le controlleur à appeler
    '''
    choix = True
    while choix != '0':
        print("Que voulez-vous faire?",
              "\n    1 - Voir catégories"
              "\n    2 - Voir catégorie #"
              "\n    3 - Ajouter catégorie"
              "\n    4 - Modifier catégorie"
              "\n    5 - Supprimer catégorie"
              "\n    0 - Retour")
        options = {'1': lambda: controlleur.liste_categories(),
                   '2': lambda: voir_categorie(controlleur),
                   '3': lambda: ajouter_categorie(controlleur),
                   '4': lambda: modifier_categorie(controlleur),
                   '5': lambda: supprimer_categorie(controlleur),
                   '0': lambda: False}
        choix = valider_choix(len(options))
        options[choix]()
        print("")
        
def voir_categorie(controlleur):
    '''
    Affiche le formulaire d'affichage d'une catégorie
    @param controlleur: Le controlleur à appeler
    '''
    categorie_id = 0
    while not categorie_id or categorie_id == 0:
        categorie_id = input('Id de la catégorie: ')
    controlleur.voir_categorie(categorie_id)
    
def modifier_categorie(controlleur):
    '''
    Affiche le formulaire de modification d'une catégorie
    @param controlleur: Le controlleur à appeler
    '''
    categorie_id = 0
    while not categorie_id or categorie_id == 0:
        categorie_id = input('Id de la catégorie: ')
    categorie_nom = input("Nom de la catégorie (0 si aucun changement): ")
    if categorie_nom == '0':
        categorie_nom = None
    #categorie_description = input('Description de la catégorie (0 si aucun changement): ')
    #if categorie_description == '0':
    #    categorie_description = None
    controlleur.modifier_categorie(categorie_id, categorie_nom)
    
    
def ajouter_categorie(controlleur):
    '''
    Affiche le formulaire d'ajout d'une catégorie
    @param controlleur: Le controlleur à appeler
    '''
    categorie_nom = ""
    while not categorie_nom or categorie_nom.strip() == "":
        categorie_nom = input("Nom de la catégorie: ")
    controlleur.ajouter_categorie(categorie_nom)

def supprimer_categorie(controlleur):
    '''
    Affiche le formulaire de suppression d'une catégorie
    @param controlleur: Le controlleur à appeler
    '''
    categorie_id = 0
    while not categorie_id or categorie_id == 0:
        categorie_id = input('Id de la catégorie: ')
    controlleur.supprimer_categorie(categorie_id)

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
    menu_principal()
    