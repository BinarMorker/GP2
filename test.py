#!/usr/bin/python3

import sys
from PyQt5.QtWidgets import QApplication
import principale as principale

app = QApplication(sys.argv)
fenetre = principale.fenetrePrincipale()

fenetre.window.show()
sys.exit(app.exec_())

