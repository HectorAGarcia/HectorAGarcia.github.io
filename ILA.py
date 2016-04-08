#Command Check
class CommandCheck():
    def __init__(self,cmdList):
        self.commands=cmdList


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



#Command Class
class Command():
    def __init__(self,Name,nAtributes,executable):
        self.name=Name
        self.nAtributes=nAtributes
        self.executable=executable


    def getName(self):
        return self.name

    def getNAtributes(self):
        return self.nAtributes

    def getExe(self):
        return self.executable



#CommandProccessor
class CommandProccesor():

    def __init__(self):
        self.commands={}
        self.loadCommands()
        self.cmdcheck= CommandCheck(self.commands)

    def execute(self, cmd, natributes,target):
        valid=self.cmdcheck.validCommand(cmd,natributes)
        if valid=="":
                self.commands[cmd].getExe()(target)
        else:
            print valid


    def addCommand(self,Name, natributes,executable):
        self.commands[Name]=Command(Name,natributes,executable)

    def loadCommands(self):
        self.addCommand("jump",0,jumpexe)
        self.addCommand("sing",0, singexe)



#Commands executables

def jumpexe(target):
    print target.getValue()+" jump!"

def singexe(target):
    print target.getValue()+" Sing!"

def domathexe(op,target):

#Math operations:
def sum(target):






#Tokenizer

class Tokenizer():
    def __init__(self):
        self.setUpTokenizer()
        self.interrupt=Interrupt()
        self.word=False

    def tokenize(self,line):
        items=line.split(" ")
        tokens=[]
        self.word=False

        for token in items:
            if not self.interrupt.checkFlag():
                item=self.checkToken(token)
                if item !="":
                    tokens.append(item)
                else:
                    print "Not valid token: "+str(token)
        if self.interrupt.checkFlag():
            self.interrupt.executeISR(self,tokens,items)

        if len(items)!= len(tokens) and (not self.word):
            print "Operation can't be completed"
            return tokens
        else:
            return tokens



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
        return ''


    def setUpTokenizer(self):
        self.characters=["fish",'lion','bird']
        self.commands=["sing","dance","jump","walk",'say','grow','shrink','flip','run','domath']
        self.atributes=["right",'left']
        self.operators=["+","-","*"]

    def if_character(self,token):
        for character in self.characters:
            if token == character:
                return True
        return False

    def if_command(self,token):
        for command in self.commands:
            if token == command:
                return True
        return False

    def if_atribute(self,token):
        for atribute in self.atributes:
            if token == atribute:
                return True
        return False

    def if_word(self,token):
        if token=="Word":
            return True
        return False

    def if_Math(self,token):
        if token=="domath":
            return True
        return False

    def toString(self, items):
        token=''
        for item in items[2:]:
            token=token+" "+item
        return self.createToken(token[2:len(token)-1],"String")

    def validateOP(self,op):
        for oper in self.operators:
            if op == oper:
                return True
        return False


    def createToken(self,value,ID):
        token=Token(value)
        token.setID(ID)
        return token

#token object
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


#Compiler

class Compiler():
    def __init__(self):
        self.tokenizer=Tokenizer()
        self.loadValidStatements()
        self.cmdPC= CommandProccesor()

    def loadValidStatements(self):
        self.statements=[]
        statement1=['character','command','atribute']
        statement2=['character','command']
        statement3=['Word','Name','String']
        self.statements.append(statement1)
        self.statements.append(statement2)
        self.statements.append(statement3)

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

    def compile(self, line):
        tokens=self.tokenizer.tokenize(line)
        if self.checkIFValidStatement(tokens):
            self.printStatement(tokens)
            index=self.find_cmd(tokens)

            if index!=-1:
                self.cmdPC.execute(tokens[index].getValue(),self.count_atributes(tokens),tokens[0])

        else:
            print "Not valid statement!"

    def printStatement(self, tokens):
        out=""
        for item in tokens:
            out=out+item.getID()+": "+item.getValue()+" "
        print out

    def count_atributes(self,tokens):
        count=0
        for token in tokens:
            if token.getID()=="atribute":
                count+=1
        return count

    def find_cmd(self,tokens):
        index=0
        for token in tokens:
            if token.getID()=="command":
                return index
            index+=1
        return -1



class Interrupt():
    def __init__(self):
        self.flag=0
        self.flagName=""
        self.ISR={"Word":self.WordISR,"Math": self.MathISR}

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
        self.clrFlag()



    def WordISR(self,instance,tokens, items):
        tokens.append(instance.createToken(items[1],"Name"))
        if len(items) > 2 and instance.checkifStringRule(items):
            tokens.append(instance.toString(items))
        self.clrFlag()

    def MathISR(self,instance,tokens,items):
        list=[]
        if instance.validateOP(items[2]):
            tokens.append(instance.createToken(items[2],"Operator"))
            for item in items[3:]:
                if item !="":
                    list.append(item)
            instance.createToken(list,"List")
            self.clrFlag()



compiler=Compiler()
while True:
   s=raw_input("cmd> ")
   compiler.compile(s)