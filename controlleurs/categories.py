'''
@author: Marc-Antoine Renaud et François Allard
'''

from modeles.categorie import Categorie
from controlleurs.controlleur import Controlleur
from sqlalchemy.orm.exc import NoResultFound

class CategoriesControlleur(Controlleur):
	'''
	Le controlleur des entités
	'''

	def liste_categories(self):
		'''
		Montre une liste des entités
		@attention: À venir
		'''
		try:
			categories = self.session.query(Categorie).all()
			for categorie in categories:
				print(str(categorie.id) + '\n' + 
					categorie.nom + '\n-------')
				for depense in categorie.depenses:
					print(depense.nom + '\n--')
		except NoResultFound:
			print('Entrée introuvable')