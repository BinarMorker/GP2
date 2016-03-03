from PyQt5.QtCore import QObject, pyqtSlot, pyqtSignal
from controlleurs.creerDepense import creerDepense
from controlleurs.modifierDepense import modifierDepense
from controlleurs.voirDepense import voirDepense

class controleurDepenses:

	sauvegarder = pyqtSignal()

	def __init__(self, fenetrePrincipale):
		self.fenetre = fenetrePrincipale
		self.controleurCreerDepense = creerDepense(self.fenetre)
		self.controleurModifierDepense = modifierDepense(self.fenetre)
		self.controleurVoirDepense = voirDepense(self.fenetre)
		self.ui.boutonAjouterDepense.clicked.connect(self.ajouterDepense)
		self.ui.boutonEditerDepense.clicked.connect(self.modifierDepense)
		self.ui.boutonRetirerDepense.clicked.connect(self.supprimerDepense)
		self.ui.boutonVoirDepense.clicked.connect(self.voirDepense)

	@pyqtSlot()
	def ajouter(self):
		self.controleurCreerDepense.activer()

	@pyqtSlot()
	def modifier(self, depense):
		self.controleurModifierDepense.activer(depense)

	@pyqtSlot()
	def voir(self, depense):
		self.controleurVoirDepense.activer(depense)

	@pyqtSlot()	
	def supprimer(self, depense):
		print("supprimer la catégorie yarr")
