#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt4 import QtGui, QtCore
import sys,Button, pickle
import Movimientos as mov
import Cliente, Servidor

class Gui(QtGui.QMainWindow):
    """Ajedrez Sencillo.
    
    """
    def __init__(self):
        super(Gui, self).__init__()
        self.setWindowTitle("Ajedrez")
        self.setGeometry(0, 0, 500, 500)
        self.wid = QtGui.QFrame(self)
        self.wid.resize(400, 400)
        self.modo=""
        self.reiniciar=QtGui.QPushButton("Reiniciar",self)
        self.reiniciar.setGeometry(390,450,60,25)
        self.reiniciar.clicked.connect(self.reiniciarJuego)
        self.actual=QtGui.QLabel("Jugador actual: Blancas",self)
        self.actual.setGeometry(20,450,150,30)
        self.rendirse=QtGui.QPushButton("Rendirse",self)
        self.rendirse.setGeometry(300,450,60,25)
        self.rendirse.clicked.connect(self.rendir)
        self.coronaB=QtCore.QStringList(["reinaB","caballoB","alfilB","torreB"])
        self.coronaR=QtCore.QStringList(["reinaR","caballoR","alfilR","torreR"])
        
        self.statusBar().showMessage("Escoge conectar como servidor o cliente")
        
        cliente=QtGui.QAction("Conectar como Cliente",self)
        cliente.triggered.connect(self.conectaCliente)
        
        servidor=QtGui.QAction("Conectar como Servidor",self)
        servidor.triggered.connect(self.conectaServidor)
        
        menu=self.menuBar()
        conectar=menu.addMenu("&Conectar")
        conectar.addAction(cliente)
        conectar.addAction(servidor)
        self.show()

    def cargarC(self):
        self.turno=True
        self.actual.setText("Jugador actual: Blancas")
        self.grid = QtGui.QGridLayout()
        self.nombresPiezas = [(
            "torreR", "caballoR", "alfilR", "reyR", "reinaR", "alfilR", "caballoR", "torreR"),
            ("peonR", "peonR", "peonR", "peonR", "peonR",
             "peonR", "peonR", "peonR", "peonR"),
            ("vacio", "vacio", "vacio", "vacio",
             "vacio", "vacio", "vacio", "vacio"),
            ("vacio", "vacio", "vacio", "vacio",
             "vacio", "vacio", "vacio", "vacio"),
            ("vacio", "vacio", "vacio", "vacio",
             "vacio", "vacio", "vacio", "vacio"),
            ("vacio", "vacio", "vacio", "vacio",
             "vacio", "vacio", "vacio", "vacio"),
            ("peonB", "peonB", "peonB", "peonB", "peonB",
             "peonB", "peonB", "peonB", "peonB"),
            ("torreB", "caballoB", "alfilB", "reyB", "reinaB", "alfilB", "caballoB", "torreB")]

        self.matriz = []
        self.lista = []
        for i in range(8):
            self.lista = []
            for j in range(8):
                self.boton = Button.Button()
                if i==0 or i==1:
                    self.boton.setColorPieza("negras")
                elif i==6 or i==7:
                    self.boton.setColorPieza("blancas")
                else:
                    self.boton.setColorPieza("vacio")
                self.boton.setMinimumSize(50, 50)
                self.boton.setCoor(QtCore.QPoint(i,j))
                self.boton.setIcon(QtGui.QIcon(
                    "images/" + self.nombresPiezas[i][j] + ".gif"))
                self.boton.setIconSize(QtCore.QSize(100, 100))
                self.boton.setNombre(self.nombresPiezas[i][j])
                self.lista.insert(j, self.boton)
                if j == 7:
                    self.matriz.insert(i, self.lista)

                tam = QtGui.QSizePolicy.Minimum
                self.boton.setSizePolicy(tam, tam)
                self.boton.clicked.connect(self.evalua)
                self.grid.addWidget(self.boton, i, j)

        self.grid.setSpacing(0)
        self.grid.setMargin(0)
        self.pintaTablero()
        self.wid.setLayout(self.grid)

    def evalua(self):
        source = self.sender()
        self.fila=source.coor.x()
        self.col=source.coor.y()
        
    ###Validaciones piezas blancas
    
        if self.turno and source.getColorPieza()=="blancas" and self.modo=="servidor":
            self.ant=source.getCoor()
            self.icono=source.icon()
            self.nombrePieza=source.getNombre()
            self.colorPieza=source.getColorPieza()
            self.pintaTablero()
            nombre=source.getNombre()
            if nombre=="peonB":
                if self.fila==6 and self.matriz[self.fila-1][self.col].getColorPieza()=="vacio" and self.matriz[self.fila-2][self.col].getColorPieza()=="vacio":
                    self.matriz[self.fila-1][self.col].setBackGroundCyan()
                    self.matriz[self.fila-2][self.col].setBackGroundCyan()
                    
                if self.matriz[self.fila-1][self.col].getColorPieza()=="vacio":
                    self.matriz[self.fila-1][self.col].setBackGroundCyan()
                if self.col>1 and self.matriz[self.fila-1][self.col-1].getColorPieza()=="negras":
                    self.matriz[self.fila-1][self.col-1].setBackGroundCyan()
                if self.col<7 and self.matriz[self.fila-1][self.col+1].getColorPieza()=="negras":
                    self.matriz[self.fila-1][self.col+1].setBackGroundCyan()
                    
            if nombre=="torreB":
                mov.validaTorre(self,source)
            
            if nombre=="alfilB":
                mov.validaAlfil(self,source)
            if nombre=="reinaB":
                mov.validaReina(self,source)
            if nombre=="reyB":
                mov.validaRey(self,source)
            if nombre=="caballoB":
                mov.validaCaballo(self,source)
                
                
                
        elif not(self.turno) and source.getColorPieza()=="negras" and self.modo=="cliente":
            self.ant=source.getCoor()
            self.icono=source.icon()
            self.nombrePieza=source.getNombre()
            self.colorPieza=source.getColorPieza()
            self.pintaTablero()
            nombre=source.getNombre()
            if nombre=="peonR":
                if self.fila==1 and self.matriz[self.fila+1][self.col].getColorPieza()=="vacio" and self.matriz[self.fila+2][self.col].getColorPieza()=="vacio":
                    self.matriz[self.fila+1][self.col].setBackGroundCyan()
                    self.matriz[self.fila+2][self.col].setBackGroundCyan()
                    
                if self.matriz[self.fila+1][self.col].getColorPieza()=="vacio":
                    self.matriz[self.fila+1][self.col].setBackGroundCyan()
                if self.col>1 and self.matriz[self.fila+1][self.col-1].getColorPieza()=="blancas":
                    self.matriz[self.fila+1][self.col-1].setBackGroundCyan()
                if self.col<7 and self.matriz[self.fila+1][self.col+1].getColorPieza()=="blancas":
                    self.matriz[self.fila+1][self.col+1].setBackGroundCyan()
                                    
            if nombre=="torreR":
                mov.validaTorre(self,source)
            
            if nombre=="alfilR":
                mov.validaAlfil(self,source)
            if nombre=="reinaR":
                mov.validaReina(self,source)
            if nombre=="reyR":
                mov.validaRey(self,source)
            if nombre=="caballoR":
                mov.validaCaballo(self,source)
            
        elif source.getColor()=="cyan":
            if source.getNombre()=="reyB" or source.getNombre()=="reyR":
                self.turno=not(self.turno)
                self.rendir()
                
                
            
            self.matriz[self.ant.x()][self.ant.y()].setIcon(QtGui.QIcon(""))
            self.matriz[self.ant.x()][self.ant.y()].setNombre("vacio")
            self.matriz[self.ant.x()][self.ant.y()].setColorPieza("vacio")
            source.setIcon(self.icono)
            source.setNombre(self.nombrePieza)
            source.setColorPieza(self.colorPieza)
            self.act=source.getCoor()
            self.turno=not(self.turno)
            self.pintaTablero()
            if self.turno==True:
                self.actual.setText("Jugador actual: Blancas")
            else:
                self.actual.setText("Jugador actual: Negras")
                
            if (source.coor.x() == 0 and source.getNombre()=="peonB") or (source.coor.x() == 7 and source.getNombre()=="peonR"):
                if source.getNombre()=="peonB":
                    ok=False
                    while ok==False:
                        pieza, ok= QtGui.QInputDialog.getItem(self, "Coronar", "Escoge una pieza: ", self.coronaB)
                if source.getNombre()=="peonR":
                    ok=False
                    while ok==False:
                        pieza, ok= QtGui.QInputDialog.getItem(self, "Coronar", "Escoge una pieza: ", self.coronaR)
                
                source.setNombre(pieza)
                self.nombrePieza=pieza
                print self.nombrePieza
                source.setIcon(QtGui.QIcon("images/"+pieza+".gif"))
                
                    
            if self.modo=="cliente":
                with open("datos.dat","wb") as f:
                    pickle.dump(self.turno,f,2)
                    pickle.dump(self.ant.x(),f,2)  
                    pickle.dump(self.ant.y(),f,2)   
                    pickle.dump(self.act.x(),f,2)  
                    pickle.dump(self.act.y(),f,2)   
                    pickle.dump(self.nombrePieza,f,2)   
                    pickle.dump(self.colorPieza,f,2)   
                with open("datos.dat","rb") as f:
                    cad=f.read()
                    self.cliente.c.send(cad)
                    
                    
            if self.modo=="servidor": 
                with open("datos.dat","wb") as f:
                    pickle.dump(self.turno,f,2)
                    pickle.dump(self.ant.x(),f,2)  
                    pickle.dump(self.ant.y(),f,2)   
                    pickle.dump(self.act.x(),f,2)  
                    pickle.dump(self.act.y(),f,2)   
                    pickle.dump(self.nombrePieza,f,2)   
                    pickle.dump(self.colorPieza,f,2)    
                with open("datos.dat","rb") as f:
                    cad=f.read()
                    self.servidor.sc.send(cad)
                
                
    def pintaTablero(self):
        color = True
        for i in range(8):
            for j in range(8):
                boton = self.matriz[i][j]
                boton.setColor("vacio")
                if color:
                    if isinstance(boton, Button.Button):
                        boton.setStyleSheet(
                            "QPushButton { background-color: white; border:0px }")
                else:
                    if isinstance(boton, Button.Button):
                        boton.setStyleSheet(
                            "QPushButton { background-color: black; border:0px }")
                if j == 7:
                    color = not(color)
                color = not(color)
            
    def reiniciarJuego(self):
        self.wid.deleteLater()
        self.wid = QtGui.QFrame(self)
        self.wid.resize(400,400)
        self.wid.setVisible(True)
        self.cargarC()
        if self.modo=="servidor":
            reiniciado=True
            with open("datos.dat","wb") as f:
                pickle.dump(reiniciado, f, 2)  #Envio la bandera 
            with open("datos.dat","rb") as f:
                cad=f.read()
                self.servidor.sc.send(cad)
        else:
            reiniciado=False
            with open("datos.dat","wb") as f:
                pickle.dump(reiniciado, f, 2)  #Envio la bandera 
            with open("datos.dat","rb") as f:
                cad=f.read()
                self.cliente.c.send(cad)
        
    def rendir(self):
        if self.turno==True:
            QtGui.QMessageBox.information(self,"Ganador", "Ha ganado Negras")
        else:
            QtGui.QMessageBox.information(self,"Ganador","Ha ganado Blancas")
        self.reiniciarJuego()
        
    def conectaCliente(self):
        self.setWindowTitle("cliente")
        ok=False
        dir=""
        while not(ok) or dir == "":
            dir, ok=QtGui.QInputDialog.getText(self, "Conectar a", "Teclea la direccion a la que se desea conectar")
        
        self.cliente= Cliente.Cliente(self,dir)
        self.cliente.start()
    
    def conectaServidor(self):
        self.setWindowTitle("Servidor")
        self.servidor= Servidor.Servidor(self)
        self.servidor.start()
            
        
    def rein(self):
        self.wid.deleteLater()
        self.wid = QtGui.QFrame(self)
        self.wid.resize(400,400)
        self.wid.setVisible(True)
        self.cargarC()    
            
if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    Ventana = Gui()
    sys.exit(app.exec_())
