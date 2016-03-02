from PyQt5.QtCore import QObject, pyqtSlot, pyqtSignal

class modifierCategorie:
	
	sauvegarder = pyqtSignal()

	def __init__(self, fenetrePrincipale):
		self.fenetre = fenetrePrincipale
		self.onglet = self.fenetre.ui.editerCategorie
		self.fenetre.ui.editerCatBoutonsControle.accepted.connect(self.valider)
		self.fenetre.ui.editerCatBoutonsControle.rejected.connect(self.annuler)
		print("prout2")
	
	def activer(self):
		self.fenetre.ui.editerCatChampNom.setText("derp")
		self.fenetre.ui.editerCatChampDesc.setText("banana")
		self.fenetre.ui.onglets.setCurrentWidget(self.onglet)

	@pyqtSlot()
	def valider(self):
		print("catégorie modifiée youpi")
		self.fenetre.ui.onglets.setCurrentWidget(self.fenetre.ui.ongletCategories)
	
	@pyqtSlot()
	def annuler(self):
		self.fenetre.ui.onglets.setCurrentWidget(self.fenetre.ui.ongletCategories)
		print(self.getNom())
		print(self.getDescription())
		
	def getNom(self):
		return self.fenetre.ui.editerCatChampNom.text()
	
	def getDescription(self):
		return self.fenetre.ui.editerCatChampDesc.document().toPlainText()
