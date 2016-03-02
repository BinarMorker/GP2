from PyQt5.QtCore import QObject, pyqtSlot, pyqtSignal

class supprimerCategorie:
	
	sauvegarder = pyqtSignal()

	def __init__(self, fenetrePrincipale):
		self.fenetre = fenetrePrincipale
		self.onglet = self.fenetre.ui.effacerCategorie
		self.fenetre.ui.effacerCatBoutonsControle.accepted.connect(self.valider)
		self.fenetre.ui.effacerCatBoutonsControle.rejected.connect(self.annuler)
		print("prout2")
	
	def activer(self):
		self.fenetre.ui.effacerCatChampNom.setText("derp")
		self.fenetre.ui.effacerCatChampDesc.setText("banana")
		self.fenetre.ui.onglets.setCurrentWidget(self.onglet)

	@pyqtSlot()
	def valider(self):
		print("catégorie supprimée youpi")
		self.fenetre.ui.onglets.setCurrentWidget(self.fenetre.ui.ongletCategories)
	
	@pyqtSlot()
	def annuler(self):
		self.fenetre.ui.onglets.setCurrentWidget(self.fenetre.ui.ongletCategories)
		print(self.getNom())
		print(self.getDescription())
		
	def getNom(self):
		return self.fenetre.ui.effacerCatChampNom.text()
	
	def getDescription(self):
		return self.fenetre.ui.effacerCatChampDesc.document().toPlainText()
