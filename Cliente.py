import socket,threading, time, pickle
from PyQt4 import QtGui

class Cliente(threading.Thread):
    def __init__(self, gui,dir):
        threading.Thread.__init__(self)
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
        try:
            while True:
                self.cad = self.c.recv(80)
                self.gui.actual.setText("Jugador actual: Negras")
                with open("datosc.dat","wb") as f:
                    f.write(self.cad)
                f = file("datosc.dat")
                self.gui.turno = pickle.load(f)
                if self.gui.turno == True:
                    self.gui.rein()
                else:
                    x= pickle.load(f)
                    y=pickle.load(f)
                    self.gui.matriz[x][y].setIcon(QtGui.QIcon(""))
                    self.gui.matriz[x][y].setNombre("vacio")
                    self.gui.matriz[x][y].setColorPieza("vacio")
                    x2 = pickle.load(f)
                    y2 = pickle.load(f)
                    nombre = pickle.load(f)
                    color = pickle.load(f)
                    self.gui.matriz[x2][y2].setIcon(QtGui.QIcon("images/"+nombre+".gif"))
                    self.gui.matriz[x2][y2].setNombre(nombre)
                    self.gui.matriz[x2][y2].setColorPieza(color)
                time.sleep(0.1)
        except:
            pass