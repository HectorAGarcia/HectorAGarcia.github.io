import sys
from PyQt4 import QtGui, QtCore

class Window(QtGui.QMainWindow):
    def __init__(self):
        super(Window,self).__init__()
        self.buttons=[]
        self.menus={}
        self.items=[]
        self.images=[]
        self.images2=[]
        self.images3=[]
        self.scenes=[]
        self.imagecount=0
        self.scenecount=0
        self.setAspect()
        self.show()

    def setAspect(self):
        self.setGeometry(200,200,800,600)
        self.setFixedSize(800,600)
        self.setWindowTitle("IMAGI")
        icon = QtGui.QIcon("IMAGI-Logo-S.png")
        self.setWindowIcon(icon)
        self.setVisuals()
        self.setButtons()
        self.setImage()

    def setMenuBar(self):
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
        self.texto.move(x,y)


    def addLabel(self,msg,x,y,width,height):
        self.label = QtGui.QLabel(msg,self)
        self.items.append(self.label)
        self.label.setPixmap(QtGui.QPixmap(msg))
        self.label.resize(width,height)
        self.label.move(x,y)

    def addLabel1(self,msg,x,y,width,height):
        self.label = QtGui.QLabel(msg,self)
        self.images.append(self.label)
        self.label.setPixmap(QtGui.QPixmap(msg))
        self.label.resize(width,height)
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
        self.label.move(x,y)
        if len(self.scenes)>1:
            self.scenes[len(self.scenes)-1].setVisible(False)


    def nextScene(self):
        if self.scenecount<len(self.scenes)-1:
            self.scenes[self.scenecount].setVisible(False)
            self.scenecount+=1
            self.scenes[self.scenecount].setVisible(True)

    def lastScene(self):
        if self.scenecount>0:
            self.scenes[self.scenecount].setVisible(False)
            self.scenecount-=1
            self.scenes[self.scenecount].setVisible(True)

    def NextImage(self):
        if self.imagecount < len(self.images)-1:
            self.images[self.imagecount].setVisible(False)
            self.images2[self.imagecount].setVisible(False)
            self.images3[self.imagecount].setVisible(False)
            self.imagecount+=1
            self.images[self.imagecount].setVisible(True)
            self.images2[self.imagecount].setVisible(True)
            self.images3[self.imagecount].setVisible(True)

    def LastImage(self):
        if self.imagecount >0:
            self.images[self.imagecount].setVisible(False)
            self.images2[self.imagecount].setVisible(False)
            self.images3[self.imagecount].setVisible(False)
            self.imagecount-=1
            self.images[self.imagecount].setVisible(True)
            self.images2[self.imagecount].setVisible(True)
            self.images3[self.imagecount].setVisible(True)

    def setImage(self):
        pass

    def setButtons(self):
        self.addButton(600,150,"","next",self.NextImage)
        self.addButton(135,150,"","prev",self.LastImage)
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

    def Testing(self):
        print self.texto.toPlainText()
        self.texto.clear()

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
        self.addLabel1("Media/fish.png",320,75,128,128)
        self.addLabel1("Media/dog.png",320,75,128,128)
        self.addLabel1("Media/lion.png",320,75,128,128)
        self.addLabel2("Media/lion_converted.png",500,75,80,80)
        self.addLabel2("Media/fish_converted.png",500,75,80,80)
        self.addLabel2("Media/dog_converted.png",500,75,80,80)
        self.addLabel3("Media/dog_converted.png",200,75,80,80)
        self.addLabel3("Media/lion_converted.png",200,75,80,80)
        self.addLabel3("Media/fish_converted.png",200,75,80,80)
        self.addLabel4("Media/campo.png",340,360,120,120)
        self.addLabel4("Media/campo2.png",340,360,120,120)
        self.addLabel4("Media/sea.png",340,360,120,120)
        self.addLabel("Media/add.png",440,201,20,20)
        self.addLabel("Media/add.png",450,470,20,20)

    def setCharactersList(self):
        self.addCharacter("fish")
        self.addCharacter("dog")
        self.addCharacter("lion")

    def addCharacterToList(self,name):
        self.characters=[]
        self.characters.append(name)



app = QtGui.QApplication(sys.argv)
window = Window()



sys.exit(app.exec_())

