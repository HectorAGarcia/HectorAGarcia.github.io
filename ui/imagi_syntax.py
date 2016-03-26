import sys
from PyQt4.QtCore import QRegExp
from PyQt4.QtGui import QColor, QTextCharFormat, QFont, QSyntaxHighlighter

def imagiformat(color, style=''):
    _color = QColor()
    _color.setNamedColor(color)
    _format = QTextCharFormat()
    _format.setForeground(_color)

    if 'bold' in style:
        _format.setFontWeight(QFont.Bold)

    return _format

STYLES = {
    'p_commands': imagiformat('red', 'bold'),
    'l_commands': imagiformat('green', 'bold'),
    'm_attributes': imagiformat('darkOrange', 'bold'),
    'types': imagiformat('blue', 'bold'),
    'operators': imagiformat('darkMagenta', 'bold')
}

class ImagiHighlighter(QSyntaxHighlighter):
    # Physical Commands
    p_commands = [
        'jump', 'walk', 'say',
        'turn', 'dance', 'sing',
        'grow', 'shrink', 'ask',
        'flip', 'run', 'time',
        'move'
    ]

    # Logic Commands
    l_commands = [
        'domultiple', 'repeat', 'domath'
    ]

    # move attributes
    m_attributes = [
        'left', 'right'
    ]

    types = [
        'word', 'number'
    ]

    operators = [
        '\+', '-', '\*', '/', '//'
    ]

    def __init__(self, document):
        QSyntaxHighlighter.__init__(self, document)

        rules = []

        rules += [(r'\b%s\b' % w, 0, STYLES['p_commands']) for w in ImagiHighlighter.p_commands]
        rules += [(r'\b%s\b' % w, 0, STYLES['l_commands']) for w in ImagiHighlighter.l_commands]
        rules += [(r'\b%s\b' % w, 0, STYLES['m_attributes']) for w in ImagiHighlighter.m_attributes]
        rules += [(r'\b%s\b' % w, 0, STYLES['types']) for w in ImagiHighlighter.types]
        rules += [(r'%s' % o, 0, STYLES['operators']) for o in ImagiHighlighter.operators]

        self.rules = [(QRegExp(pat), index, fmt) for (pat, index, fmt) in rules]

    def highlightBlock(self, text):
        for expression, nth, format in self.rules:

            index = expression.indexIn(text, 0)
            while index >= 0:
                index = expression.pos(nth)
                length = expression.cap(nth).length()
                self.setFormat(index, length, format)
                index = expression.indexIn(text, index + length)

        self.setCurrentBlockState(0)