#!/usr/bin/python3

import sys
from PyQt5.QtWidgets import QApplication
import interface as ui

app = QApplication(sys.argv)
fenetre = ui.creerFenetre()
fenetre.show()
sys.exit(app.exec_())

