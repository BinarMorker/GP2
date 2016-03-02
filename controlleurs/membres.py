'''
@author: Marc-Antoine Renaud, François Allard et Steve Lehoux
'''

from modeles.membre import Membre
from controlleurs.controlleur import Controlleur
from sqlalchemy.orm.exc import NoResultFound
from outils.nombre import Nombre



class MembresControlleur(Controlleur):
	'''
	Le controlleur des membre
	'''

	def liste_membres(self):
		'''
		Montre une liste des membre
		@attention: À venir
		'''
		try:
			membres = self.session.query(Membre).all()
			for membre in membres:
				print(str(membre.id) + '\n' + membre.nom + '\n-------')
				for distribution_depense in membre.distributions:
					print(str(distribution_depense.pourcentage) + '\n--')
		except NoResultFound:
			print('Entrée introuvable')
		
	def voir_membre(self, membre_id):
		'''
		Affiche un membre
		@param entite_id: L'identifiant du membre à afficher
		'''
		try:
			membre = self.session.query(Membre).filter(Membre.id == membre_id).one()
			print(str(membre.id) + '\n' + membre.nom)
		except NoResultFound:
			print('Entrée introuvable')
		
	def ajouter_membre(self, nom):
		'''
		Ajoute un membre
		@param nom: Le nom du nouveau membre
		@param montant: Le montant du nouveau membre
		@param description: La description du nouveau membre
		'''
		try:
			membre = Membre()
			if nom.strip() == "":
				raise AssertionError
			membre.nom = nom
			self.session.add(membre)
			self.session.commit()
			print(str(membre.id) + '\n' + membre.nom)
		except AssertionError:
			print('Le format est invalide')
		
	def modifier_membre(self, membre_id, nom = None):
		'''
		Modifie un membre existant
		@param membre_id: L'identifiant du membre
		@param nom: Le nouveau nom du membre
		'''
		try:
			membre = self.session.query(Membre).filter(Membre.id == membre_id).one()
			if nom != None:
				if nom.strip() == "":
					raise AssertionError
				membre.nom = nom
			self.session.commit()
			print(str(membre.id) + '\n' + membre.nom)
		except AssertionError:
			print('Le format est invalide')
		except NoResultFound:
			print('Entrée introuvable')
		
	def supprimer_membre(self, membre_id):
		'''
		Supprime une membre
		@param membre_id: L'identifiant du membre à supprimer
		'''
		try:
			membre = self.session.query(Membre).filter(Membre.id == membre_id).one()
			self.session.delete(membre)
			self.session.commit()
			print(str(membre.id) + '\n' + membre.nom + '\nSupprimé')
		except NoResultFound:
			print('Entrée introuvable')