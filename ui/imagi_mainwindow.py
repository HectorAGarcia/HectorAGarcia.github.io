# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'imagi_mainwindow_v3.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

# ----------------------------------------
from PyQt4.QtGui import *
import AnimatorClass
import imagi_syntax
import imagi_character_class
import sys
from ILA import *

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
        self.lastAnim=None
        self.characters = []
        self.activeCharacters = []
        self.animators={}
        self.setCharacters()
        self.backgrounds = []
        self.setBackgrounds()
        self.default_scene()
        self.animations={} #animations dictionary
        ##self.group= QtCore.QSequentialAnimationGroup() #Animation group
        self.animation = None # The animation object, do not change
        set_window(self) #set a reference to the main window in the ILA
        self.compiler=Compiler()
        self.compiler.set_comp(self)
    # ----------------------------------


    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.setFixedSize(820, 717) # DO NOT CHANGE

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("Media/fish.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setTabShape(QtGui.QTabWidget.Rounded)
        self.centralwidget = QtGui.QWidget(MainWindow)
        # self.centralwidget.setStyleSheet(_fromUtf8("background-color: rgb(27, 194, 244);"))
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
        self.applySceneChangesButton = QtGui.QPushButton(self.sceneEditorTab)
        self.applySceneChangesButton.setStyleSheet(_fromUtf8("background-color: rgb(255, 238, 41);\n" "border-color: rgb(255, 0, 127);"))
        self.applySceneChangesButton.setAutoDefault(False)
        self.applySceneChangesButton.setDefault(False)
        self.applySceneChangesButton.setFlat(False)
        self.applySceneChangesButton.setObjectName(_fromUtf8("applySceneChangesButton"))
        self.applySceneChangesButton.setGeometry(QtCore.QRect(580, 240, 200, 20))
        self.applySceneChangesButton.setText('Apply Scene Changes')
        # ---------------------
        self.verticalLayout.addWidget(self.tabWidget)
        # ----

        # Graphics View ----
        self.graphicsView = QtGui.QGraphicsView(self.centralwidget)
        self.graphicsView.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);\n" "border-color: rgb(157, 78, 0);"))
        self.graphicsView.setObjectName(_fromUtf8("graphicsView"))
        self.verticalLayout.addWidget(self.graphicsView)
        self.graphicsView.isHidden()
        self.sceneBackground = QtGui.QLabel(self.centralwidget)
        self.sceneBackground.setText(_fromUtf8(""))
        self.sceneBackground.setScaledContents(True)
        self.sceneBackground.setGeometry(QtCore.QRect(11, 332, 798, 289))
        self.sceneBackground.setObjectName(_fromUtf8("sceneBackground"))
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
        self.imagineButton.clicked.connect(self.run_code)
        self.applySceneChangesButton.clicked.connect(self.apply_scene_changes)

    # Functions not made by the generator
    """
    Function for apply scene changes button that updates the background
    according to the radio button selected in the background selector in the
    scene editor tab.
    """
    def apply_scene_changes(self):
        self.displaySelectedBackground()
        self.setSelectedCharactersAsActive()
        self.setUnselectedCharactersAsInactive()

    """
    Function to get the text from the text editor.
    """
    def get_text(self):
        return self.textEdit.toPlainText()

    """
    ------------------ New ----------------------------------------
    """

    """
    Function to run the code
    """
    def run_code(self):
        self.group= QtCore.QSequentialAnimationGroup()
        self.reset_character_labels()
        code=self.get_text()
        code1=str(code)
        lines=code1.split(";")
        code= self.clean_code(lines)
        for line in code:
             self.compiler.compile(line)#compile line
        i=0
        self.group.start()





    """
    Function to clean  new lines from code....
    """
    def clean_code(self, lines):
        ctr=[]
        for line in lines:
            str=""
            list=line.split("\n")
            for item in list:
                if item !="":
                    str=item
            if str !="":
                ctr.append(str)
        return ctr

    """
    Function to return the main window compiler instance
    """
    def get_window_compiler(self):
        return self.compiler

    """
    Function to return the character dictionary
    """
    def get_characters_dict(self):
        return self.characterDICT

    def getAnimatorsDict(self):
        return self.animators

    def reset_character_labels(self):
        self.characterDICT["fish"].setGeometry(QtCore.QRect(20, 525, 70, 70))
        self.characterDICT["dog"].setGeometry(QtCore.QRect(120, 525, 70, 70))
        self.characterDICT["lion"].setGeometry(QtCore.QRect(220, 525, 100, 100))

    """
    -----------------------------------------------------------------------------
    """

    """
    Function to setup the chracters available for the user to select
    """
    def setCharacters(self):
        self.characterSelectText = QtGui.QLabel(self.sceneEditorTab)
        self.characterSelectText.setText('CHARACTERS')
        self.characterSelectText.setGeometry(QtCore.QRect(150, 10, 95, 20))

        fishIcon = QtGui.QIcon()
        fishIcon.addPixmap(QtGui.QPixmap(_fromUtf8("Media/fish.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        dogIcon = QtGui.QIcon()
        dogIcon.addPixmap(QtGui.QPixmap(_fromUtf8("Media/dog.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        lionIcon = QtGui.QIcon()
        lionIcon.addPixmap(QtGui.QPixmap(_fromUtf8("Media/lion.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        self.fishButton = QtGui.QCheckBox(self.sceneEditorTab)
        self.fishButton.setIcon(fishIcon)
        self.fishButton.setText('Fish')
        self.fishButton.setGeometry(QtCore.QRect(20, 50, 95, 20))

        self.dogButton = QtGui.QCheckBox(self.sceneEditorTab)
        self.dogButton.setIcon(dogIcon)
        self.dogButton.setText('Dog')
        self.dogButton.setGeometry(QtCore.QRect(20, 100, 95, 20))

        self.lionButton = QtGui.QCheckBox(self.sceneEditorTab)
        self.lionButton.setIcon(lionIcon)
        self.lionButton.setText('Lion')
        self.lionButton.setGeometry(QtCore.QRect(20, 150, 95, 20))
        # Add them to a list
        self.characters.append(self.fishButton)
        self.characters.append(self.dogButton)
        self.characters.append(self.lionButton)
        # Create the characters
        self.fishCharacter = imagi_character_class.ImagiCharacter(self.addCharacterToScene('Fish', 'Media/fish.png', 20, 525, 70, 70))
        self.dogCharacter = imagi_character_class.ImagiCharacter(self.addCharacterToScene('Dog', 'Media/dog.png', 120, 525, 70, 70))
        self.dogCharacter.characterLabel.setVisible(False)
        self.lionCharacter = imagi_character_class.ImagiCharacter(self.addCharacterToScene('Lion', 'Media/lion.png', 220, 525, 100, 100))
        self.lionCharacter.characterLabel.setVisible(False)

        #Create a dictionary containing all characters
        self.characterDICT={"fish":self.fishCharacter.characterLabel,"dog":self.dogCharacter.characterLabel,"lion":self.lionCharacter.characterLabel}
        self.animators={"fish":AnimatorClass.Animator(self.fishCharacter.characterLabel),"dog":AnimatorClass.Animator(self.fishCharacter.characterLabel),"lion":AnimatorClass.Animator(self.fishCharacter.characterLabel)}

    """
    Function to setup the backgrounds available for the user to select
    """
    def setBackgrounds(self):
        self.backgroundSelectText = QtGui.QLabel(self.sceneEditorTab)
        self.backgroundSelectText.setText('BACKGROUND')
        self.backgroundSelectText.setGeometry(QtCore.QRect(550, 10, 95, 20))

        self.desertButton = QtGui.QRadioButton(self.sceneEditorTab)
        self.desertButton.setText('Desert Highway')
        self.desertButton.setGeometry(QtCore.QRect(420, 50, 120, 20))

        self.beachButton = QtGui.QRadioButton(self.sceneEditorTab)
        self.beachButton.setText('Cool Beach')
        self.beachButton.setGeometry(QtCore.QRect(420, 100, 120, 20))

        self.plainsButton = QtGui.QRadioButton(self.sceneEditorTab)
        self.plainsButton.setText('Pink Tree Plains')
        self.plainsButton.setGeometry(QtCore.QRect(420, 150, 120, 20))
        # Add them to a list
        self.backgrounds.append(self.desertButton)
        self.backgrounds.append(self.beachButton)
        self.backgrounds.append(self.plainsButton)

    """
    Displays the background according to the selected radio button, remember that only radio button can be
    selected at a time.
    """
    def displaySelectedBackground(self):
        for background in self.backgrounds:
            if background.isChecked() and background.text() == 'Pink Tree Plains':
                self.sceneBackground.setPixmap(QtGui.QPixmap(_fromUtf8("Media/pink_tree_plains.png")))
            if background.isChecked() and background.text() == 'Desert Highway':
                self.sceneBackground.setPixmap(QtGui.QPixmap(_fromUtf8("Media/desert_highway.png")))
            if background.isChecked() and background.text() == 'Cool Beach':
                self.sceneBackground.setPixmap(QtGui.QPixmap(_fromUtf8("Media/cool_beach.png")))

    def addCharacterToScene(self, character, character_image, posX, posY, length, width):
        self.charLabel = QtGui.QLabel(self.centralwidget)
        self.charLabel.setText(_fromUtf8(""))
        self.charLabel.setScaledContents(True)
        self.charLabel.setGeometry(QtCore.QRect(posX, posY, length, width))
        self.charLabel.setObjectName(_fromUtf8(character))
        self.charLabel.setPixmap(QtGui.QPixmap(_fromUtf8(character_image)))
        return self.charLabel

    def setSelectedCharactersAsActive(self):
        for character in self.characters:
            if character.isChecked() and character.text() == 'Fish':
                self.activeCharacters.append(self.fishCharacter)
                self.fishCharacter.characterLabel.setVisible(True)
            if character.isChecked() and character.text() == 'Dog':
                self.activeCharacters.append(self.dogCharacter)
                self.dogCharacter.characterLabel.setVisible(True)
            if character.isChecked() and character.text() == 'Lion':
                self.activeCharacters.append(self.lionCharacter)
                self.lionCharacter.characterLabel.setVisible(True)

    def setUnselectedCharactersAsInactive(self):
        for character in self.characters:
            if not character.isChecked() and character.text() == 'Fish':
                self.fishCharacter.characterLabel.setVisible(False)
            if not character.isChecked() and character.text() == 'Dog':
                self.dogCharacter.characterLabel.setVisible(False)
            if not character.isChecked() and character.text() == 'Lion':
                self.lionCharacter.characterLabel.setVisible(False)
        # We need at least one character to be active though so let's put fish as default if nothing else is active
        if not self.characters[0].isChecked() and not self.characters[1].isChecked() and not self.characters[2].isChecked():
            self.characters[0].setChecked(True)
            self.setSelectedCharactersAsActive()

    """
    Function to update the scene according to default editor selectables
    Called upon startup
    """
    def default_scene(self):
        self.backgrounds[2].setChecked(True) # Default background scene is Pink Tree Plains
        self.characters[0].setChecked(True) # Default active character is Fish
        self.setSelectedCharactersAsActive()

    """
    Function to update the scene according to scene editor selectables
    """
    def update_scene(self):
        return None

    """
    Animation Functions
    """

    def moveRight(self, characterLabel):
        animationMoveRight = QtCore.QPropertyAnimation(characterLabel, 'geometry') # Create the animation for specific characterLabel
        animationMoveRight.setDuration(1000)
        x1 = characterLabel.x()
        x2 = characterLabel.x() + 100
        y1 = characterLabel.y()
        w1 = characterLabel.width()
        h1 = characterLabel.height()
        animationMoveRight.setStartValue(QtCore.QRect(x1, y1 , w1, h1)) # Original QRect Properties of characterLabel
        animationMoveRight.setEndValue(QtCore.QRect(x2, y1, w1, h1)) # QRect Properties after animation of characterLabel
        characterLabel.setGeometry(QtCore.QRect(x2, y1, w1, h1)) #Change label x coordinate

        return animationMoveRight

    def moveLeft(self, characterLabel):
        animationMoveLeft = QtCore.QPropertyAnimation(characterLabel, 'geometry') # Create the animation for specific characterLabel
        animationMoveLeft.setDuration(1000)
        x1 = characterLabel.x()

        x2 = characterLabel.x() - 100
        y1 = characterLabel.y()
        w1 = characterLabel.width()
        h1 = characterLabel.height()
        animationMoveLeft.setStartValue(QtCore.QRect(x1, y1 , w1, h1)) # Original QRect Properties of characterLabel
        animationMoveLeft.setEndValue(QtCore.QRect(x2, y1, w1, h1)) # QRect Properties after animation of characterLabel
        characterLabel.setGeometry(QtCore.QRect(x2, y1, w1, h1)) #Change label x coordinate

        return  animationMoveLeft

    def jumpAnimation(self, characterLabel, direction):
        animationJump = QtCore.QPropertyAnimation(characterLabel, 'geometry') # Create the animation for specific characterLabel
        if direction=="up":
            animationJump.setDuration(200)
            x1 = characterLabel.x()
            x2 = characterLabel.x()
            y1 = characterLabel.y()
            y2 = characterLabel.y()-50
            w1 = characterLabel.width()
            h1 = characterLabel.height()
        else:
            animationJump.setDuration(400)
            x1 = characterLabel.x()
            x2 = characterLabel.x()
            y1 = characterLabel.y()
            y2 = characterLabel.y()+50
            w1 = characterLabel.width()
            h1 = characterLabel.height()

        animationJump.setStartValue(QtCore.QRect(x1, y1 , w1, h1)) # Original QRect Properties of characterLabel
        animationJump.setEndValue(QtCore.QRect(x2, y2, w1, h1)) # QRect Properties after animation of characterLabel
        characterLabel.setGeometry(QtCore.QRect(x2, y2, w1, h1)) #Change label x coordinate

        return animationJump

    def shrinkCharacter(self, characterLabel):
        animationShrink = QtCore.QPropertyAnimation(characterLabel, 'geometry') # Create the animation for specific characterLabel
        animationShrink.setDuration(500)
        if characterLabel.height>30 and characterLabel.width>30:
            x1 = characterLabel.x()
            y1 = characterLabel.y()
            w1 = characterLabel.width()
            h1 = characterLabel.height()
            w2 = characterLabel.width()-20
            h2 = characterLabel.height()-20

        animationShrink.setStartValue(QtCore.QRect(x1, y1 , w1, h1)) # Original QRect Properties of characterLabel
        animationShrink.setEndValue(QtCore.QRect(x1, y1, w2, h2)) # QRect Properties after animation of characterLabel
        characterLabel.setGeometry(QtCore.QRect(x1, y1, w2, h2)) #Change label x coordinate

        return animationShrink

    def growCharacter(self, characterLabel):
        animationGrow = QtCore.QPropertyAnimation(characterLabel, 'geometry') # Create the animation for specific characterLabel
        animationGrow.setDuration(500)
        x1 = characterLabel.x()
        y1 = characterLabel.y()
        w1 = characterLabel.width()
        h1 = characterLabel.height()
        w2 = characterLabel.width()+20
        h2 = characterLabel.height()+20

        animationGrow.setStartValue(QtCore.QRect(x1, y1 , w1, h1)) # Original QRect Properties of characterLabel
        animationGrow.setEndValue(QtCore.QRect(x1, y1, w2, h2)) # QRect Properties after animation of characterLabel
        characterLabel.setGeometry(QtCore.QRect(x1, y1, w2, h2)) #Change label x coordinate

        return animationGrow

    def runAnimation(self, characterLabel, direction):
        animationRun = QtCore.QPropertyAnimation(characterLabel, 'geometry') # Create the animation for specific characterLabel
        animationRun.setDuration(500)
        if direction=="right":
            x1 = characterLabel.x()
            x2 = characterLabel.x() + 100
            y1 = characterLabel.y()
            w1 = characterLabel.width()
            h1 = characterLabel.height()
        else:
            x1 = characterLabel.x()
            x2 = characterLabel.x() - 100
            y1 = characterLabel.y()
            w1 = characterLabel.width()
            h1 = characterLabel.height()
        animationRun.setStartValue(QtCore.QRect(x1, y1 , w1, h1)) # Original QRect Properties of characterLabel
        animationRun.setEndValue(QtCore.QRect(x2, y1, w1, h1)) # QRect Properties after animation of characterLabel
        characterLabel.setGeometry(QtCore.QRect(x2, y1, w1, h1)) #Change label x coordinate

        return animationRun

    def moveAnimation(self, characterLabel, direction):
        animationMove = QtCore.QPropertyAnimation(characterLabel, 'geometry') # Create the animation for specific characterLabel
        animationMove.setDuration(1000)
        if direction=="right":
            x1 = characterLabel.x()
            x2 = characterLabel.x() + 100
            y1 = characterLabel.y()
            w1 = characterLabel.width()
            h1 = characterLabel.height()
        else:
            x1 = characterLabel.x()
            x2 = characterLabel.x() - 100
            y1 = characterLabel.y()
            w1 = characterLabel.width()
            h1 = characterLabel.height()
        animationMove.setStartValue(QtCore.QRect(x1, y1 , w1, h1)) # Original QRect Properties of characterLabel
        animationMove.setEndValue(QtCore.QRect(x2, y1, w1, h1)) # QRect Properties after animation of characterLabel
        characterLabel.setGeometry(QtCore.QRect(x2, y1, w1, h1)) #Change label x coordinate

        return animationMove

if __name__ == '__main__':
    app = QtGui.QApplication([])
    mw = Ui_MainWindow()
    highlight = imagi_syntax.ImagiHighlighter(mw.textEdit.document())
    mw.displaySelectedBackground()
    mw.show()
    sys.exit(app.exec_())