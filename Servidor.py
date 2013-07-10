import socket,threading,time,pickle
from PyQt4 import QtGui, QtCore

class Servidor(QtCore.QThread):
    def __init__(self, gui):
        super(Servidor,self).__init__()
        self.gui=gui
        self.signal=QtCore.SIGNAL("signal")
        self.sig=QtCore.SIGNAL("senal")
        try:
            s = socket.socket()
            s.bind(("localhost",9999))
            s.listen(1)
            self.sc, dir = s.accept()
            self.gui.cargarC()
            self.gui.modo="servidor"
            self.gui.statusBar().showMessage("Conectado como servidor")
            s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        except Exception:
            s.close()
        except:
            self.sc.close()
            s.close()
        
    def run(self):
        while True:
            self.cad = self.sc.recv(100)
            self.gui.actual.setText("Jugador actual: Blancas")
            with open("datoss.dat",'wb') as f:
                f.write(self.cad)
            f= file("datos.dat",'rb')
            self.gui.turno = pickle.load(f)
            if self.gui.turno == False:
                self.emit(QtCore.SIGNAL("reiniciarJuego"))
            else:
                x= pickle.load(f)
                y=pickle.load(f)
                self.gui.matriz[x][y].setIcon(QtGui.QIcon(""))
                self.gui.matriz[x][y].setNombre("vacio")
                self.gui.matriz[x][y].setColorPieza("vacio")
                x2 = pickle.load(f)
                y2 = pickle.load(f)
                nombre = pickle.load(f)
                if self.gui.matriz[x2][y2].getNombre()=="reyB":
                    self.emit(self.sig)
                    continue
                image=QtGui.QImage()
                image.load(QtCore.QString.fromUtf8("images/"+nombre+".gif"))
                self.emit(self.signal,image,x2,y2)
                self.gui.matriz[x2][y2].setNombre(nombre)
                self.gui.matriz[x2][y2].setColorPieza("negras")
            time.sleep(0.1)
    
    