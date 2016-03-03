from PyQt5.QtCore import QObject, pyqtSlot, pyqtSignal
from controlleurs.depenses import DepensesControlleur

class creerDepense:
	
	sauvegarder = pyqtSignal()

	def __init__(self, fenetrePrincipale):
		self.fenetre = fenetrePrincipale
		self.onglet = self.fenetre.ui.ajouterDepense
		self.fenetre.ui.creerDepBoutonsControle.accepted.connect(self.valider)
		self.fenetre.ui.creerDepBoutonsControle.rejected.connect(self.annuler)
	
	def activer(self):
		self.fenetre.ui.creerDepenseChampNom.setText("")
		self.fenetre.ui.creerDepenseChampDesc.setText("")
		self.fenetre.ui.onglets.setCurrentWidget(self.onglet)

	@pyqtSlot()
	def valider(self):
		print(str(self.fenetre.ui.creerDepenseChampNom.text()))
		print(str(self.fenetre.ui.creerDepenseSpinBoxMontant.value()))
		print(str(self.fenetre.ui.creerDepenseChampDesc.document().toPlainText()))
		try:
			DepensesControlleur.ajouter_depense(
				str(self.fenetre.ui.creerDepenseChampNom.text()), 
				self.fenetre.ui.creerDepenseSpinBoxMontant.value(), 
				1, 
				str(self.fenetre.ui.creerDepenseChampDesc.document().toPlainText())
			)
		except Exception as e:
			print(e.message)
		self.fenetre.ui.onglets.setCurrentWidget(self.fenetre.ui.ongletDepenses)
	
	@pyqtSlot()
	def annuler(self):
		self.fenetre.ui.onglets.setCurrentWidget(self.fenetre.ui.ongletDepenses)
