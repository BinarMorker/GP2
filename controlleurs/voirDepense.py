from PyQt5.QtCore import QObject, pyqtSlot, pyqtSignal
from controlleurs.depenses import DepensesControlleur

class voirDepense:
	
	sauvegarder = pyqtSignal()

	def __init__(self, fenetrePrincipale):
		self.fenetre = fenetrePrincipale
		self.onglet = self.fenetre.ui.voirDepense
		self.fenetre.ui.voirDepenseBoutonsControle.accepted.connect(self.valider)
		self.fenetre.ui.voirDepenseBoutonsControle.rejected.connect(self.annuler)
	
	def activer(self, categorie):
		depense = DepensesControlleur.voir_depense(1) #TODO: mettre le vrai ID
		self.fenetre.ui.voirDepenseChampNom.setText(depense.nom)
		self.fenetre.ui.voirDepenseChampCat.setText(depense.categorie.nom)
		self.fenetre.ui.voirDepenseChampDesc.setText(depense.description)
		self.fenetre.ui.voirDepenseSpinBoxMontant.setValue(depense.montant)
		self.fenetre.ui.onglets.setCurrentWidget(self.onglet)

	@pyqtSlot()
	def valider(self):
		self.fenetre.ui.onglets.setCurrentWidget(self.fenetre.ui.ongletDepenses)
	
	@pyqtSlot()
	def annuler(self):
		self.fenetre.ui.onglets.setCurrentWidget(self.fenetre.ui.ongletDepenses)