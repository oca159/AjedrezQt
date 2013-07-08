from PyQt4 import QtGui,QtCore
class Button(QtGui.QPushButton):
    def __init__(self):
        super(Button,self).__init__()
        self.nombre="vacio"
        self.color="vacio"
        self.colorPieza="vacio"
        self.coor=QtCore.QPoint(0,0)
    
    def getNombre(self):
        return self.nombre
    def setNombre(self,nombre):
        self.nombre=nombre

    def setBackGroundCyan(self):
        self.setStyleSheet("QPushButton {background-color: cyan ; border: 1px solid black; }")
        self.color="cyan"
    
    def getColor(self):
        return self.color
    def setColor(self,color):
        self.color=color
    
    def getColorPieza(self):
        return self.colorPieza
    def setColorPieza(self,colorPieza):
        self.colorPieza=colorPieza
        
    def getCoor(self):
        return self.coor
    def setCoor(self,coor):
        self.coor=coor