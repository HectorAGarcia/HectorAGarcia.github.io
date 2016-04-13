import sys
from PyQt4 import QtGui, QtCore
from PyQt4.QtGui import QWidget, QMainWindow
import imagi_mainwindow



class Animator():
    def __init__(self, label):
        self.defaultDimW= 128
        self.defaultDimH=128
        self.character= label

    def chageCharacter(self,label):
        self.character=label

    def moveAnimation(self, characterLabel, direction):
        animationMoveRight = QtCore.QPropertyAnimation(characterLabel, 'geometry') # Create the animation for specific characterLabel
        animationMoveRight.setDuration(1000)
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
        animationMoveRight.setStartValue(QtCore.QRect(x1, y1 , w1, h1)) # Original QRect Properties of characterLabel
        animationMoveRight.setEndValue(QtCore.QRect(x2, y1, w1, h1)) # QRect Properties after animation of characterLabel
        characterLabel.setGeometry(QtCore.QRect(x2, y1, w1, h1)) #Change label x coordinate

        return  animationMoveRight
    """
    def moveAnimation(self,imageLabel,direction):
        if direction=="right":
            for i in range(0,30):
                imageLabel.move(imageLabel.x() + 4, imageLabel.y())
                imageLabel.repaint()
                app.processEvents()
        elif direction=="left":
            for i in range(0,30):
                imageLabel.move(imageLabel.x() - 4, imageLabel.y())
                imageLabel.repaint()
                app.processEvents()


    def runAnimation(self,imageLabel,direction):
        if direction=="right":
            for i in range(0,30):
                imageLabel.move(imageLabel.x() + 6, imageLabel.y())
                imageLabel.repaint()
                app.processEvents()
        elif direction=="left":
            for i in range(0,30):
                imageLabel.move(imageLabel.x() - 6, imageLabel.y())
                imageLabel.repaint()
                app.processEvents()
    """
    def runAnimation(self,characterLabel,direction):
        animationMoveRight = QtCore.QPropertyAnimation(characterLabel, 'geometry') # Create the animation for specific characterLabel
        animationMoveRight.setDuration(500)
        if direction=="right":
            x1 = characterLabel.x()
            x2 = characterLabel.x() - 100
            y1 = characterLabel.y()
            w1 = characterLabel.width()
            h1 = characterLabel.height()
        else:
            x1 = characterLabel.x()
            x2 = characterLabel.x() - 100
            y1 = characterLabel.y()
            w1 = characterLabel.width()
            h1 = characterLabel.height()
        animationMoveRight.setStartValue(QtCore.QRect(x1, y1 , w1, h1)) # Original QRect Properties of characterLabel
        animationMoveRight.setEndValue(QtCore.QRect(x2, y1, w1, h1)) # QRect Properties after animation of characterLabel
        characterLabel.setGeometry(QtCore.QRect(x2, y1, w1, h1)) #Change label x coordinate

        return  animationMoveRight
    """
    def jumpAnimation(self,imageLabel):
            for i in range(0,20):
                imageLabel.move(imageLabel.x(), imageLabel.y()-4)
                imageLabel.repaint()
                app.processEvents()
            for i in range(0,20):
                imageLabel.move(imageLabel.x(), imageLabel.y()+4)
                imageLabel.repaint()
                app.processEvents()
    """
    def jumpAnimation(self,characterLabel,direction):
        animationMoveRight = QtCore.QPropertyAnimation(characterLabel, 'geometry') # Create the animation for specific characterLabel
        animationMoveRight.setDuration(500)
        if direction=="up":
            x1 = characterLabel.x()
            x2 = characterLabel.x()
            y1 = characterLabel.y()
            y2 = characterLabel.y()+40
            w1 = characterLabel.width()
            h1 = characterLabel.height()
        else:
            x1 = characterLabel.x()
            x2 = characterLabel.x()
            y1 = characterLabel.y()
            y2 = characterLabel.y()-40
            w1 = characterLabel.width()
            h1 = characterLabel.height()

        animationMoveRight.setStartValue(QtCore.QRect(x1, y1 , w1, h1)) # Original QRect Properties of characterLabel
        animationMoveRight.setEndValue(QtCore.QRect(x2, y2, w1, h1)) # QRect Properties after animation of characterLabel
        characterLabel.setGeometry(QtCore.QRect(x2, y2, w1, h1)) #Change label x coordinate

        return  animationMoveRight

    def shrinkCharacter(self,characterLabel):
        animationMoveRight = QtCore.QPropertyAnimation(characterLabel, 'geometry') # Create the animation for specific characterLabel
        animationMoveRight.setDuration(500)
        if characterLabel.height>30 and characterLabel.width>30:
            x1 = characterLabel.x()
            y1 = characterLabel.y()
            w1 = characterLabel.width()
            h1 = characterLabel.height()
            w2 = characterLabel.width()-20
            h2 = characterLabel.height()-20

        animationMoveRight.setStartValue(QtCore.QRect(x1, y1 , w1, h1)) # Original QRect Properties of characterLabel
        animationMoveRight.setEndValue(QtCore.QRect(x1, y1, w2, h2)) # QRect Properties after animation of characterLabel
        characterLabel.setGeometry(QtCore.QRect(x1, y1, w2, h2)) #Change label x coordinate

        return  animationMoveRight

    def growCharacter(self,characterLabel):
        animationMoveRight = QtCore.QPropertyAnimation(characterLabel, 'geometry') # Create the animation for specific characterLabel
        animationMoveRight.setDuration(500)
        if characterLabel.height<180 and characterLabel.width>180:
            x1 = characterLabel.x()
            y1 = characterLabel.y()
            w1 = characterLabel.width()
            h1 = characterLabel.height()
            w2 = characterLabel.width()+20
            h2 = characterLabel.height()+20

        animationMoveRight.setStartValue(QtCore.QRect(x1, y1 , w1, h1)) # Original QRect Properties of characterLabel
        animationMoveRight.setEndValue(QtCore.QRect(x1, y1, w2, h2)) # QRect Properties after animation of characterLabel
        characterLabel.setGeometry(QtCore.QRect(x1, y1, w2, h2)) #Change label x coordinate

        return  animationMoveRight



    """
    def shrinkCharacter(self,imageLabel):
        self.width=imageLabel.width()
        self.height=imageLabel.height()
        for i in range(0,30):
            if(imageLabel.height>10 and imageLabel.width>10):
                imageLabel.resize(self.width-i, self.height-i)
                imageLabel.repaint()
                app.processEvents()


    def growCharacter(self,imageLabel):
        self.width=imageLabel.width()
        self.height=imageLabel.height()
        for i in range(0,30):
            if(imageLabel.height<200 and imageLabel.width<200):
                imageLabel.resize(self.width+i, self.height+i)
                imageLabel.repaint()
                app.processEvents()
    """

    def grow(self):
        self.growCharacter(self.character)

    def shrink(self):
        self.shrinkCharacter(self.character)

    def moveLeft(self):
        self.moveAnimation(self.character,"left")

    def moveRight(self):
        self.moveAnimation(self.character,"right")

    def runLeft(self):
        self.runAnimation(self.character,"left")

    def runRight(self):
        self.runAnimation(self.character,"right")

    def jump(self):
        self.jumpAnimation(self.character,"up")
        self.jumpAnimation(self.character,"down")



