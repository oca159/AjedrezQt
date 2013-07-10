import socket, time, pickle
from PyQt4 import QtGui, QtCore

class Cliente(QtCore.QThread):
    def __init__(self, gui, dir):
        super(Cliente,self).__init__()
        self.gui=gui
        self.signal=QtCore.SIGNAL("signal")
        self.sig=QtCore.SIGNAL("senal")
        try:
            self.c = socket.socket() 
            self.c.connect((dir,9999))
            self.gui.statusBar().showMessage("Conectado como cliente")
            self.gui.cargarC()
            self.gui.modo="cliente"
        except Exception:
            self.c.close()
        
    def run(self):
        while True:
            self.cad = self.c.recv(100)
            self.gui.actual.setText("Jugador actual: Negras")
            with open("datosc.dat","wb") as f:
                f.write(self.cad)
            f = file("datosc.dat","rb")
            self.gui.turno = pickle.load(f)
            if self.gui.turno == True:
                self.emit(self.sig)
            else:
                x = pickle.load(f)
                y = pickle.load(f)
                self.gui.matriz[x][y].setIcon(QtGui.QIcon(""))
                self.gui.matriz[x][y].setNombre("vacio")
                self.gui.matriz[x][y].setColorPieza("vacio") 
                x2 = pickle.load(f)
                y2 = pickle.load(f)
                nombre = pickle.load(f)
                if self.gui.matriz[x2][y2].getNombre()=="reyR":
                    self.emit(self.sig)
                    continue
                image=QtGui.QImage()
                image.load(QtCore.QString.fromUtf8("images/"+nombre+".gif"))
                self.emit(self.signal,image,x2,y2)
                self.gui.matriz[x2][y2].setNombre(nombre)
                self.gui.matriz[x2][y2].setColorPieza("blancas")
            time.sleep(0.1)
            
    def makeIcon(self,image,x2,y2):
        print "entro"
        pixmap=QtGui.QPixmap(50,50)
        pixmap.convertFromImage(image)
        self.gui.matriz[x2][y2].setIcon(QtGui.QIcon(pixmap))
        pass
        