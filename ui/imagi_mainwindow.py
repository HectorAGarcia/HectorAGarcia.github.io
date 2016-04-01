# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'imagi_mainwindow.ui'
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
        MainWindow.setEnabled(True)
        MainWindow.resize(1108, 864)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("../../../../../Dropbox/PL/IMAGI-Logo-S.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setAutoFillBackground(False)
        self.centralwidget.setStyleSheet(_fromUtf8("background-color: rgb(255, 221, 48);"))
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.blueTopStripe = QtGui.QWidget(self.centralwidget)
        self.blueTopStripe.setGeometry(QtCore.QRect(-30, 0, 1141, 31))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.blueTopStripe.sizePolicy().hasHeightForWidth())
        self.blueTopStripe.setSizePolicy(sizePolicy)
        self.blueTopStripe.setAutoFillBackground(False)
        self.blueTopStripe.setStyleSheet(_fromUtf8("background-color: rgb(38, 237, 255);"))
        self.blueTopStripe.setObjectName(_fromUtf8("blueTopStripe"))
        self.scene = QtGui.QGraphicsView(self.centralwidget)
        self.scene.setGeometry(QtCore.QRect(10, 430, 1091, 341))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scene.sizePolicy().hasHeightForWidth())
        self.scene.setSizePolicy(sizePolicy)
        self.scene.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.scene.setFrameShape(QtGui.QFrame.Box)
        self.scene.setFrameShadow(QtGui.QFrame.Raised)
        self.scene.setObjectName(_fromUtf8("scene"))
        self.redBotStripe = QtGui.QWidget(self.centralwidget)
        self.redBotStripe.setGeometry(QtCore.QRect(-10, 780, 1121, 31))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.redBotStripe.sizePolicy().hasHeightForWidth())
        self.redBotStripe.setSizePolicy(sizePolicy)
        self.redBotStripe.setStyleSheet(_fromUtf8("background-color: rgb(226, 0, 113);"))
        self.redBotStripe.setObjectName(_fromUtf8("redBotStripe"))
        self.brownBelowGraphics = QtGui.QWidget(self.centralwidget)
        self.brownBelowGraphics.setGeometry(QtCore.QRect(0, 420, 1111, 361))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.brownBelowGraphics.sizePolicy().hasHeightForWidth())
        self.brownBelowGraphics.setSizePolicy(sizePolicy)
        self.brownBelowGraphics.setStyleSheet(_fromUtf8("background-color: rgb(157, 78, 0);"))
        self.brownBelowGraphics.setObjectName(_fromUtf8("brownBelowGraphics"))
        self.scene.raise_()
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 1111, 421))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.tabWidget.setPalette(palette)
        self.tabWidget.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.tabWidget.setTabShape(QtGui.QTabWidget.Triangular)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.textEditorTab = QtGui.QWidget()
        self.textEditorTab.setObjectName(_fromUtf8("textEditorTab"))
        self.textEdit = QtGui.QTextEdit(self.textEditorTab)
        self.textEdit.setGeometry(QtCore.QRect(0, 0, 1111, 401))
        self.textEdit.setStyleSheet(_fromUtf8("background-color: rgb(255, 239, 211);"))
        self.textEdit.setFrameShape(QtGui.QFrame.NoFrame)
        self.textEdit.setFrameShadow(QtGui.QFrame.Plain)
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.tabWidget.addTab(self.textEditorTab, _fromUtf8(""))
        self.sceneEditorTab = QtGui.QWidget()
        self.sceneEditorTab.setObjectName(_fromUtf8("sceneEditorTab"))
        self.tabWidget.addTab(self.sceneEditorTab, _fromUtf8(""))





        self.imagineButton = QtGui.QPushButton(self.centralwidget)
        self.imagineButton.setGeometry(QtCore.QRect(460, 790, 201, 31))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.imagineButton.sizePolicy().hasHeightForWidth())
        self.imagineButton.setSizePolicy(sizePolicy)
        self.imagineButton.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.imagineButton.setObjectName(_fromUtf8("imagineButton"))
        self.redBotStripe.raise_()
        self.brownBelowGraphics.raise_()
        self.blueTopStripe.raise_()
        self.scene.raise_()
        self.tabWidget.raise_()
        self.imagineButton.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1108, 26))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.menubar.sizePolicy().hasHeightForWidth())
        self.menubar.setSizePolicy(sizePolicy)
        self.menubar.setStyleSheet(_fromUtf8(""))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)

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
        MainWindow.setWindowTitle(_translate("MainWindow", "IMAGI Programming Language for Kids - Focus on Storytelling", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.textEditorTab), _translate("MainWindow", "Code Editor", None))
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