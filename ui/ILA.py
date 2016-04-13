
from imagi_mainwindow import *
from PyQt4 import *



"""
---------------------------------Command Check -------------------------------------------
"""
class CommandCheck():
    def __init__(self,cmdList):
        self.commands=cmdList

    # - Name: name of command that is wanted to be execute
    # - nAtributes: number of tokens that are identified as atribute
    # - validCommand: check if the given command is valid
    def validCommand(self,Name,nAtributes):
        if self.validName(Name):
            if self.validNAtributes(Name,nAtributes):
                return ""
            else:
                return "Illegal Number of Atributes: "+str(nAtributes)
        return "Not valid command: "+Name


    def validName(self,Name):
        for key in self.commands.keys():
            if key == Name:
                return True
        return False

    def validNAtributes(self,Name,nAtributes):
        if self.commands[Name].getNAtributes()==nAtributes:
            return True
        return False



"""
 -------------------------Command Class------------------------------------------------
"""
class Command():
    def __init__(self,Name,nAtributes,executable):
        self.name=Name
        self.nAtributes=nAtributes
        self.executable=executable

    # -getName: returns the name of the command
    def getName(self):
        return self.name

    # -getNAtributes: return the number of atributes that are suposed to be indentified as atributes
    def getNAtributes(self):
        return self.nAtributes

    # -getExe: return the name of the function to be executed by the command
    def getExe(self):
        return self.executable



"""
-----------------------------Command Proccesor Class------------------------------------------------
"""
class CommandProccesor():

    def __init__(self):
        self.commands={}
        self.loadCommands()
        self.cmdcheck= CommandCheck(self.commands)


    # -cmd: Name of the command to execute
    # -tokens: tokens that contain the information needed to execute the command
    def execute(self, cmd, natributes,tokens):
        valid=self.cmdcheck.validCommand(cmd,natributes)
        if valid=="":
            if cmd=="turn":
                window.run_partial()
                window.turn(window.characterDICT[tokens[0].getValue()].characterLabel,tokens[0].getValue())

            else:
                self.commands[cmd].getExe()(tokens)
        else:
            print valid

    #-addCommand: add a command to the list
    def addCommand(self,Name, natributes,executable):
        self.commands[Name]=Command(Name,natributes,executable)

    # -loadCommands: setup the command list
    def loadCommands(self):
        self.addCommand("jump",0,jumpexe)
        self.addCommand("sing",0, singexe)
        self.addCommand("domath",0,domathexe)
        self.addCommand("grow",0,growexe)
        self.addCommand("shrink",0,shrinkexe)
        self.addCommand("flip",0,flipexe)
        self.addCommand("walk",1,walkexe)
        self.addCommand("run",1,runexe)
        self.addCommand("turn",0,turnexe)
        self.addCommand("dance",0,danceexe)


"""
-------------------------Command Executables------------------------------------------------
"""

def jumpexe(tokens):
    characterDICT=window.get_characters_dict() # get window character dictionary
    window.animations[len(window.animations)]=window.jumpAnimation(characterDICT[tokens[0].getValue()].characterLabel,"up")
    window.group.addAnimation(window.animations[len(window.animations)-1])#add to the dictionary of animations the created QPropertyAnimation
    window.animations[len(window.animations)]=window.jumpAnimation(characterDICT[tokens[0].getValue()].characterLabel,"down")
    window.group.addAnimation(window.animations[len(window.animations)-1])#add to the dictionary of animations the created QPropertyAnimation

def singexe(tokens):
    print tokens[0].getValue()+" Sing!"

def danceexe(tokens):
    slightMoveexe(tokens, "right")
    slightMoveexe(tokens, "left")
    jumpexe(tokens)
    jumpexe(tokens)
    slightMoveexe(tokens, "right")
    slightMoveexe(tokens, "right")
    slightMoveexe(tokens, "left")
    slightMoveexe(tokens, "left")
    shrinkexe(tokens)
    growexe(tokens)
    jumpexe(tokens)

def slightMoveexe(tokens, direction):
    characterDICT=window.get_characters_dict() # get window character dictionary
    window.animations[len(window.animations)]=window.slightMove(characterDICT[tokens[0].getValue()].characterLabel, direction)
    window.group.addAnimation(window.animations[len(window.animations)-1])#add to the dictionary of animations the created QPropertyAnimation

