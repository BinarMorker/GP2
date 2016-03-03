from PyQt5.QtCore import QObject, pyqtSlot, pyqtSignal

class modifierDepense:
	
	sauvegarder = pyqtSignal()

	def __init__(self, fenetrePrincipale):
		self.fenetre = fenetrePrincipale
		self.onglet = self.fenetre.ui.editerDepense
		self.fenetre.ui.editerDepenseBoutonsControle.accepted.connect(self.valider)
		self.fenetre.ui.editerDepenseBoutonsControle.rejected.connect(self.annuler)

	def activer(self, depense):	
		self.fenetre.ui.onglets.setCurrentWidget(self.onglet)

	@pyqtSlot()
	def valider(self):
		print("dépense modifiée youpi")
		self.fenetre.ui.onglets.setCurrentWidget(self.fenetre.ui.ongletDepenses)
	
	@pyqtSlot()
	def annuler(self):
		self.fenetre.ui.onglets.setCurrentWidget(self.fenetre.ui.ongletDepenses)
		print(self.getNom())
		print(self.getDescription())
		
	def getNom(self):
		return self.fenetre.ui.editerCatChampNom.text()
	
	def getDescription(self):
		return self.fenetre.ui.editerCatChampDesc.document().toPlainText()