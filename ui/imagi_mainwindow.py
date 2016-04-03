# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'imagi_mainwindow_v3.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

# ----------------------------------------
from PyQt4.QtGui import *
import imagi_syntax
import sys
# ----------------------------------------

from PyQt4 import QtCore, QtGui

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
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.setupUi(self)
    # ----------------------------------


    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(820, 717)

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("../../../../Dropbox/PL/IMAGI_PL/fish.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setTabShape(QtGui.QTabWidget.Rounded)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setStyleSheet(_fromUtf8("background-color: rgb(27, 194, 244);"))
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))

        # Top Red Stripe ----
        self.lineEdit_2 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_2.setEnabled(False)
        self.lineEdit_2.setStyleSheet(_fromUtf8("background-color: rgb(239, 0, 119);"))
        self.lineEdit_2.setFrame(False)
        self.lineEdit_2.setReadOnly(True)
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.verticalLayout.addWidget(self.lineEdit_2)
        # -------------------

        # Tab Widget ----
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setStyleSheet(_fromUtf8("background-color: qconicalgradient(cx:0, cy:0, angle:135, stop:0 rgba(255, 255, 0, 69), stop:0.375 rgba(255, 255, 0, 69), stop:0.423533 rgba(251, 255, 0, 145), stop:0.45 rgba(247, 255, 0, 208), stop:0.477581 rgba(255, 244, 71, 130), stop:0.518717 rgba(255, 218, 71, 130), stop:0.55 rgba(255, 255, 0, 255), stop:0.57754 rgba(255, 203, 0, 130), stop:0.625 rgba(255, 255, 0, 69), stop:1 rgba(255, 255, 0, 69));"))
        self.tabWidget.setTabShape(QtGui.QTabWidget.Triangular)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))

        # Code Editor Tab ----
        self.codeEditorTab = QtGui.QWidget()
        self.codeEditorTab.setStyleSheet(_fromUtf8("background-color: rgb(157, 78, 0);"))
        self.codeEditorTab.setObjectName(_fromUtf8("codeEditorTab"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.codeEditorTab)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.textEdit = QtGui.QTextEdit(self.codeEditorTab)
        self.textEdit.setStyleSheet(_fromUtf8("background-color: rgb(255, 239, 211);"))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.verticalLayout_2.addWidget(self.textEdit)
        self.tabWidget.addTab(self.codeEditorTab, _fromUtf8(""))
        # ---------------------

        # Scene Editor Tab ----
        self.sceneEditorTab = QtGui.QWidget()
        self.sceneEditorTab.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.sceneEditorTab.setObjectName(_fromUtf8("sceneEditorTab"))
        self.tabWidget.addTab(self.sceneEditorTab, _fromUtf8(""))
        # ---------------------
        self.verticalLayout.addWidget(self.tabWidget)
        # ----

        # Graphics View ----
        self.graphicsView = QtGui.QGraphicsView(self.centralwidget)
        self.graphicsView.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);\n" "border-color: rgb(157, 78, 0);"))
        self.graphicsView.setObjectName(_fromUtf8("graphicsView"))
        self.verticalLayout.addWidget(self.graphicsView)
        # ----

        # Imagine Button ----
        self.imagineButton = QtGui.QPushButton(self.centralwidget)
        self.imagineButton.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);\n" "border-color: rgb(255, 0, 127);"))
        self.imagineButton.setAutoDefault(False)
        self.imagineButton.setDefault(False)
        self.imagineButton.setFlat(False)
        self.imagineButton.setObjectName(_fromUtf8("imagineButton"))
        self.verticalLayout.addWidget(self.imagineButton)
        # ----

        # Bottom Red Stripe ----
        self.lineEdit = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit.setEnabled(False)
        self.lineEdit.setStyleSheet(_fromUtf8("background-color: rgb(239, 0, 119);"))
        self.lineEdit.setFrame(False)
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.verticalLayout.addWidget(self.lineEdit)
        # ----------------------

        # ---------------------------------------------------
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 820, 26))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        # ----------------------------------------------------

        # Added By Edgardo.... not the generator
        # The following is setting up the text editor
        self.textEdit.setLineWrapMode(QTextEdit.NoWrap)
        font = QFont()
        font.setFamily('Consolas')
        font.setFixedPitch(True)
        font.setPointSize(14)
        self.textEdit.setFont(font)
        # --------------------------------------

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "IMAGI - Programming Language for Kids - Focus on Storytelling", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.codeEditorTab), _translate("MainWindow", "Code Editor", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.sceneEditorTab), _translate("MainWindow", "Scene Editor", None))
        self.imagineButton.setText(_translate("MainWindow", "IMAGINE", None))
        # For a button action just do .clicked.connect(self.definedfunction) like in the following example -Edgardo
        self.imagineButton.clicked.connect(self.get_text)


    # Functions not made by the generator
    """
    Function to get the text from the text editor.
    -usercode variable is where the code to be analyzed is in
    """
    usercode = ''
    def get_text(self):
        user_code = self.textEdit.toPlainText()
        print user_code

if __name__ == '__main__':
    app = QtGui.QApplication([])
    mw = Ui_MainWindow()
    highlight = imagi_syntax.ImagiHighlighter(mw.textEdit.document())
    mw.show()
    sys.exit(app.exec_())