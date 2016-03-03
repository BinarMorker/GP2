from PyQt5.QtCore import QObject, pyqtSlot, pyqtSignal
from controlleurs.creerDepense import creerDepense
from controlleurs.modifierDepense import modifierDepense
from controlleurs.voirDepense import voirDepense
from controlleurs.depenses import DepensesControlleur as controleur_depenses

class controleurVueDepenses:

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
		# depenses = controleur_depenses.liste_depenses()
		# for depense in depenses:
		# 	print(depense.nom)

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
