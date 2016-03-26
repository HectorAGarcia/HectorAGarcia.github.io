# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'imagi_mainwindow.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import *
import imagi_syntax
import sys

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(QMainWindow):
    # Added By Edgardo.... not the generator
    # textEdit = QtGui.QTextEdit()
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.setupUi(self)
    # ----------------------------------

    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1117, 856)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.textEdit = QtGui.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(10, 50, 1101, 341))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))

        # Added By Edgardo.... not the generator
        # The following is setting up the text editor
        self.textEdit.setLineWrapMode(QTextEdit.NoWrap)
        font = QFont()
        font.setFamily('Consolas')
        font.setFixedPitch(True)
        font.setPointSize(14)
        self.textEdit.setFont(font)
        p = self.textEdit.palette()
        p.setColor(QPalette.Base, QColor(228, 255, 221))
        self.textEdit.setPalette(p)

        # --------------------------------------

        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(500, 10, 93, 28))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_3 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(500, 410, 93, 28))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.graphicsView = QtGui.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(10, 450, 1091, 351))
        self.graphicsView.setObjectName(_fromUtf8("graphicsView"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1117, 26))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.pushButton.setText(_translate("MainWindow", "Setup Scene", None))
        self.pushButton_3.setText(_translate("MainWindow", "Imagine", None))


if __name__ == '__main__':
    app = QtGui.QApplication([])
    mw = Ui_MainWindow()
    highlight = imagi_syntax.ImagiHighlighter(mw.textEdit.document())
    mw.show()
    sys.exit(app.exec_())