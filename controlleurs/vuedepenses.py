from PyQt5.QtCore import QObject, pyqtSlot, pyqtSignal, Qt
from PyQt5.QtWidgets import QTableWidgetItem
from controlleurs.creerDepense import creerDepense
from controlleurs.modifierDepense import modifierDepense
from controlleurs.voirDepense import voirDepense
from controlleurs.depenses import DepensesControlleur as controleur_depenses

class controleurVueDepenses:

	sauvegarder = pyqtSignal()

	def __init__(self, fenetrePrincipale):
		self.fenetre = fenetrePrincipale
		self.controleurCreerDepense = creerDepense(self.fenetre)
		self.controleurModifierDepense = modifierDepense(self.fenetre)
		self.controleurVoirDepense = voirDepense(self.fenetre)
		self.fenetre.ui.boutonAjouterDepense.clicked.connect(self.ajouter)
		self.fenetre.ui.boutonEditerDepense.clicked.connect(self.modifier)
		self.fenetre.ui.boutonRetirerDepense.clicked.connect(self.supprimer)
		self.fenetre.ui.boutonVoirDepense.clicked.connect(self.voir)
		self.fenetre.ui.tabDep.currentCellChanged.connect(self.selectionner_id)

	@pyqtSlot()
	def activer(self):
		self.fenetre.ui.onglets.setCurrentWidget(self.fenetre.ui.ongletDepenses)
		depenses = controleur_depenses.liste_depenses()
		self.fenetre.ui.tabDep.setRowCount(len(depenses))
		self.fenetre.ui.tabDep.setColumnCount(4)
		i=0
		for depense in depenses:
			nom = QTableWidgetItem(depense.nom)
			nom.setData(Qt.UserRole, depense.id)
			self.fenetre.ui.tabDep.setItem(i,0,nom)
			description = QTableWidgetItem(depense.description)
			self.fenetre.ui.tabDep.setItem(i,1,description)
			montant = QTableWidgetItem(str(depense.montant))
			self.fenetre.ui.tabDep.setItem(i,2,montant)
			categorie = QTableWidgetItem(depense.categorie.nom)
			self.fenetre.ui.tabDep.setItem(i,3,categorie)
			i+=1
		self.id_selectionne = -1

	@pyqtSlot()
	def ajouter(self):
		self.controleurCreerDepense.activer()

	@pyqtSlot()
	def modifier(self):
		if (self.id_selectionne != -1):
			self.controleurModifierDepense.activer(self.id_selectionne)

	@pyqtSlot()
	def voir(self):
		if (self.id_selectionne != -1):
			self.controleurVoirDepense.activer(self.id_selectionne)

	@pyqtSlot()	
	def supprimer(self, depense):
		print("supprimer la dépense yarr")

	@pyqtSlot()
	def selectionner_id(self):
		rangee = self.fenetre.ui.tabDep.currentIndex().row()
		#cellule_id = self.fenetre.ui.tabDep.model().index(rangee, 0)
		self.id_selectionne = int(self.fenetre.ui.tabDep.item(rangee, 0).data(Qt.UserRole))
		print(self.id_selectionne)
