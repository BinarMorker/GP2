from PyQt5.QtCore import QObject, pyqtSlot, pyqtSignal

class creerCategorie:
	
	sauvegarder = pyqtSignal()

	def __init__(self, fenetrePrincipale):
		self.fenetre = fenetrePrincipale
		self.onglet = self.fenetre.ui.ajouterCategorie
		self.fenetre.ui.creerCatBoutonsControle.accepted.connect(self.valider)
		self.fenetre.ui.creerCatBoutonsControle.rejected.connect(self.annuler)
	
	def activer(self):
		self.fenetre.ui.creerCatChampNom.setText("derp")
		self.fenetre.ui.creerCatChampDesc.setText("banana")
		self.fenetre.ui.onglets.setCurrentWidget(self.onglet)

	@pyqtSlot()
	def valider(self):
		print("nouvelle catégorie créée youpi")
		self.fenetre.ui.onglets.setCurrentWidget(self.fenetre.ui.ongletCategories)
	
	@pyqtSlot()
	def annuler(self):
		self.fenetre.ui.onglets.setCurrentWidget(self.fenetre.ui.ongletCategories)
		print(self.getNom())
		print(self.getDescription())
		
	def getNom(self):
		return self.fenetre.ui.creerCatChampNom.text()
	
	def getDescription(self):
		return self.fenetre.ui.creerCatChampDesc.document().toPlainText()
