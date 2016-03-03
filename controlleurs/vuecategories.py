from PyQt5.QtCore import QObject, pyqtSlot, pyqtSignal
from controlleurs.creerCategorie import creerCategorie
from controlleurs.modifierCategorie import modifierCategorie
from controlleurs.voirCategorie import voirCategorie

class controleurCategories:

	sauvegarder = pyqtSignal()

	def __init__(self, fenetrePrincipale):
		self.fenetre = fenetrePrincipale
		self.controleurCreerCategorie = creerCategorie(self.fenetre)
		self.controleurModifierCategorie = modifierCategorie(self.fenetre)
		self.controleurVoirCategorie = voirCategorie(self.fenetre)
		self.fenetre.ui.boutonAjouterCategorie.clicked.connect(self.ajouter)
		self.fenetre.ui.boutonEditerCategorie.clicked.connect(self.modifier)
		self.fenetre.ui.boutonRetirerCategorie.clicked.connect(self.supprimer)
		self.fenetre.ui.boutonVoirCategorie.clicked.connect(self.voir)

	@pyqtSlot()
	def ajouter(self):
		self.controleurCreerCategorie.activer()

	@pyqtSlot()
	def modifier(self, categorie):
		self.controleurModifierCategorie.activer(categorie)

	@pyqtSlot()
	def voir(self, categorie):
		self.controleurVoirCategorie.activer(categorie)

	@pyqtSlot()	
	def supprimer(self, categorie):
		print("supprimer la catégorie yarr")
