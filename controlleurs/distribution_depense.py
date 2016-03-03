'''
@author: Marc-Antoine Renaud et François Allard
'''

from modeles.distribution_depense import Distribution_Depense
from outils.basededonnees import *

class DistributionsDepensesControlleur:
    '''
    Le controlleur des distributions des dépenses
    '''

    @staticmethod
    def liste_distributions_depenses():
        '''
        Montre une liste des distributions des dépenses
        @attention: À venir
        '''
        distributions_depenses = BaseDeDonnees.Instance().session.query(Distribution_Depense).all()
        return distributions_depenses
         
    @staticmethod       
    def liste_distributions_depenses_depense(depense_id):
        '''
        Montre une liste des distributions des dépenses
        @attention: À venir
        '''
        distributions_depenses = BaseDeDonnees.Instance().query(Distribution_Depense).filter(Distribution_Depense.id_depense == depense_id).filter(Distribution_Depense).all()
        return distributions_depenses

    @staticmethod
    def liste_distributions_depenses_entite(membre_id):
        '''
        Montre une liste des distributions des dépenses
        @attention: À venir
        '''
        distributions_depenses = BaseDeDonnees.Instance().session.query(Distribution_Depense).filter(Distribution_Depense.id_membre == membre_id).filter(Distribution_Depense).all()
        return distributions_depenses
        
    @staticmethod
    def voir_distribution_depense(self, depense_id, membre_id):
        '''
        Affiche une dépense
        @param depense_id: L'identifiant de la dépense à afficher
        '''
        distribution_depense = self.session.query(Distribution_Depense).filter(Distribution_Depense.id_depense == depense_id).filter(Distribution_Depense).one()
        return distribution_depense
        
    @staticmethod
    def ajouter_distribution_depense(depense_id, membre_id, pourcentage=0, montant_paye=0.0):
        '''
        Ajoute une dépense
        @param nom: Le nom de la nouvelle dépense
        @param montant: Le montant de la nouvelle dépense
        @param id_categorie: La catégorie de la nouvelle distributions des dépenses
        @param description: La description de la nouvelle dépense
        '''
        distribution_depense = Distribution_Depense()
        distribution_depense.id_depense = depense_id
        distribution_depense.id_membre = membre_id
        if not pourcentage <= 0:
            raise AssertionError
        distribution_depense.pourcentage = pourcentage
        if not montant_paye.is_float() and not montant_paye <= 0:
            raise AssertionError
        distribution_depense.montant_paye = montant_paye
        BaseDeDonnees.Instance().session.add(distribution_depense)
        BaseDeDonnees.Instance().session.commit()
        return distribution_depense
        
    @staticmethod
    def modifier_distribution_depense(depense_id, membre_id, pourcentage=None, montant_paye=None):
        '''
        Modifie une dépense existante
        @param depense_id: L'identifiant de la dépense
        @param nom: Le nouveau nom de la dépense
        @param montant: Le nouveau montant de la dépense
        @param id_categorie: La nouvelle catégorie de la dépense
        @param description: La nouvelle description de la dépense
        '''
        distribution_depense = BaseDeDonnees.Instance().session.query(Distribution_Depense).filter(Distribution_Depense.id_depense == depense_id).filter(Distribution_Depense.id_membre == membre_id).one()
        if pourcentage != None:
            if pourcentage <= 0:
                raise AssertionError
            distribution_depense.pourcentage = pourcentage
        if montant_paye != None:
            if not montant_paye.is_float() and montant_paye <= 0:
                raise AssertionError
            distribution_depense.montant_paye = montant_paye
        BaseDeDonnees.Instance().session.add(distribution_depense)
        BaseDeDonnees.Instance().session.commit()
        return distribution_depense
        
    @staticmethod
    def supprimer_distribution_depense(depense_id, membre_id):
        '''
        Supprime une dépense
        @param depense_id: L'identifiant de la dépense à supprimer
        '''
        distribution_depense = BaseDeDonnees.Instance().query(Distribution_Depense).filter(Distribution_Depense.id_depense == depense_id).filter(Distribution_Depense.id_membre == membre_id).one()
        BaseDeDonnees.Instance().session.delete(distribution_depense)
        BaseDeDonnees.Instance().session.commit()
