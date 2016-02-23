import sys
from PyQt5.QtWidgets import QApplication, QDialog
from ui_test import Ui_Dialog

app = QApplication(sys.argv)
window = QDialog()
ui = Ui_Dialog()
ui.setupUi(window)

window.accepted.connect(window.show)

window.show()
sys.exit(app.exec_())
