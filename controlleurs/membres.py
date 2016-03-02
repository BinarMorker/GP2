'''
@author: Marc-Antoine Renaud, François Allard et Steve Lehoux
'''

from modeles.membre import Membre
from outils.basededonnees import *

class MembresControlleur(Controlleur):
	'''
	Le controlleur des membre
	'''
	@staticmethod
	def liste_membres():
		'''
		Montre une liste des membre
		@attention: À venir
		'''
		membres = BaseDeDonnees.Instance().session.query(Membre).all()
		return membres
	
	@staticmethod
	def voir_membre(membre_id):
		'''
		Affiche un membre
		@param membre_id: L'identifiant du membre à afficher
		'''
		membre = BaseDeDonnees.Instance().session.query(Membre).filter(Membre.id == membre_id).one()
		return membre		
	
	@staticmethod
	def ajouter_membre(nom):
		'''
		Ajoute un membre
		@param nom: Le nom du nouveau membre
		'''
		membre = Membre()
		if nom.strip() == "":
			raise AssertionError
		membre.nom = nom
		BaseDeDonnees.Instance().session.add(membre)
		BaseDeDonnees.Instance().session.commit()
		return membre
	
	@staticmethod
	def modifier_membre(membre_id, nom = None):
		'''
		Modifie un membre existant
		@param membre_id: L'identifiant du membre
		@param nom: Le nouveau nom du membre
		'''
		membre = BaseDeDonnees.Instance().session.query(Membre).filter(Membre.id == membre_id).one()
		if nom != None:
			if nom.strip() == "":
				raise AssertionError
			membre.nom = nom
		BaseDeDonnees.Instance().session.commit()
		return membre
	
	@staticmethod
	def supprimer_membre(membre_id):
		'''
		Supprime une membre
		@param membre_id: L'identifiant du membre à supprimer
		'''
		membre = BaseDeDonnees.Instance().session.query(Membre).filter(Membre.id == membre_id).one()
		BaseDeDonnees.Instance().session.delete(membre)
		BaseDeDonnees.Instance().session.commit()
		return membre
