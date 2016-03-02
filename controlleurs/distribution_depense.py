'''
@author: Marc-Antoine Renaud et François Allard
'''

from modeles.distribution_depense import Distribution_Depense
from controlleurs.controlleur import Controlleur
from sqlalchemy.orm.exc import NoResultFound
from controlleurs.depenses import DepensesControlleur

class DistributionsDepensesControlleur(Controlleur):
    '''
    Le controlleur des distributions des dépenses
    '''

    def liste_distributions_depenses(self):
        '''
        Montre une liste des distributions des dépenses
        @attention: À venir
        '''
        try:
            distributions_depenses = self.session.query(Distribution_Depense).all()
            for distribution_depense in distributions_depenses:
                DepensesControlleur.voir_depense(self, distribution_depense.depense.id, distribution_depense.entite.id)
        except NoResultFound:
            print('Entrée introuvable')

    def liste_distributions_depenses_depense(self, depense_id):
        '''
        Montre une liste des distributions des dépenses
        @attention: À venir
        '''
        try:
            distributions_depenses = self.session.query(Distribution_Depense).all()
            for distribution_depense in distributions_depenses:
                DepensesControlleur.voir_depense(self, distribution_depense.depense.id, distribution_depense.entite.id)
        except NoResultFound:
            print('Entrée introuvable')

    def liste_distributions_depenses_entite(self, entite_id):
        '''
        Montre une liste des distributions des dépenses
        @attention: À venir
        '''
        try:
            distributions_depenses = self.session.query(Distribution_Depense).all()
            for distribution_depense in distributions_depenses:
                DepensesControlleur.voir_depense(self, distribution_depense.depense.id, distribution_depense.entite.id)
        except NoResultFound:
            print('Entrée introuvable')
        
    def voir_distribution_depense(self, depense_id, entite_id):
        '''
        Affiche une dépense
        @param depense_id: L'identifiant de la dépense à afficher
        '''
        try:
            distribution_depense = self.session.query(Distribution_Depense).filter(Distribution_Depense.id_depense == depense_id).filter(Distribution_Depense).one()
            print(str(distribution_depense.depense.id) + '\n' + 
                distribution_depense.entite.id + '\n' + 
                str(distribution_depense.pourcentage) + '\n' + 
                str(distribution_depense.montant_paye) + '\n' + 
                str(distribution_depense.montant_a_payer()) + '\n' + 
                str(distribution_depense.montant_total()) + '\n' + 
                str(distribution_depense.est_paye()))
        except NoResultFound:
            print('Entrée introuvable')
        
    def ajouter_distribution_depense(self, depense_id, membre_id, pourcentage=0, montant_paye=0.0):
        '''
        Ajoute une dépense
        @param nom: Le nom de la nouvelle dépense
        @param montant: Le montant de la nouvelle dépense
        @param id_categorie: La catégorie de la nouvelle distributions des dépenses
        @param description: La description de la nouvelle dépense
        '''
        try:
            distribution_depense = Distribution_Depense()
            distribution_depense.id_depense = depense_id
            distribution_depense.id_entite = membre_id
            if not pourcentage <= 0:
                raise AssertionError
            distribution_depense.pourcentage = pourcentage
            if not montant_paye.is_float() and not montant_paye <= 0:
                raise AssertionError
            distribution_depense.montant_paye = montant_paye
            self.session.commit()
            self.voir_distribution_depense(depense_id, membre_id)
            print('\nAjouté')
        except AssertionError:
            print('Le format est invalide')
        
    def modifier_distribution_depense(self, depense_id, membre_id, pourcentage=None, montant_paye=None):
        '''
        Modifie une dépense existante
        @param depense_id: L'identifiant de la dépense
        @param nom: Le nouveau nom de la dépense
        @param montant: Le nouveau montant de la dépense
        @param id_categorie: La nouvelle catégorie de la dépense
        @param description: La nouvelle description de la dépense
        '''
        try:
            distribution_depense = self.session.query(Distribution_Depense).filter(Distribution_Depense.id_depense == depense_id).filter(Distribution_Depense.id_membre == membre_id).one()
            if pourcentage != None:
                if pourcentage <= 0:
                    raise AssertionError
                distribution_depense.pourcentage = pourcentage
            if montant_paye != None:
                if not montant_paye.is_float() and montant_paye <= 0:
                    raise AssertionError
                distribution_depense.montant_paye = montant_paye
            self.session.commit()
            self.voir_distribution_depense(depense_id, membre_id)
            print('\nModifié')
        except AssertionError:
            print('Le format est invalide')
        except NoResultFound:
            print('Entrée introuvable')
        
    def supprimer_distribution_depense(self, depense_id, membre_id):
        '''
        Supprime une dépense
        @param depense_id: L'identifiant de la dépense à supprimer
        '''
        try:
            distribution_depense = self.session.query(Distribution_Depense).filter(Distribution_Depense.id_depense == depense_id).filter(Distribution_Depense.id_membre == membre_id).one()
            self.session.delete(distribution_depense)
            self.session.commit()
            self.voir_distribution_depense(depense_id, membre_id)
            print('\nSupprimé')
        except NoResultFound:
            print('Entrée introuvable')
