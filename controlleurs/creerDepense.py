from PyQt5.QtCore import QObject, pyqtSlot, pyqtSignal
from controlleurs.depenses import DepensesControlleur
from controlleurs.categories import CategoriesControlleur

class creerDepense:
	
	sauvegarder = pyqtSignal()

	def __init__(self, fenetrePrincipale):
		self.fenetre = fenetrePrincipale
		self.onglet = self.fenetre.ui.ajouterDepense
		self.fenetre.ui.creerDepenseBoutonsControle.accepted.connect(self.valider)
		self.fenetre.ui.creerDepenseBoutonsControle.rejected.connect(self.annuler)
	
	def activer(self):
		self.fenetre.ui.creerDepenseChampNom.setText("")
		self.fenetre.ui.creerDepenseComboBoxCat.model().clear()
		for categorie in CategoriesControlleur.liste_categories():
			self.fenetre.ui.creerDepenseComboBoxCat.addItem(categorie.nom, categorie.id)
		self.fenetre.ui.creerDepenseChampDesc.setText("")
		self.fenetre.ui.creerDepenseSpinBoxMontant.setValue(0)
		self.fenetre.ui.onglets.setCurrentWidget(self.onglet)

	@pyqtSlot()
	def valider(self):
		DepensesControlleur.ajouter_depense(
			self.getNom(), 
			self.getMontant(), 
			self.getCategorie(), 
			self.getDescription()
		)
		self.fenetre.ui.onglets.setCurrentWidget(self.fenetre.ui.ongletDepenses)
	
	@pyqtSlot()
	def annuler(self):
		print("annuler")
		self.fenetre.ui.onglets.setCurrentWidget(self.fenetre.ui.ongletDepenses)
		
	def getNom(self):
		return self.fenetre.ui.creerDepenseChampNom.text()
	
	def getCategorie(self):
		return self.fenetre.ui.creerDepenseComboBoxCat.currentData()
	
	def getDescription(self):
		return self.fenetre.ui.creerDepenseChampDesc.document().toPlainText()

	def getMontant(self):
		return self.fenetre.ui.creerDepenseSpinBoxMontant.value()