def growexe(tokens):
    characterDICT=window.get_characters_dict() # get window character dictionary
    h=characterDICT[tokens[0].getValue()].characterLabel.height()
    if h<75:
        window.animations[len(window.animations)]=window.growCharacter(characterDICT[tokens[0].getValue()].characterLabel)
        window.group.addAnimation(window.animations[len(window.animations)-1])#add to the dictionary of animations the created QPropertyAnimation

def shrinkexe(tokens):
    characterDICT=window.get_characters_dict() # get window character dictionary
    h=characterDICT[tokens[0].getValue()].characterLabel.height()
    if h>65:
        window.animations[len(window.animations)]=window.shrinkCharacter(characterDICT[tokens[0].getValue()].characterLabel)
        window.group.addAnimation(window.animations[len(window.animations)-1])#add to the dictionary of animations the created QPropertyAnimation

def flipexe(tokens):
    print tokens[0].getValue()+" Flip!"

def turnexe(tokens):
    characterDICT=window.get_characters_dict() # get window character dictionary
    window.animations[len(window.animations)]=window.turn(characterDICT[tokens[0].getValue()].characterLabel,tokens[0].getValue())
    window.group.addAnimation(window.animations[len(window.animations)-1])#add to the dictionary of animations the created QPropertyAnimation


def runexe(tokens):
    characterDICT=window.get_characters_dict() # get window character dictionary
    x=characterDICT[tokens[0].getValue()].characterLabel.x()
    if tokens[2].getValue()=="right"and  x<(798-100):
        window.animations[len(window.animations)]=window.runAnimation(characterDICT[tokens[0].getValue()].characterLabel,tokens[2].getValue())
        window.group.addAnimation(window.animations[len(window.animations)-1])
    if tokens[2].getValue()=="left" and x>100:
        window.animations[len(window.animations)]=window.moveAnimation(characterDICT[tokens[0].getValue()].characterLabel,tokens[2].getValue())#add to the dictionary of animations the created QPropertyAnimation
        window.group.addAnimation(window.animations[len(window.animations)-1])

def walkexe(tokens):

    characterDICT=window.get_characters_dict() # get window character dictionary
    x=characterDICT[tokens[0].getValue()].characterLabel.x()
    if tokens[2].getValue()=="right" and x<(798-100):
        window.animations[len(window.animations)]=window.moveAnimation(characterDICT[tokens[0].getValue()].characterLabel,tokens[2].getValue())#add to the dictionary of animations the created QPropertyAnimation
        window.group.addAnimation(window.animations[len(window.animations)-1])

    if tokens[2].getValue()=="left" and x>100:
        window.animations[len(window.animations)]=window.moveAnimation(characterDICT[tokens[0].getValue()].characterLabel,tokens[2].getValue())#add to the dictionary of animations the created QPropertyAnimation
        window.group.addAnimation(window.animations[len(window.animations)-1])



def domathexe(tokens):
    if tokens[2].getValue()=="+":
        print sum(tokens[3].getValue())
    elif tokens[2].getValue()=="-":
        print sub(tokens[3].getValue())
    elif tokens[2].getValue()=="*":
        print mult(tokens[3].getValue())
    else:
        print div(tokens[3].getValue())


#Check Variables existance
def check_Num_Exist(name,list):

    for item in list.keys():
        if name == item:
            return True
    return False

#Math operations:

def sub(items):
    sub=0
    list=compiler.get_TokenizerNUMVAR()
    try:
        sub=int(items[0])
    except ValueError:
        if check_Num_Exist(items[0],list):
            sub=int(list[items[0]])
        else:
            return "Not valid variable: "+items[0]

    i=0
    try:
       i=int(items[1])
    except ValueError:
        if check_Num_Exist(items[1],list):
            i=int(list[items[1]])
        else:
            return "Not valid variable: "+items[1]

    sub=sub-i
    return sub


def mult(items):
    mult =1
    i =1
    list=compiler.get_TokenizerNUMVAR()
    for item in items:
        i=1
        try:
            i=int(item)
        except ValueError:
            if check_Num_Exist(item,list):
                i=int(list[item])
            else:
                return "Not valid variable: "+item
        mult=mult*i
    return mult

