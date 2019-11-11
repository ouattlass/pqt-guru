#  Copyright (c) 2019.
#  @Author : Lassina OUATTARA
#  @Python code
import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidgetItem, QHeaderView, QMessageBox
import os

if __name__ == "__main__":
    app = QApplication(sys.argv)
    dialog = uic.loadUi(os.path.join(os.path.dirname(__file__), "..\\View\\Client_creation_UI.ui"))
    print(dialog.email_input.setText('lassina@gmail.com'))
    dialog.show()
    sys.exit(app.exec_())

