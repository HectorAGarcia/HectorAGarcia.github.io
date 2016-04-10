import sys
from PyQt4 import QtGui, QtCore
from PyQt4.QtGui import QWidget, QMainWindow


class Animator():
    def __init__(self, label):
        self.defaultDimW= 128
        self.defaultDimH=128
        self.character= label

    def chageCharacter(self,label):
        self.character=label

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

    def jumpAnimation(self,imageLabel):
            for i in range(0,20):
                imageLabel.move(imageLabel.x(), imageLabel.y()-4)
                imageLabel.repaint()
                app.processEvents()
            for i in range(0,20):
                imageLabel.move(imageLabel.x(), imageLabel.y()+4)
                imageLabel.repaint()
                app.processEvents()

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
        self.jumpAnimation(self.character)




app = QtGui.QApplication(sys.argv)



sys.exit(app.exec_())
