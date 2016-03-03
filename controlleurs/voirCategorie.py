from PyQt5.QtCore import QObject, pyqtSlot, pyqtSignal

class voirCategorie:
	
	sauvegarder = pyqtSignal()

	def __init__(self, fenetrePrincipale):
		self.fenetre = fenetrePrincipale
		self.onglet = self.fenetre.ui.voirCategorie
		self.fenetre.ui.voirCatBoutonsControle.accepted.connect(self.valider)
		self.fenetre.ui.voirCatBoutonsControle.rejected.connect(self.annuler)
	
	def activer(self, categorie):
		self.fenetre.ui.voirCatChampNom.setText("derp")
		self.fenetre.ui.voirCatChampDesc.setText("banana")
		self.fenetre.ui.onglets.setCurrentWidget(self.onglet)

	@pyqtSlot()
	def valider(self):
		print("catégorie visualisée youpi")
		self.fenetre.ui.onglets.setCurrentWidget(self.fenetre.ui.ongletCategories)
	
	@pyqtSlot()
	def annuler(self):
		self.fenetre.ui.onglets.setCurrentWidget(self.fenetre.ui.ongletCategories)
		print(self.getNom())
		print(self.getDescription())
		
	def getNom(self):
		return self.fenetre.ui.voirCatChampNom.text()
	
	def getDescription(self):
		return self.fenetre.ui.voirCatChampDesc.document().toPlainText()
