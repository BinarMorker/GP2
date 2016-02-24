from PyQt5.QtWidgets import QMainWindow
from ui_test import Ui_MainWindow

def creerFenetre():
	window = QMainWindow()
	ui = Ui_MainWindow()
	ui.setupUi(window)
	ui.tabWidget.tabBar().hide()
	return window
