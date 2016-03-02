'''
@author: Marc-Antoine Renaud et François Allard
'''

from modeles.depense import Depense
from controlleurs.controlleur import Controlleur
from sqlalchemy.orm.exc import NoResultFound
from outils.nombre import Nombre

class DepensesControlleur(Controlleur):
	'''
	Le controlleur des dépenses
	'''

	def liste_depenses(self):
		'''
		Montre une liste des dépenses
		@attention: À venir
		'''
		try:
			depenses = self.session.query(Depense).all()
			for depense in depenses:
				print(
					str(depense.id) + '\n' + 
					depense.nom + '\n' + 
					str(depense.montant) + '\n' + 
					depense.categorie.nom + '\n' + 
					depense.description + '\n-------')
				for distribution in depense.distributions:
					print(distribution.membre.nom + ': ' + str(distribution.pourcentage) + '\n--')
		except NoResultFound:
			print('Entrée introuvable')
		
	def voir_depense(self, depense_id):
		'''
		Affiche une dépense
		@param depense_id: L'identifiant de la dépense à afficher
		'''
		try:
			depense = self.session.query(Depense).filter(Depense.id == depense_id).one()
			print(str(depense.id) + '\n' + 
				depense.nom + '\n' + 
				str(depense.montant) + '\n' + 
				depense.categorie.nom + '\n' + 
				depense.description)
		except NoResultFound:
			print('Entrée introuvable')
		
	def ajouter_depense(self, nom, montant, id_categorie, description = ''):
		'''
		Ajoute une dépense
		@param nom: Le nom de la nouvelle dépense
		@param montant: Le montant de la nouvelle dépense
		@param id_categorie: La catégorie de la nouvelle dépenses
		@param description: La description de la nouvelle dépense
		'''
		try:
			depense = Depense()
			if nom.strip() == "":
				raise AssertionError
			depense.nom = nom
			if not Nombre.is_float(montant) or float(montant) <= 0:
				raise AssertionError
			depense.montant = montant
			depense.id_categorie = id_categorie
			depense.description = description
			self.session.add(depense)
			self.session.commit()
			print(str(depense.id) + '\n' + 
				depense.nom + '\n' + 
				str(depense.montant) + '\n' + 
				str(depense.categorie.nom) + '\n' + 
				depense.description)
		except AssertionError:
			print('Le format est invalide')
		
	def modifier_depense(self, depense_id, nom = None, montant = None, id_categorie = None, description = None):
		'''
		Modifie une dépense existante
		@param depense_id: L'identifiant de la dépense
		@param nom: Le nouveau nom de la dépense
		@param montant: Le nouveau montant de la dépense
		@param id_categorie: La nouvelle catégorie de la dépense
		@param description: La nouvelle description de la dépense
		'''
		try:
			depense = self.session.query(Depense).filter(Depense.id == depense_id).one()
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
			self.session.commit()
			print(str(depense.id) + '\n' + 
				depense.nom + '\n' + 
				str(depense.montant) + '\n' + 
				str(depense.categorie.nom) + '\n' + 
				depense.description)
		except AssertionError:
			print('Le format est invalide')
		except NoResultFound:
			print('Entrée introuvable')
		
	def supprimer_depense(self, depense_id):
		'''
		Supprime une dépense
		@param depense_id: L'identifiant de la dépense à supprimer
		'''
		try:
			depense = self.session.query(Depense).filter(Depense.id == depense_id).one()
			self.session.delete(depense)
			self.session.commit()
			print(str(depense.id) + '\n' + depense.nom + '\n' + str(depense.montant) + '\n' + depense.description + '\nSupprimé')
		except NoResultFound:
			print('Entrée introuvable')