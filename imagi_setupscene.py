import sys
from PyQt4 import QtGui, QtCore
from PyQt4.QtGui import QWidget


class Window(QWidget):
    def __init__(self):
        super(Window,self).__init__()
        self.defaultDimW= 128
        self.defaultDimH=128
        self.buttons=[]
        #self.menus={}
        self.items=[]
        #self.images=[]
        self.characters=[]
        self.scenes=[]
        self.imagecount=0
        self.scenecount=0
        self.setAspect()
        self.show()

    def setAspect(self):
        self.setGeometry(800,800,800,600)
        self.setFixedSize(700,250)
        self.setWindowTitle("IMAGI")
        icon = QtGui.QIcon("IMAGI-Logo-S.png")
        self.setWindowIcon(icon)
        self.setVisuals()
        self.setCharacterSelect()
        self.setSceneList()
        self.setButtons()


    """def setMenuBar(self):
        self.menu =self.menuBar()

    def addTab(self,name):
        self.menus[name[1:]]=self.menu.addMenu(name)

    def addSubMenu(self,parent, name,msg,Action):
        submenu = QtGui.QAction(name,self)
        submenu.setStatusTip(msg)
        submenu.triggered.connect(Action)
        parent.addAction(submenu)

    def addTextbox(self,x,y,width,height):
        self.texto=QtGui.QTextEdit(self)
        self.texto.resize(width,height)
        self.texto.move(x,y)"""


    def addLabel(self,msg,x,y,width,height):
        self.label = QtGui.QLabel(msg,self)
        self.items.append(self.label)
        self.label.setPixmap(QtGui.QPixmap(msg))
        self.label.resize(width,height)
        self.label.move(x,y)

    """def addLabel1(self,msg,x,y,width,height):
        self.label = QtGui.QLabel(msg,self)
        self.images.append(self.label)
        self.label.setPixmap(QtGui.QPixmap(msg))
        self.label.resize(width,height)
        self.label.setScaledContents(True)
        self.label.move(x,y)
        if len(self.images)>1:
            self.images[len(self.images)-1].setVisible(False)

    def addLabel2(self,msg,x,y,width,height):
        self.label = QtGui.QLabel(msg,self)
        self.images2.append(self.label)
        self.label.setPixmap(QtGui.QPixmap(msg))
        self.label.resize(width,height)
        self.label.move(x,y)
        if len(self.images2)>1:
            self.images2[len(self.images2)-1].setVisible(False)

    def addLabel3(self,msg,x,y,width,height):
        self.label = QtGui.QLabel(msg,self)
        self.images3.append(self.label)
        self.label.setPixmap(QtGui.QPixmap(msg))
        self.label.resize(width,height)
        self.label.move(x,y)
        if len(self.images3)>1:
            self.images3[len(self.images3)-1].setVisible(False)

    def addLabel4(self,msg,x,y,width,height):
        self.label = QtGui.QLabel(msg,self)
        self.scenes.append(self.label)
        self.label.setPixmap(QtGui.QPixmap(msg))
        self.label.resize(width,height)
        self.label.setScaledContents(True)
        self.label.move(x,y)
        if len(self.scenes)>1:
            self.scenes[len(self.scenes)-1].setVisible(False)"""

    def nextScene(self):
        if self.scenecount<len(self.scenes):
            self.scenes[self.scenecount].setVisible(False)
            if self.scenecount+1< len(self.scenes):
                self.scenecount+=1
                self.scenes[self.scenecount].setVisible(True)
            else:
                self.scenes[0].setVisible(True)
                self.scenecount=0

    def lastScene(self):
        if self.scenecount>=0:
            self.scenes[self.scenecount].setVisible(False)
            if self.scenecount-1<0:
                self.scenecount=len(self.scenes)-1
                self.scenes[self.scenecount].setVisible(True)
            else:
                self.scenecount-=1
                self.scenes[self.scenecount].setVisible(True)


    def NextCharacter(self):
        newImageCount=0
        for character in self.characters:
            character.setVisible(False)
        self.setCharacterLabel("center",self.characters[self.imagecount])
        if self.imagecount-1 >= 0:
            self.setCharacterLabel("left",self.characters[self.imagecount-1])
            newImageCount=self.imagecount-1
        else:
            self.setCharacterLabel("left",self.characters[len(self.characters)-1])
            newImageCount=len(self.characters)-1
        if self.imagecount+1<len(self.characters):
            self.setCharacterLabel("right",self.characters[self.imagecount+1])
        else:
            self.setCharacterLabel("right",self.characters[0])

        self.imagecount=newImageCount
        #self.moveimageAnimation(self.characters[self.imagecount], "right")
        self.jumpAnimation(self.characters[self.imagecount])

    def PrevCharacter(self):
        newImageCount=0
        for character in self.characters:
            character.setVisible(False)

        if self.imagecount>=0:
            if self.imagecount+1 < len(self.characters):
                self.setCharacterLabel("left",self.characters[self.imagecount+1])
                newImageCount=self.imagecount+1
            else:
                self.setCharacterLabel("left",self.characters[0])
                self.setCharacterLabel("center",self.characters[1])
                self.setCharacterLabel("right",self.characters[2])
                newImageCount=0
                self.imagecount=newImageCount
                return
            if self.imagecount+2 < len(self.characters):
                self.setCharacterLabel("center",self.characters[self.imagecount+2])
            else:
                self.setCharacterLabel("center",self.characters[0])
                self.setCharacterLabel("right",self.characters[1])
                self.imagecount=newImageCount
                return
            if self.imagecount+3 < len(self.characters):
                self.setCharacterLabel("right",self.characters[self.imagecount+3])
            else:
                self.setCharacterLabel("right",self.characters[0])
            self.imagecount=newImageCount
            self.moveimageAnimation(self.characters[self.imagecount], "left")
    """
    def LastImage(self):
        if self.imagecount >0:
            self.images[self.imagecount].setVisible(False)
            self.images2[self.imagecount].setVisible(False)
            self.images3[self.imagecount].setVisible(False)
            self.imagecount-=1
            self.images[self.imagecount].setVisible(True)
            self.images2[self.imagecount].setVisible(True)
            self.images3[self.imagecount].setVisible(True)"""

    def setButtons(self):
        self.addButton(600,150,"","next",self.NextCharacter)
        self.addButton(135,150,"","prev",self.PrevCharacter)
        self.addButton(600,400,"","next",self.nextScene)
        self.addButton(135,400,"","prev",self.lastScene)
        self.addButton(720,530,"","shutdown",self.exitApplication)

    #create Buttons
    def addButton(self,x,y,message,toolTip,Action):
        self.buttons.append(QtGui.QPushButton(message,self))
        self.buttons[len(self.buttons)-1].setToolTip(toolTip)
        self.buttons[len(self.buttons)-1].clicked.connect(Action)
        self.buttons[len(self.buttons)-1].move(x,y)
        self.buttons[len(self.buttons)-1].resize(50,50)
        self.buttons[len(self.buttons)-1].setStyleSheet("QPushButton{background: transparent;}")
    """
    def Testing(self):
        print self.texto.toPlainText()
        self.texto.clear()"""

    def exitApplication(self):
        sys.exit()

    def setVisuals(self):
        self.addLabel("Media/background.png",0,0,800,600)
        self.addLabel("Media/characters.png",290,20,300,40)
        self.addLabel("Media/left.png",120,110,128,128)
        self.addLabel("Media/right.png",590,110,128,128)
        self.addLabel("Media/left.png",120,360,128,128)
        self.addLabel("Media/right.png",590,360,128,128)
        self.addLabel("Media/shutdown.png",720,530,80,80)
        self.addLabel("Media/start.png",650,530,80,80)
        self.addLabel("Media/scenes.png",290,300,200,40)
        self.addLabel("Media/add.png",440,201,20,20)
        self.addLabel("Media/add.png",450,470,20,20)

    def setCharactersList(self):
        self.addCharacter("Media/fish.png", self.defaultDimW, self.defaultDimH)
        self.addCharacter("Media/dog.png", self.defaultDimW, self.defaultDimH )
        self.addCharacter("Media/lion.png", self.defaultDimW, self.defaultDimH)

    def setSceneList(self):
        self.addScene("Media/scene3.png", self.defaultDimW, self.defaultDimH)
        self.addScene("Media/scene2.png", self.defaultDimW, self.defaultDimH)
        self.addScene("Media/scene1.png", self.defaultDimW, self.defaultDimH)
        for scene in self.scenes:
            scene.setVisible(False)
        self.scenes[0].setVisible(True)

    def addScene(self, pathToMedia, width, height):
        self.label = QtGui.QLabel(pathToMedia,self)
        self.scenes.append(self.label)
        self.label.setPixmap(QtGui.QPixmap(pathToMedia))
        self.label.resize(width,height)
        self.label.move(340,360)
        self.label.setScaledContents(True)

    def addCharacter(self, pathToMedia, width, height):
        self.label = QtGui.QLabel(pathToMedia,self)
        self.characters.append(self.label)
        self.label.setPixmap(QtGui.QPixmap(pathToMedia))
        self.label.resize(width,height)
        self.label.setScaledContents(True)

    def setCharacterSelect(self):
        self.setCharactersList()
        if len(self.characters)>=2:
            self.setCharacterLabel("left", self.characters[0])
            self.setCharacterLabel("center", self.characters[1])
            self.setCharacterLabel("right", self.characters[2])

    def setCharacterLabel(self, pos, label):
        if pos=="center":
            label.move(320,75)
            label.resize(128,128)
        elif pos=="left":
            label.move(200,75)
            label.resize(80,80)
        elif pos=="right":
            label.move(500,75)
            label.resize(80,80)

        label.setVisible(True)



    """
    def addCharacterToList(self,name):
        self.characters=[]
        self.characters.append(name)"""

    def moveimageAnimation(self,imageLabel,direction):
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
    def jumpAnimation(self,imageLabel):
            for i in range(0,20):
                imageLabel.move(imageLabel.x(), imageLabel.y()-4)
                imageLabel.repaint()
                app.processEvents()
            for i in range(0,20):
                imageLabel.move(imageLabel.x(), imageLabel.y()+4)
                imageLabel.repaint()
                app.processEvents()
    def shrink(self,imageLabel):
        pass



app = QtGui.QApplication(sys.argv)
window = Window()



sys.exit(app.exec_())

