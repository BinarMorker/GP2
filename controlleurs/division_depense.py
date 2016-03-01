'''
@author: Marc-Antoine Renaud et François Allard
'''

from modeles.division_depense import Division_Depense
from controlleurs.controlleur import Controlleur
from sqlalchemy.orm.exc import NoResultFound
from controlleurs.depenses import DepensesControlleur

class DivisionsDepensesControlleur(Controlleur):
    '''
    Le controlleur des divisions des dépenses
    '''

    def liste_divisions_depenses(self):
        '''
        Montre une liste des divisions des dépenses
        @attention: À venir
        '''
        try:
            divisions_depenses = self.session.query(Division_Depense).all()
            for division_depense in divisions_depenses:
                DepensesControlleur.voir_depense(self, division_depense.depense.id, division_depense.entite.id)
        except NoResultFound:
            print('Entrée introuvable')

    def liste_divisions_depenses_depense(self, depense_id):
        '''
        Montre une liste des divisions des dépenses
        @attention: À venir
        '''
        try:
            divisions_depenses = self.session.query(Division_Depense).all()
            for division_depense in divisions_depenses:
                DepensesControlleur.voir_depense(self, division_depense.depense.id, division_depense.entite.id)
        except NoResultFound:
            print('Entrée introuvable')

    def liste_divisions_depenses_entite(self, entite_id):
        '''
        Montre une liste des divisions des dépenses
        @attention: À venir
        '''
        try:
            divisions_depenses = self.session.query(Division_Depense).all()
            for division_depense in divisions_depenses:
                DepensesControlleur.voir_depense(self, division_depense.depense.id, division_depense.entite.id)
        except NoResultFound:
            print('Entrée introuvable')
        
    def voir_division_depense(self, depense_id, entite_id):
        '''
        Affiche une dépense
        @param depense_id: L'identifiant de la dépense à afficher
        '''
        try:
            division_depense = self.session.query(Division_Depense).filter(Division_Depense.id_depense == depense_id).filter(Division_Depense.id_entite == entite_id).one()
            print(str(division_depense.depense.id) + '\n' + 
                division_depense.entite.id + '\n' + 
                str(division_depense.pourcentage) + '\n' + 
                str(division_depense.montant_paye) + '\n' + 
                str(division_depense.montant_a_payer()) + '\n' + 
                str(division_depense.montant_total()) + '\n' + 
                str(division_depense.est_paye()))
        except NoResultFound:
            print('Entrée introuvable')
        
    def ajouter_division_depense(self, depense_id, entite_id, pourcentage = 0, montant_paye = 0.0):
        '''
        Ajoute une dépense
        @param nom: Le nom de la nouvelle dépense
        @param montant: Le montant de la nouvelle dépense
        @param id_categorie: La catégorie de la nouvelle divisions des dépenses
        @param description: La description de la nouvelle dépense
        '''
        try:
            division_depense = Division_Depense()
            division_depense.id_depense = depense_id
            division_depense.id_entite = entite_id
            if not pourcentage <= 0:
                raise AssertionError
            division_depense.pourcentage = pourcentage
            if not montant_paye.is_float() and not montant_paye <= 0:
                raise AssertionError
            division_depense.montant_paye = montant_paye
            self.session.commit()
            self.voir_division_depense(depense_id, entite_id)
            print('\nAjouté')
        except AssertionError:
            print('Le format est invalide')
        
    def modifier_division_depense(self, depense_id, entite_id, pourcentage = None, montant_paye = None):
        '''
        Modifie une dépense existante
        @param depense_id: L'identifiant de la dépense
        @param nom: Le nouveau nom de la dépense
        @param montant: Le nouveau montant de la dépense
        @param id_categorie: La nouvelle catégorie de la dépense
        @param description: La nouvelle description de la dépense
        '''
        try:
            division_depense = self.session.query(Division_Depense).filter(Division_Depense.id_depense == depense_id).filter(Division_Depense.id_entite == entite_id).one()
            if pourcentage != None:
                if pourcentage <= 0:
                    raise AssertionError
                division_depense.pourcentage = pourcentage
            if montant_paye != None:
                if not montant_paye.is_float() and montant_paye <= 0:
                    raise AssertionError
                division_depense.montant_paye = montant_paye
            self.session.commit()
            self.voir_division_depense(depense_id, entite_id)
            print('\nModifié')
        except AssertionError:
            print('Le format est invalide')
        except NoResultFound:
            print('Entrée introuvable')
        
    def supprimer_division_depense(self, depense_id, entite_id):
        '''
        Supprime une dépense
        @param depense_id: L'identifiant de la dépense à supprimer
        '''
        try:
            division_depense = self.session.query(Division_Depense).filter(Division_Depense.id_depense == depense_id).filter(Division_Depense.id_entite == entite_id).one()
            self.session.delete(division_depense)
            self.session.commit()
            self.voir_division_depense(depense_id, entite_id)
            print('\nSupprimé')
        except NoResultFound:
            print('Entrée introuvable')