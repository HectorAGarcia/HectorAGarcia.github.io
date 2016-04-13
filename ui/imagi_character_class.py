from PyQt4.uic.uiparser import QtGui




class ImagiCharacter:
    """Base class for character in IMAGI"""
    active = False

    # Constructor
    def __init__(self, characterLabel):
        self.characterLabel = characterLabel

    # Returns true if character is currently activated to appear in the scene, false if not
    def isActive(self):
        return self.active

    # Sets the character as active or not in the scene
    def setActive(self, boolean):
        self.active = boolean