def div(items):
    d=0
    list=compiler.get_TokenizerNUMVAR()
    try:
        d=int(items[0])
    except ValueError:
        if check_Num_Exist(items[0],list):
            d=int(list[items[0]])
        else:
            return "Not valid variable: "+items[0]

    i=0
    try:
       i=int(items[1])
    except ValueError:
        if check_Num_Exist(items[1],list):
            i=int(list[items[1]])
        else:
            return "Not valid variable: "+items[1]

    d=d-i
    return d

def sum(items):
    sum=0
    i=0
    list=compiler.get_TokenizerNUMVAR()
    for item in items:
        i=0
        try:
            i=int(item)
        except ValueError:
            if check_Num_Exist(item,list):
                i=int(list[item])
            else:
                return "Not valid variable: "+item
        sum=sum+i
    return str(sum)




"""
-------------------------------Tokenizer Class-----------------------------------------------------------
"""

class Tokenizer():
    def __init__(self):
        self.setUpTokenizer()
        self.interrupt=Interrupt()
        self.WordVariables={}
        self.NumberVariables={}

    #-line: code line to tokenize
    #-tokenize: identify tokens on a code line and return it
    def tokenize(self,line):
        notready=line.split(" ")
        items=[]
        tokens=[]
        for item in notready:
            if item !="":
                items.append(item)

        self.interrupt.clrFlag()
        for token in items:
            if not self.interrupt.checkFlag():
                item=self.checkToken(token)
                if item !="":
                    tokens.append(item)
                else:
                    print "Not valid token: "+str(token)
        if self.interrupt.checkFlag():
            self.interrupt.executeISR(self,tokens,items)

        if len(items)!= len(tokens) and not self.interrupt.checkFlag():
            print "Operation can't be completed"
            return tokens
        else:
            return tokens


    #-checkifStringRule: verify if the given string is between quotes
    #-items: tokens that belong to the string
    def checkifStringRule(self,items):
        count =0
        if items[2][0]=='"':
            x=len(items[len(items)-1])
            if items[len(items)-1][x-1] =='"':
                for item in items:
                    for c in item:
                        if c =='"':
                            count+=1
        return count ==2

    #-checkToken: identify the token with the correct ID
    def checkToken(self, token):
        if self.if_character(token):
            return self.createToken(token,"character")
        if self.if_command(token) and token != "domath":
            return self.createToken(token,"command")
        if self.if_atribute(token):
            return self.createToken(token,"atribute")
        if self.if_word(token):
            self.interrupt.raiseFlag("Word")
            return self.createToken(token,"Word")
        if self.if_Math(token):
            self.interrupt.raiseFlag("Math")
            return self.createToken(token,"command")
        if self.if_Number(token):
            self.interrupt.raiseFlag("Number")
            return self.createToken(token,"Number")
        return ''

    #setUpTokenizer: setup the tokens to be identified
    def setUpTokenizer(self):
        self.characters=["fish",'lion','dog']
        self.commands=["sing","dance","jump","walk",'say','grow','shrink','flip','run','domath',"turn", "dance"]
        self.atributes=["right",'left']
        self.operators=["+","-","*","/"]

    #check if the token is Number type
    def if_Number(self,token):
        if token =="Number":
            return True
        return False

    #check if the token is a character
    def if_character(self,token):
        for character in self.characters:
            if token == character:
                return True
        return False

    #check if the token is a command
    def if_command(self,token):
        for command in self.commands:
            if token == command:
                return True
        return False

    #check if the token is a atribute
    def if_atribute(self,token):
        for atribute in self.atributes:
            if token == atribute:
                return True
        return False

    #check if token is Word type
    def if_word(self,token):
        if token=="Word":
            return True
        return False

    #check if token is domath command
    def if_Math(self,token):
        if token=="domath":
            return True
        return False

    #convert a list of items to string
    def toString(self, items):
        token=''
        for item in items[2:]:
            token=token+" "+item
        return self.createToken(token[2:len(token)-1],"String")

    #check if the operation given is valid
    def validateOP(self,op):
        for oper in self.operators:
            if op == oper:
                return True
        return False

    #returns the dictionary containing all the Word type variables
    def getWordDict(self):
        return self.WordVariables

    #returns the dictionary containinf all the Number type variables
    def getNumberDict(self):
        return self.NumberVariables

    #create a token with the given value and the corresponding ID
    def createToken(self,value,ID):
        token=Token(value)
        token.setID(ID)
        return token

