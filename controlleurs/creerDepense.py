from PyQt5.QtCore import QObject, pyqtSlot, pyqtSignal
from controlleurs.depenses import DepensesControlleur

class creerDepense:
	
	sauvegarder = pyqtSignal()

	def __init__(self, fenetrePrincipale):
		self.fenetre = fenetrePrincipale
		self.onglet = self.fenetre.ui.ajouterDepense
		self.fenetre.ui.creerDepenseBoutonsControle.accepted.connect(self.valider)
		self.fenetre.ui.creerDepenseBoutonsControle.rejected.connect(self.annuler)
	
	def activer(self):
		self.fenetre.ui.creerDepenseChampNom.setText("")
		self.fenetre.ui.creerDepenseChampDesc.setText("")
		self.fenetre.ui.creerDepenseChampMontant.value(0)
		self.fenetre.ui.onglets.setCurrentWidget(self.onglet)

	@pyqtSlot()
	def valider(self):

		print(str(self.fenetre.ui.creerDepenseChampNom.text()))
		print(str(self.fenetre.ui.creerDepenseSpinBoxMontant.value()))
		print(str(self.fenetre.ui.creerDepenseChampDesc.document().toPlainText()))
		DepensesControlleur.ajouter_depense(
			str(self.fenetre.ui.creerDepenseChampNom.text()), 
			self.fenetre.ui.creerDepenseSpinBoxMontant.value(), 
			1, 
			str(self.fenetre.ui.creerDepenseChampDesc.document().toPlainText())
		)
		self.fenetre.ui.onglets.setCurrentWidget(self.fenetre.ui.ongletDepenses)
	
	@pyqtSlot()
	def annuler(self):
		print("annuler")
		self.fenetre.ui.onglets.setCurrentWidget(self.fenetre.ui.ongletDepenses)
		
	def getNom(self):
		return self.fenetre.ui.creerDepenseChampNom.text()
	
	def getDescription(self):
		return self.fenetre.ui.creerDepenseChampDesc.document().toPlainText()

	def getMontant(self):
		return self.fenetre.ui.creerDepenseChampMontant.value()
