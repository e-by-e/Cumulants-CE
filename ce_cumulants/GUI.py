"""
Authors: B.Friman, A.Rustamov
"""
from PyQt5 import QtCore, QtGui, QtWidgets
from ce_cumulants.cumulans import Cumulants


class CeGUI(object):
    def setup_ui(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setMinimumSize(QtCore.QSize(800, 600))
        MainWindow.setMaximumSize(QtCore.QSize(800, 600))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(20, 271, 761, 271))
        self.textBrowser.setObjectName("textBrowser")

        self.textBrowser_2 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_2.setGeometry(QtCore.QRect(10, 10, 781, 31))
        self.textBrowser_2.setObjectName("textBrowser_2")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 556, 241, 16))
        self.label.setObjectName("label")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(275, 180, 114, 35))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.click_method)

        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(120, 70, 81, 21))
        self.textEdit.setObjectName("textEdit")
        self.textEdit.setText(str(370))

        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(120, 100, 81, 21))
        self.textEdit_2.setObjectName("textEdit_2")
        self.textEdit_2.setText(str(20))

        self.spinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox.setMaximum(100)
        self.spinBox.setValue(2)
        self.spinBox.setMinimum(1)
        self.spinBox.setGeometry(QtCore.QRect(280, 67, 104, 26))
        self.spinBox.setObjectName("spinBox")

        self.textEdit_3 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_3.setGeometry(QtCore.QRect(120, 160, 81, 21))
        self.textEdit_3.setObjectName("textEdit_3")
        self.textEdit_3.setText(str(0.106))

        self.textEdit_4 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_4.setGeometry(QtCore.QRect(120, 130, 81, 21))
        self.textEdit_4.setObjectName("textEdit_4")
        self.textEdit_4.setText(str(0.068))

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(60, 73, 60, 16))
        self.label_2.setObjectName("label_2")

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(60, 103, 60, 16))
        self.label_3.setObjectName("label_3")

        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(60, 131, 60, 16))
        self.label_4.setObjectName("label_4")

        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(60, 161, 60, 16))
        self.label_5.setObjectName("label_5")
        
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(284, 49, 101, 16))
        self.label_6.setObjectName("label_6")

        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(31, 229, 151, 16))
        self.label_7.setObjectName("label_7")

        self.textBrowser_3 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_3.setGeometry(QtCore.QRect(500, 60, 261, 121))
        self.textBrowser_3.setObjectName("textBrowser_3")

        self.textBrowser_4 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_4.setGeometry(QtCore.QRect(20, 246, 171, 22))
        self.textBrowser_4.setObjectName("textBrowser_4")

        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(250, 110, 161, 20))
        self.checkBox.setObjectName("checkBox")
        self.checkBox.setText("print analytic formulas")

        self.checkBox_2 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_2.setGeometry(QtCore.QRect(250, 136, 121, 20))
        self.checkBox_2.setObjectName("checkBox_2")
        self.checkBox_2.setText("Generate .cc file")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def click_method(self):
        self.textBrowser.clear()
        self.textBrowser.clearHistory()
        self.textBrowser_4.clear()
        self.textBrowser_4.clearHistory()
        NB = float(self.textEdit.toPlainText())
        NBar = float(self.textEdit_2.toPlainText())
        pB = float(self.textEdit_4.toPlainText())
        pBar = float(self.textEdit_3.toPlainText())
        nc = self.spinBox.value()
        a = Cumulants(NB, NBar, pB, pBar)
        a.process(nc)
        kappax_num = a.get_num_values()
        kappax_formulas = a.get_formulas()
        zr = a.get_recalculatedz()
        outstring = []
        if self.checkBox_2.checkState():
            outF = open("ce_cumulants.cc", "w")
        for i in range(0, nc):
            outstring.extend(['{:.6}'.format(float(kappax_num[i]))])
        zr0 = '{:.10}'.format(float(zr[0]))
        self.textBrowser_4.append("z = " + str(zr0))
        #self.textBrowser_4.setStyleSheet("background-color: green;")
        self.textBrowser_4.repaint()
        self.textBrowser.append("Numerical values\n")
        for i in range(0, nc):
            self.textBrowser.append("kappa_" + str(i+1) + "  = " + str(outstring[i]))
        if self.checkBox.checkState():
            self.textBrowser.append("")
            self.textBrowser.append("Analytic formulas: \n")
            for i in range(0, nc):
                self.textBrowser.append("kappa_" + str(i+1) + "  = " + str(kappax_formulas[i]).replace("std::","") + "\n")
        if self.checkBox_2.checkState():
            for i in range(0, nc):
                outF.write(f'double kappa{i+1}(double NBc, double NBbc, double z, double p, double pb) \n{"{"} '
                           f'\n      double k{i+1} = '
                           f'{str(kappax_formulas[i])}; \n      {"return"} k{i+1}; \n{"}"}')
                outF.write("\n")
                outF.write("\n")
            outF.close()
        self.textBrowser.repaint()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", ""))
        self.textBrowser_2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt; font-weight:600; color:#ad1b20;\">Cumulants in the canonical thermodynamics</span></p></body></html>"))
        self.label.setText(_translate("MainWindow", "Authors: B. Friman, A. Rustamov"))
        self.label_7.setText(_translate("MainWindow", "Recalculated value of z"))
        self.pushButton.setText(_translate("MainWindow", "calculate"))
        self.label_2.setText(_translate("MainWindow", "NB :"))
        self.label_3.setText(_translate("MainWindow", "NBar :"))
        self.label_4.setText(_translate("MainWindow", "pB :"))
        self.label_5.setText(_translate("MainWindow", "pBar :"))
        self.label_6.setText(_translate("MainWindow", "cumulant order"))
        self.textBrowser_3.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">NB</span>: number of baryons in 4pi</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">NBar</span>: number of anti-baryons in 4pi</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">pB</span>: accepted protons</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">pBar</span>: accepted anti-protons </p></body></html>"))