"""
---------------------------------------Token Class---------------------------------------------
"""
class Token():

    def __init__(self,value):
        self.value=value
        self.ID=""

    def getID(self):
        return self.ID

    def getValue(self):
        return self.value

    def setID(self,ID):
        self.ID=ID


"""
-------------------------------------Compiler Class--------------------------------------
"""
class Compiler():
    def __init__(self):
        self.tokenizer=Tokenizer()
        self.loadValidStatements()
        self.cmdPC= CommandProccesor()

    def set_comp(self,window):
        set_compiler(window.get_window_compiler())

    # -loadValidStatements: define the statements accepted
    def loadValidStatements(self):
        self.statements=[] #List of staments that are accepted
        statement1=['character','command','atribute']
        statement2=['character','command']
        statement3=['Word','Name','String']
        statement4=['Number','Name','Value']
        statement5=['character','command','Operator','List']
        self.statements.append(statement1) #add statement to list
        self.statements.append(statement2)
        self.statements.append(statement3)
        self.statements.append(statement4)
        self.statements.append(statement5)

    # -checkIFValidStatement : check if the statement given is valid
    def checkIFValidStatement(self,tokens):
        i=0
        valid=False
        while i < len(self.statements)and (not valid):
            j=0
            coincidence=0
            if len(self.statements[i])== len(tokens):
                while j<len(tokens) and (not valid):
                    if self.statements[i][j]==tokens[j].getID():
                        coincidence+=1
                    if coincidence == len(self.statements[i]):
                        valid=True
                    j+=1

            i+=1
        return valid

    #-line: line of code
    #-compile: compile the line of code supplied
    def compile(self, line):
        tokens=self.tokenizer.tokenize(line)
        if self.checkIFValidStatement(tokens):


            index=self.find_cmd(tokens)

            if index!=-1:
                self.cmdPC.execute(tokens[index].getValue(),self.count_atributes(tokens),tokens)

        else:
            print "Not valid statement!"

    #-tokens: tokens that belong to the code line
    # count the number of atributes inside the token list
    def count_atributes(self,tokens):
        count=0
        for token in tokens:
            if token.getID()=="atribute":
                count+=1
        return count

    #find the index of the cmd on the token list
    def find_cmd(self,tokens):
        index=0
        for token in tokens:
            if token.getID()=="command":
                return index
            index+=1
        return -1

    #returns the dictionary containing the Number type variables
    def get_TokenizerNUMVAR(self):
        return self.tokenizer.getNumberDict()


"""
------------------------------------Interrupt Class-------------------------------------------
"""
class Interrupt():
    def __init__(self):
        self.flag=0
        self.flagName=""
        self.ISR={"Word":self.WordISR,"Math": self.MathISR,"Number":self.NumberISR}


    def raiseFlag(self,name):
        self.flag=1
        self.flagName=name

    def clrFlag(self):
        self.flag=0
        self.flagName=""

    def checkFlag(self):
        return self.flag==1

    def executeISR(self, instance,tokens,items):
        self.ISR[self.flagName](instance,tokens,items)



    def NumberISR(self,instance,tokens,items):
        if len(items)==3:
             tokens.append(instance.createToken(items[1],"Name"))
             tokens.append(instance.createToken(items[2],"Value"))
             instance.NumberVariables[items[1]]=items[2]


    def WordISR(self,instance,tokens, items):

        if len(items) > 2 and instance.checkifStringRule(items):
            tokens.append(instance.createToken(items[1],"Name"))
            tokens.append(instance.toString(items))
            instance.WordVariables[items[1]]=tokens[len(tokens)-1].getValue()
            print instance.getWordDict()


    def MathISR(self,instance,tokens,items):
        list=[]
        if len(items)> 3:
            if instance.validateOP(items[2]):
                tokens.append(instance.createToken(items[2],"Operator"))
                if len(items) == 5:
                      for item in items[3:]:
                          if item !="":
                              list.append(item)
                      if len(list)==2:
                          tokens.append(instance.createToken(list,"List"))
        if len(tokens) < 3:
            tokens.append(instance.createToken("not valid","String"))

def set_window(w):
    global window
    window = w



def set_compiler(wcompiler):
    global  compiler
    compiler = wcompiler

