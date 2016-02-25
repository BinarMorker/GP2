from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import QObject, pyqtSlot, pyqtSignal
from ui_test import Ui_MainWindow

class fenetrePrincipale(QMainWindow):

	supersignal = pyqtSignal()

	def creer(self):
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)
		self.ui.onglets.tabBar().hide()
		self.ui.boutonDepenses.clicked.connect(self.depenses)
		self.ui.boutonCategories.clicked.connect(self.categories)
		self.ui.boutonMembres.clicked.connect(self.membres)
		self.ui.boutonAjouterDepense.clicked.connect(self.ajouterDepense)
		self.ui.boutonEditerDepense.clicked.connect(self.modifierDepense)
		self.ui.boutonRetirerDepense.clicked.connect(self.supprimerDepense)
		self.ui.boutonAjouterCategorie.clicked.connect(self.ajouterCategorie)
		self.ui.boutonEditerCategorie.clicked.connect(self.modifierCategorie)
		self.ui.boutonRetirerCategorie.clicked.connect(self.supprimerCategorie)
		self.ui.boutonAjouterMembre.clicked.connect(self.ajouterMembre)
		self.ui.boutonEditerMembre.clicked.connect(self.modifierMembre)
		self.ui.boutonRetirerMembre.clicked.connect(self.supprimerMembre)

	@pyqtSlot()
	def derp(self):
		print("derp")
		self.supersignal.emit()

	@pyqtSlot()
	def depenses(self):
		self.ui.onglets.setCurrentWidget(self.ui.ongletDepenses)

	@pyqtSlot()
	def ajouterDepense(self):
		print("ajouter dépense")

	@pyqtSlot()
	def modifierDepense(self):
		print("modifier dépense")

	@pyqtSlot()
	def supprimerDepense(self):
		print("supprimer dépense")

	@pyqtSlot()
	def categories(self):
		self.ui.onglets.setCurrentWidget(self.ui.ongletCategories)

	@pyqtSlot()
	def ajouterCategorie(self):
		print("ajouter catégorie")

	@pyqtSlot()
	def modifierCategorie(self):
		print("ajouter catégorie")

	@pyqtSlot()
	def supprimerCategorie(self):
		print("ajouter catégorie")

	@pyqtSlot()
	def membres(self):
		self.ui.onglets.setCurrentWidget(self.ui.ongletMembres)

	@pyqtSlot()
	def ajouterMembre(self):
		print("ajouter membre")

	@pyqtSlot()
	def modifierMembre(self):
		print("ajouter membre")

	@pyqtSlot()
	def supprimerMembre(self):
		print("ajouter membre")
