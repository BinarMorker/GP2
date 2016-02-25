'''
@author: Marc-Antoine Renaud, François Allard et Steve Lehoux
'''

from modeles.entite import Entite
from controlleurs.controlleur import Controlleur
from sqlalchemy.orm.exc import NoResultFound
from outils.nombre import Nombre



class EntitesControlleur(Controlleur):
	'''
	Le controlleur des entités
	'''

	def liste_entites(self):
		'''
		Montre une liste des entités
		@attention: À venir
		'''
		print('À venir')
		
	def voir_entite(self, entite_id):
		'''
		Affiche une entité
		@param entite_id: L'identifiant de l'entité à afficher
		'''
		try:
			entite = self.session.query(Entite).filter(Entite.id == entite_id).one()
			print(str(entite.id) + '\n' + entite.nom)
		except NoResultFound:
			print('Entrée introuvable')
		
	def ajouter_entite(self, nom):
		'''
		Ajoute une entité
		@param nom: Le nom de la nouvelle entité
		@param montant: Le montant de la nouvelle entité
		@param description: La description de la nouvelle entité
		'''
		try:
			entite = Entite()
			if nom.strip() == "":
				raise AssertionError
			entite.nom = nom
			self.session.add(entite)
			self.session.commit()
			print(str(entite.id) + '\n' + entite.nom)
		except AssertionError:
			print('Le format est invalide')
		
	def modifier_entite(self, entite_id, nom = None):
		'''
		Modifie une entité existante
		@param entite_id: L'identifiant de l'entité
		@param nom: Le nouveau nom de l'entité
		'''
		try:
			entite = self.session.query(Entite).filter(Entite.id == Entite_id).one()
			if nom != None:
				if nom.strip() == "":
					raise AssertionError
				entite.nom = nom
			self.session.commit()
			print(str(entite.id) + '\n' + entite.nom)
		except AssertionError:
			print('Le format est invalide')
		except NoResultFound:
			print('Entrée introuvable')
		
	def supprimer_entite(self, entite_id):
		'''
		Supprime une entité
		@param entite_id: L'identifiant de l'entité à supprimer
		'''
		try:
			entite = self.session.query(Entite).filter(Entite.id == entite_id).one()
			self.session.delete(entite)
			self.session.commit()
			print(str(entite.id) + '\n' + entite.nom + '\nSupprimé')
		except NoResultFound:
			print('Entrée introuvable')