'''
@author: Marc-Antoine Renaud et François Allard
'''

from modeles.entite import Entite
from controlleurs.controlleur import Controlleur
from sqlalchemy.orm.exc import NoResultFound

class EntitesControlleur(Controlleur):
	'''
	Le controlleur des entités
	'''

	def liste_entites(self):
		'''
		Montre une liste des entités
		@attention: À venir
		'''
		try:
			entites = self.session.query(Entite).all()
			for entite in entites:
				print(str(entite.id) + '\n' + entite.nom + '\n-------')
				for division_depense in entite.division_depenses:
					print(str(division_depense.pourcentage) + '\n--')
		except NoResultFound:
			print('Entrée introuvable')