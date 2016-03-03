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
	def modifier(self, depense):
		self.controleurModifierDepense.activer(depense)

	@pyqtSlot()
	def voir(self, depense):
		self.controleurVoirDepense.activer(depense)

	@pyqtSlot()	
	def supprimer(self, depense):
		print("supprimer la dépense yarr")
