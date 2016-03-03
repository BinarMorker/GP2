'''
@author: Marc-Antoine Renaud et François Allard
'''

from modeles.depense import Depense
from outils.nombre import Nombre
from outils.basededonnees import *

class DepensesControlleur:
	'''
	Le controlleur des dépenses
	'''

	@staticmethod
	def liste_depenses():
		'''
		Montre une liste des dépenses
		@attention: À venir
		'''
		depenses = BaseDeDonnees.Instance().session.query(Depense).all()
		return depenses
		
	@staticmethod
	def voir_depense(depense_id):
		'''
		Affiche une dépense
		@param depense_id: L'identifiant de la dépense à afficher
		'''
		depense = BaseDeDonnees.Instance().session.query(Depense).filter(Depense.id == depense_id).one()
		return depense
		
	@staticmethod
	def ajouter_depense(nom, montant, id_categorie, description = ''):
		'''
		Ajoute une dépense
		@param nom: Le nom de la nouvelle dépense
		@param montant: Le montant de la nouvelle dépense
		@param id_categorie: La catégorie de la nouvelle dépenses
		@param description: La description de la nouvelle dépense
		'''
		depense = Depense()
		if nom.strip() == "":
			raise AssertionError("La dépense doit avoir un nom")
		depense.nom = nom
		if not Nombre.is_float(montant) or float(montant) <= 0:
			raise AssertionError("Le montant de la dépense ne peut pas être nul")
		depense.montant = montant
		depense.id_categorie = id_categorie
		depense.description = description
		BaseDeDonnees.Instance().session.add(depense)
		BaseDeDonnees.Instance().session.commit()
		return depense
		
	@staticmethod
	def modifier_depense(depense_id, nom = None, montant = None, id_categorie = None, description = None):
		'''
		Modifie une dépense existante
		@param depense_id: L'identifiant de la dépense
		@param nom: Le nouveau nom de la dépense
		@param montant: Le nouveau montant de la dépense
		@param id_categorie: La nouvelle catégorie de la dépense
		@param description: La nouvelle description de la dépense
		'''
		depense = BaseDeDonnees.Instance().session.query(Depense).filter(Depense.id == depense_id).one()
		if nom != None:
			if nom.strip() == "":
				raise AssertionError
			depense.nom = nom
		if montant != None:
			if not Nombre.is_float(montant) or montant <= 0:
				raise AssertionError
			depense.montant = montant
		if id_categorie != None:
			depense.id_categorie = id_categorie
		if description != None:
			depense.description = description
		BaseDeDonnees.Instance().session.commit()
		return depense
		
	@staticmethod
	def supprimer_depense(depense_id):
		'''
		Supprime une dépense
		@param depense_id: L'identifiant de la dépense à supprimer
		'''
		depense = BaseDeDonnees.Instance().session.query(Depense).filter(Depense.id == depense_id).one()
		BaseDeDonnees.Instance().session.delete(depense)
		BaseDeDonnees.Instance().session.commit()
		return depense
