from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import QObject, pyqtSlot
from ui_test import Ui_MainWindow

class fenetrePrincipale:

	def __init__(self):
		self.window = QMainWindow()
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self.window)
		self.ui.tabWidget.tabBar().hide()
		self.ui.boutonEntites.clicked.connect(self.derp)
		#pyqtSignal(int, int, name='rangeChanged')

	@pyqtSlot()
	def derp(self):
		print("derp")
