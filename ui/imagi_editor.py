from PyQt4 import QtGui
from PyQt4.QtGui import *
import sys
import imagi_syntax

app = QtGui.QApplication([])

# Main Window
window = QMainWindow()

# Code editor
editor = QtGui.QTextEdit
editor.setLineWrapMode(QTextEdit.NoWrap)

font = QFont()
font.setFamily('Consolas')
font.setFixedPitch(True)
font.setPointSize(14)
editor.setFont(font)

p = editor.palette()
p.setColor(QPalette.Base, QColor(204, 239, 255))
editor.setPalette(p)

highlight = imagi_syntax.ImagiHighlighter(editor.document())


# Scene Display
# scene = QtGui.QGraphicsView(window)

editor.show()
# scene.show()

app.exec_()