'''
@author: Marc-Antoine Renaud et François Allard
'''

from modeles.categorie import Categorie
from controlleurs.controlleur import Controlleur
from sqlalchemy.orm.exc import NoResultFound

class CategoriesControlleur(Controlleur):
	'''
	Le controlleur des catégories
	'''

	def liste_categories(self):
		'''
		Montre une liste des catégories
		@attention: À venir
		'''
		print('À venir')
		
	def voir_categorie(self, categorie_id):
		'''
		Affiche une catégorie
		@param categorie_id: L'identifiant de la catégorie à afficher
		'''
		try:
			categorie = self.session.query(Categorie).filter(Categorie.id == categorie_id).one()
			print(str(categorie.id) + '\n' + categorie.nom)
		except NoResultFound:
			print('Entrée introuvable')
		
	def ajouter_categorie(self, nom):
		'''
		Ajoute une catégorie
		@param nom: Le nom de la nouvelle catégorie
		'''
		try:
			categorie = Categorie()
			if nom.strip() == "":
				raise AssertionError
			categorie.nom = nom
			self.session.add(categorie)
			self.session.commit()
			print(str(categorie.id) + '\n' + categorie.nom)
		except AssertionError:
			print('Le format est invalide')
		
	def modifier_categorie(self, categorie_id, nom = None):
		'''
		Modifie une catégorie existante
		@param categorie_id: L'identifiant de la catégorie
		@param nom: Le nouveau nom de la catégorie
		'''
		try:
			categorie = self.session.query(Categorie).filter(Categorie.id == categorie_id).one()
			if nom != None:
				if nom.strip() == "":
					raise AssertionError
				categorie.nom = nom
			self.session.commit()
			print(str(categorie.id) + '\n' + categorie.nom)
		except AssertionError:
			print('Le format est invalide')
		except NoResultFound:
			print('Entrée introuvable')
		
	def supprimer_categorie(self, categorie_id):
		'''
		Supprime une catégorie
		@param categorie_id: L'identifiant de la catégorie à supprimer
		'''
		try:
			categorie = self.session.query(Categorie).filter(Categorie.id == categorie_id).one()
			self.session.delete(categorie)
			self.session.commit()
			print(str(categorie.id) + '\n' + categorie.nom + '\nSupprimé')
		except NoResultFound:
			print('Entrée introuvable')