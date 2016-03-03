from PyQt5.QtCore import QObject, pyqtSlot, pyqtSignal
from controlleurs.depenses import DepensesControlleur
from controlleurs.categories import CategoriesControlleur

class modifierDepense:
	
	sauvegarder = pyqtSignal()

	def __init__(self, fenetrePrincipale):
		self.fenetre = fenetrePrincipale
		self.onglet = self.fenetre.ui.editerDepense
		self.fenetre.ui.editerDepenseBoutonsControle.accepted.connect(self.valider)
		self.fenetre.ui.editerDepenseBoutonsControle.rejected.connect(self.annuler)

	def activer(self, depense):	
		depense = DepensesControlleur.voir_depense(1) #TODO: mettre le vrai ID
		self.fenetre.ui.editerDepenseChampNom.setText(depense.nom)
		self.fenetre.ui.editerDepenseComboBoxCat.model().clear()
		for categorie in CategoriesControlleur.liste_categories():
			self.fenetre.ui.editerDepenseComboBoxCat.addItem(categorie.nom, categorie.id)
		self.fenetre.ui.editerDepenseComboBoxCat.setCurrentText(depense.categorie.nom)
		self.fenetre.ui.editerDepenseChampDesc.setText(depense.description)
		self.fenetre.ui.editerDepenseSpinBoxMontant.setValue(depense.montant)
		self.fenetre.ui.onglets.setCurrentWidget(self.onglet)

	@pyqtSlot()
	def valider(self):
		DepensesControlleur.modifier_depense(
			1, #TODO: mettre le vrai ID
			self.getNom(), 
			self.getMontant(), 
			self.getCategorie(), 
			self.getDescription()
		)
		self.fenetre.ui.onglets.setCurrentWidget(self.fenetre.ui.ongletDepenses)
	
	@pyqtSlot()
	def annuler(self):
		self.fenetre.ui.onglets.setCurrentWidget(self.fenetre.ui.ongletDepenses)
		print(self.getNom())
		print(self.getDescription())
		
	def getNom(self):
		return self.fenetre.ui.editerDepenseChampNom.text()
	
	def getCategorie(self):
		return self.fenetre.ui.editerDepenseComboBoxCat.currentData()
	
	def getDescription(self):
		return self.fenetre.ui.editerDepenseChampDesc.document().toPlainText()

	def getMontant(self):
		return self.fenetre.ui.editerDepenseSpinBoxMontant.value()