from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import QObject, pyqtSlot, pyqtSignal
import controlleurs
import modeles
from vues.ui_test import Ui_MainWindow
from controlleurs.vuecategories import controleurCategories
from controlleurs.vuedepenses import controleurDepenses

class fenetrePrincipale(QMainWindow):

	supersignal = pyqtSignal()

	def creer(self):
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)
		self.ui.onglets.tabBar().hide()
		self.controleurCategories = controleurCategories(self)
		self.controleurDepenses = controleurDepenses(self)
		self.ui.boutonDepenses.clicked.connect(self.depenses)
		self.ui.boutonCategories.clicked.connect(self.categories)
		self.ui.boutonMembres.clicked.connect(self.membres)
		self.ui.boutonParametres.clicked.connect(self.parametres)
		self.ui.boutonAPropos.clicked.connect(self.aPropos)
		self.ui.boutonAjouterCategorie.clicked.connect(self.ajouterCategorie)
		self.ui.boutonEditerCategorie.clicked.connect(self.modifierCategorie)
		self.ui.boutonRetirerCategorie.clicked.connect(self.supprimerCategorie)
		self.ui.boutonVoirCategorie.clicked.connect(self.voirCategorie)
		self.ui.boutonAjouterMembre.clicked.connect(self.ajouterMembre)
		self.ui.boutonEditerMembre.clicked.connect(self.modifierMembre)
		self.ui.boutonRetirerMembre.clicked.connect(self.supprimerMembre)
		self.ui.boutonVoirMembre.clicked.connect(self.voirMembre)

	# @pyqtSlot()
	# def depenses(self):
	# 	self.ui.onglets.setCurrentWidget(self.ui.ongletDepenses)

	# @pyqtSlot()
	# def ajouterDepense(self):
	# 	self.ui.onglets.setCurrentWidget(self.ui.ajouterDepense)

	# @pyqtSlot()
	# def modifierDepense(self):
	# 	self.ui.onglets.setCurrentWidget(self.ui.editerDepense)

	# @pyqtSlot()
	# def voirDepense(self):
	# 	self.ui.onglets.setCurrentWidget(self.ui.voirDepense)

	# @pyqtSlot()
	# def supprimerDepense(self):
	# 	print("supprimer dépense")

	@pyqtSlot()
	def categories(self):
		self.ui.onglets.setCurrentWidget(self.ui.ongletCategories)

	@pyqtSlot()
	def ajouterCategorie(self):
		self.controleurCategories.ajouter()
		#self.controleurCreerCategorie.activer()

	@pyqtSlot()
	def modifierCategorie(self):
		self.controleurCategories.modifier("derp")
		#self.controleurModifierCategorie.activer()

	@pyqtSlot()
	def voirCategorie(self):
		self.controleurCategories.voir("derp")
		#self.controleurVoirCategorie.activer()

	@pyqtSlot()
	def supprimerCategorie(self):
		self.controleurCategories.supprimer("derp")
		#print("supprimer membre")

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
	def parametres(self):
		self.ui.onglets.setCurrentWidget(self.ui.ongletParametres)

	@pyqtSlot()
	def aPropos(self):
		self.ui.onglets.setCurrentWidget(self.ui.ongletAPropos)
