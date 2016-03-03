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
		self.fenetre.ui.boutonAjouterDepense.clicked.connect(self.ajouter)
		self.fenetre.ui.boutonEditerDepense.clicked.connect(self.modifier)
		self.fenetre.ui.boutonRetirerDepense.clicked.connect(self.supprimer)
		self.fenetre.ui.boutonVoirDepense.clicked.connect(self.voir)

	@pyqtSlot()
	def activer(self):
		self.fenetre.ui.onglets.setCurrentWidget(self.fenetre.ui.ongletDepenses)

	@pyqtSlot()
	def ajouter(self):
		self.controleurCreerDepense.activer()

	@pyqtSlot()
	def modifier(self, categorie):
		self.controleurModifierDepense.activer(categorie)

	@pyqtSlot()
	def voir(self, categorie):
		self.controleurVoirDepense.activer(categorie)

	@pyqtSlot()
	def supprimer(self, categorie):
		print("supprimer la dépense yarr")
