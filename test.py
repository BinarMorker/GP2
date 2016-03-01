#!/usr/bin/python3

import sys

sys.path.insert(0, '/views/')

from PyQt5.QtWidgets import QApplication
import vues.principale as principale

app = QApplication(sys.argv)
fenetre = principale.fenetrePrincipale()
fenetre.creer()

fenetre.show()
sys.exit(app.exec_())

