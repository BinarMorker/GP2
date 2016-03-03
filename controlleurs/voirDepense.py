from PyQt5.QtCore import QObject, pyqtSlot, pyqtSignal

class voirDepense:
	
	sauvegarder = pyqtSignal()

	def __init__(self, fenetrePrincipale):
		self.fenetre = fenetrePrincipale
		self.onglet = self.fenetre.ui.voirDepense
		self.fenetre.ui.voirDepenseBoutonsControle.accepted.connect(self.valider)
		self.fenetre.ui.voirDepenseBoutonsControle.rejected.connect(self.annuler)

	
	def activer(self, categorie):
		self.fenetre.ui.voirDepenseChampNom.setText("derp")
		self.fenetre.ui.voirDepenseChampDesc.setText("banana")
		self.fenetre.ui.onglets.setCurrentWidget(self.onglet)

	@pyqtSlot()
	def valider(self):
		print("dépense visualisée youpi")
		self.fenetre.ui.onglets.setCurrentWidget(self.fenetre.ui.ongletDepenses)
	
	@pyqtSlot()
	def annuler(self):
		self.fenetre.ui.onglets.setCurrentWidget(self.fenetre.ui.ongletDepenses)
		print(self.getNom())
		print(self.getDescription())
		
	def getNom(self):
		return self.fenetre.ui.voirDepenseChampNom.text()
	
	def getDescription(self):
		return self.fenetre.ui.voirDepenseChampDesc.document().toPlainText()

