import socket,threading,time,pickle
from PyQt4 import QtGui

class Servidor(threading.Thread):
    def __init__(self, gui):
        threading.Thread.__init__(self)
        self.gui=gui
        try:
            s = socket.socket()
            s.bind(("localhost",9999))
            s.listen(1)
            self.sc, dir = s.accept()
            self.gui.cargarC()
            self.gui.modo="servidor"
            self.gui.statusBar().showMessage("Conectado como servidor")
            s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        except Exception as e:
            s.close()
        except:
            self.sc.close()
            s.close()
        
    def run(self):
        try:
            while True:
                self.cad = self.sc.recv(80)
                self.gui.actual.setText("Jugador actual: Blancas")
                with open("datoss.dat","wb") as f:
                    f.write(self.cad)
                f= file("datos.dat")
                self.gui.turno = pickle.load(f)
                if self.gui.turno == False:
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