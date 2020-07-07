"""
Authors: B.Friman, A.Rustamov

The formalism and analytic formulas used in the package are based on the publication:

Peter Braun-Munzinger, Bengt Friman, Krzysztof Redlich, Anar Rustamov, Johanna Stachel
Relativistic nuclear collisions: Establishing the non-critical baseline for fluctuation measurements.

arXiv:2007.02463 [nucl-th]

If you use the code to produce results for a publication, we ask you to be fair and cite the above paper!

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

