import socket,threading, time, pickle
from PyQt4 import QtGui, QtCore

class Cliente(QtCore.QThread):
    def __init__(self, gui,dir):
        super(Cliente,self).__init__()
        self.gui=gui
        try:
            self.c = socket.socket() 
            self.c.connect((dir,9999))
            self.gui.statusBar().showMessage("Conectado como cliente")
            self.gui.cargarC()
            self.gui.modo="cliente"
        except Exception as e:
            self.c.close()
        
    def run(self):
        while True:
            self.cad = self.c.recv(100)
            self.gui.actual.setText("Jugador actual: Negras")
            with open("datosc.dat","wb") as f:
                f.write(self.cad)
            f = file("datosc.dat","rb")
            self.gui.turno = pickle.load(f)
            print self.gui.turno
            if self.gui.turno == True:
                self.gui.rein()
            else:
                x = pickle.load(f)
                y = pickle.load(f)
                self.gui.matriz[x][y].setIcon(QtGui.QIcon(""))
                self.gui.matriz[x][y].setNombre("vacio")
                self.gui.matriz[x][y].setColorPieza("vacio") 
                x2 = pickle.load(f)
                y2 = pickle.load(f)
                print x2, y2
                nombre = pickle.load(f)
                print "llego bien 1"
                self.gui.matriz[x2][y2].setIcon(QtGui.QIcon("images/"+nombre+".gif"))
                self.gui.matriz[x2][y2].setNombre(nombre)
                self.gui.matriz[x2][y2].setColorPieza("blancas")
            time.sleep(0.1)
        