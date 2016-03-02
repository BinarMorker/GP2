'''
@author: Marc-Antoine Renaud et François Allard
'''

from modeles.categorie import Categorie
from outils.basededonnees import *

class CategoriesControlleur:
	'''
	Le controlleur des catégories
	'''
	@staticmethod
	def liste_categories():
		'''
		Montre une liste des catégories
		'''
		categories = BaseDeDonnees.Instance().session.query(Categorie).all()
		return categories
		
	@staticmethod
	def voir_categorie(categorie_id):
		'''
		Affiche une catégorie
		@param categorie_id: L'identifiant de la catégorie à afficher
		'''
		categorie = BaseDeDonnees.Instance().session.query(Categorie).filter(Categorie.id == categorie_id).one()
		return categorie
		
	@staticmethod
	def ajouter_categorie(nom, description):
		'''
		Ajoute une catégorie
		@param nom: Le nom de la nouvelle catégorie
		'''
		categorie = Categorie()
		if nom.strip() == "":
			raise AssertionError
		categorie.nom = nom
		BaseDeDonnees.Instance().session.add(categorie)
		BaseDeDonnees.Instance().session.commit()
		return categorie
		
	@staticmethod
	def modifier_categorie(categorie_id, nom = None, description = None):
		'''
		Modifie une catégorie existante
		@param categorie_id: L'identifiant de la catégorie
		@param nom: Le nouveau nom de la catégorie
		'''
		categorie = BaseDeDonnees.Instance().session.query(Categorie).filter(Categorie.id == categorie_id).one()
		if nom != None:
			if nom.strip() == "":
				raise AssertionError
			categorie.nom = nom
		if description != None:
			if description.strip() == "":
				raise AssertionError
			categorie.description = description
		BaseDeDonnees.Instance().session.commit()
		return categorie
		
	@staticmethod
	def supprimer_categorie(categorie_id):
		'''
		Supprime une catégorie
		@param categorie_id: L'identifiant de la catégorie à supprimer
		'''
		categorie = BaseDeDonnees.Instance().session.query(Categorie).filter(Categorie.id == categorie_id).one()
		BaseDeDonnees.Instance().session.delete(categorie)
		BaseDeDonnees.Instance().session.commit()
		return categorie