from PyQt5.QtCore import QObject, pyqtSlot, pyqtSignal

class creerCategorie:

	def __init__(self, fenetrePrincipale):
		self.fenetre = fenetrePrincipale
		self.onglet = self.fenetre.ui.ajouterCategorie
		print("prout")
	
	def activer(self):
		self.fenetre.ui.creerCatChampNom.setText("derp")
		self.fenetre.ui.creerCatChampDesc.setText("banana")
		self.fenetre.ui.onglets.setCurrentWidget(self.onglet)

	#@pyqtSlot()
	#def depenses(self):
		#self.ui.onglets.setCurrentWidget(self.ui.ongletDepenses)
