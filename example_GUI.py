"""
Authors: B.Friman, A.Rustamov
"""

#from ce_cumulants.cumulans import Cumulants
from ce_cumulants.GUI import CeGUI
# creating the object od Cumulant
from PyQt5 import QtCore, QtGui, QtWidgets
import sys

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = CeGUI()
ui.setup_ui(MainWindow)
MainWindow.show()
sys.exit(app.exec_())

