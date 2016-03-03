from PyQt5.QtCore import QObject, pyqtSlot, pyqtSignal

class creerDepense:
	
	sauvegarder = pyqtSignal()

	def __init__(self, fenetrePrincipale):
		self.fenetre = fenetrePrincipale
		self.onglet = self.fenetre.ui.ajouterDepense
		self.fenetre.ui.creerDepBoutonsControle.accepted.connect(self.valider)
		self.fenetre.ui.creerDepBoutonsControle.rejected.connect(self.annuler)
	
	def activer(self):
		self.fenetre.ui.creerDepenseChampNom.setText("derp")
		self.fenetre.ui.creerDepenseChampDesc.setText("banana")
		self.fenetre.ui.onglets.setCurrentWidget(self.onglet)

	@pyqtSlot()
	def valider(self):
		print("nouvelle dépense créée youpi")
		self.fenetre.ui.onglets.setCurrentWidget(self.fenetre.ui.ongletDepenses)
	
	@pyqtSlot()
	def annuler(self):
		self.fenetre.ui.onglets.setCurrentWidget(self.fenetre.ui.ongletDepenses)
