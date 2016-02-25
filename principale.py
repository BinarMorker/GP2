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

	@pyqtSlot()
	def derp(self):
		print("derp")
		self.supersignal.emit()

	@pyqtSlot()
	def depenses(self):
		self.ui.onglets.setCurrentWidget(self.ui.ongletDepenses)

	@pyqtSlot()
	def categories(self):
		self.ui.onglets.setCurrentWidget(self.ui.ongletCategories)

	@pyqtSlot()
	def membres(self):
		self.ui.onglets.setCurrentWidget(self.ui.ongletMembres)
