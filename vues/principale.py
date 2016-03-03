from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import QObject, pyqtSlot, pyqtSignal
import controlleurs
import modeles
from vues.ui_test import Ui_MainWindow
from controlleurs.vuecategories import controleurCategories
from controlleurs.vuedepenses import controleurVueDepenses

class fenetrePrincipale(QMainWindow):

	supersignal = pyqtSignal()

	def creer(self):
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)
		self.ui.onglets.tabBar().hide()
		self.controleurCategories = controleurCategories(self)
		self.controleurDepenses = controleurVueDepenses(self)
		self.ui.boutonDepenses.clicked.connect(self.depenses)
		self.ui.boutonCategories.clicked.connect(self.categories)
		self.ui.boutonMembres.clicked.connect(self.membres)
		self.ui.boutonAttribution.clicked.connect(self.attribution)
		self.ui.boutonParametres.clicked.connect(self.parametres)
		self.ui.boutonAPropos.clicked.connect(self.aPropos)
		self.ui.boutonAjouterMembre.clicked.connect(self.ajouterMembre)
		self.ui.boutonEditerMembre.clicked.connect(self.modifierMembre)
		self.ui.boutonRetirerMembre.clicked.connect(self.supprimerMembre)
		self.ui.boutonVoirMembre.clicked.connect(self.voirMembre)

	@pyqtSlot()
	def depenses(self):
		self.controleurDepenses.activer()

	@pyqtSlot()
	def categories(self):
		self.controleurCategories.activer()

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
		
	@pyqtSlot()
	def attribution(self):
		self.ui.onglets.setCurrentWidget(self.ui.ongletAttribution)

	@pyqtSlot()
	def parametres(self):
		self.ui.onglets.setCurrentWidget(self.ui.ongletParametres)

	@pyqtSlot()
	def aPropos(self):
		self.ui.onglets.setCurrentWidget(self.ui.ongletAPropos)
