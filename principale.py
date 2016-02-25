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
		self.ui.boutonVoirDepense.clicked.connect(self.voirDepense)
		self.ui.boutonAjouterCategorie.clicked.connect(self.ajouterCategorie)
		self.ui.boutonEditerCategorie.clicked.connect(self.modifierCategorie)
		self.ui.boutonRetirerCategorie.clicked.connect(self.supprimerCategorie)
		self.ui.boutonVoirCategorie.clicked.connect(self.voirCategorie)
		self.ui.boutonAjouterMembre.clicked.connect(self.ajouterMembre)
		self.ui.boutonEditerMembre.clicked.connect(self.modifierMembre)
		self.ui.boutonRetirerMembre.clicked.connect(self.supprimerMembre)
		self.ui.boutonVoirMembre.clicked.connect(self.voirMembre)

	@pyqtSlot()
	def derp(self):
		print("derp")
		self.supersignal.emit()

	@pyqtSlot()
	def depenses(self):
		self.ui.onglets.setCurrentWidget(self.ui.ongletDepenses)

	@pyqtSlot()
	def ajouterDepense(self):
		self.ui.onglets.setCurrentWidget(self.ui.ajouterDepense)

	@pyqtSlot()
	def modifierDepense(self):
		self.ui.onglets.setCurrentWidget(self.ui.editerDepense)

	@pyqtSlot()
	def voirDepense(self):
		self.ui.onglets.setCurrentWidget(self.ui.voirDepense)

	@pyqtSlot()
	def supprimerDepense(self):
		print("supprimer dépense")

	@pyqtSlot()
	def categories(self):
		self.ui.onglets.setCurrentWidget(self.ui.ongletCategories)

	@pyqtSlot()
	def ajouterCategorie(self):
		self.ui.onglets.setCurrentWidget(self.ui.ajouterCategorie)

	@pyqtSlot()
	def modifierCategorie(self):
		self.ui.onglets.setCurrentWidget(self.ui.editerCategorie)

	@pyqtSlot()
	def voirCategorie(self):
		self.ui.onglets.setCurrentWidget(self.ui.voirCategorie)

	@pyqtSlot()
	def supprimerCategorie(self):
		print("supprimer catégorie")

	@pyqtSlot()
	def membres(self):
		self.ui.onglets.setCurrentWidget(self.ui.ongletMembres)

	@pyqtSlot()
	def ajouterMembre(self):
		self.ui.onglets.setCurrentWidget(self.ui.ajouterMembre)

	@pyqtSlot()
	def modifierMembre(self):
		self.ui.onglets.setCurrentWidget(self.ui.editerMembre)

	@pyqtSlot()
	def voirMembre(self):
		self.ui.onglets.setCurrentWidget(self.ui.voirMembre)

	@pyqtSlot()
	def supprimerMembre(self):
		print("supprimer membre")
