from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import QObject, pyqtSlot, pyqtSignal
from ui_test import Ui_MainWindow

class fenetrePrincipale(QMainWindow):

	supersignal = pyqtSignal()

	def creer(self):
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)
		self.ui.tabWidget.tabBar().hide()
		self.ui.boutonEntites.clicked.connect(self.derp)
		self.ui.boutonCategories.clicked.connect(self.herp)
		self.supersignal.connect(self.herp)

	@pyqtSlot()
	def derp(self):
		print("derp")
		self.supersignal.emit()

	@pyqtSlot()
	def herp(self):
		print("herp")
