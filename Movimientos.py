from PyQt4 import QtGui,QtCore

def validaTorre(self,source):
        j=self.col+1
        while j<8:
            if self.matriz[self.fila][j].getColorPieza() != source.getColorPieza() or self.matriz[self.fila][j].getColorPieza() == "vacio" :
                self.matriz[self.fila][j].setBackGroundCyan()
            if self.matriz[self.fila][j].getColorPieza() == "negras" or self.matriz[self.fila][j].getColorPieza() == "blancas" :
                break
            j += 1
            
        j=self.col-1
        while j>-1:
            if self.matriz[self.fila][j].getColorPieza() != source.getColorPieza() or self.matriz[self.fila][j].getColorPieza() == "vacio":
                self.matriz[self.fila][j].setBackGroundCyan()
            if self.matriz[self.fila][j].getColorPieza() =="negras" or self.matriz[self.fila][j].getColorPieza() == "blancas": 
                break
            j -= 1
            
        j=self.fila+1
        while j <8:
            if self.matriz[j][self.col].getColorPieza() != source.getColorPieza() or self.matriz[j][self.col].getColorPieza() == "vacio":
                self.matriz[j][self.col].setBackGroundCyan()
            if self.matriz[j][self.col].getColorPieza() =="negras" or self.matriz[j][self.col].getColorPieza() == "blancas": 
                break
            j += 1
        
        j=self.fila-1
        while j > -1:
            if self.matriz[j][self.col].getColorPieza() != source.getColorPieza() or self.matriz[j][self.col].getColorPieza() == "vacio":
                self.matriz[j][self.col].setBackGroundCyan()
            if self.matriz[j][self.col].getColorPieza() =="negras" or self.matriz[j][self.col].getColorPieza() == "blancas": 
                break
            j -= 1
    
def validaAlfil(self,source):
        
        i = self.fila+1
        j = self.col-1
        while i<8 and j> -1:
            if self.matriz[i][j].getColorPieza() != source.getColorPieza() or self.matriz[i][j].getColorPieza() == "vacio" :
                self.matriz[i][j].setBackGroundCyan()
            if self.matriz[i][j].getColorPieza() == "negras" or self.matriz[i][j].getColorPieza() == "blancas" :
                break
            i += 1
            j -= 1
        
        i = self.fila+1
        j = self.col+1
        while i<8 and j< 8:
            if self.matriz[i][j].getColorPieza() != source.getColorPieza() or self.matriz[i][j].getColorPieza() == "vacio" :
                self.matriz[i][j].setBackGroundCyan()
            if self.matriz[i][j].getColorPieza() == "negras" or self.matriz[i][j].getColorPieza() == "blancas" :
                break
            i += 1
            j += 1
            
        i = self.fila-1
        j = self.col-1
        while i> -1 and j> -1:
            if self.matriz[i][j].getColorPieza() != source.getColorPieza() or self.matriz[i][j].getColorPieza() == "vacio" :
                self.matriz[i][j].setBackGroundCyan()
            if self.matriz[i][j].getColorPieza() == "negras" or self.matriz[i][j].getColorPieza() == "blancas" :
                break
            i -= 1
            j -= 1
        
        i = self.fila-1
        j = self.col+1
        while i>-1 and j< 8:
            if self.matriz[i][j].getColorPieza() != source.getColorPieza() or self.matriz[i][j].getColorPieza() == "vacio" :
                self.matriz[i][j].setBackGroundCyan()
            if self.matriz[i][j].getColorPieza() == "negras" or self.matriz[i][j].getColorPieza() == "blancas" :
                break
            i -= 1
            j += 1
            
def validaReina(self,source):
        validaAlfil(self,source)
        validaTorre(self,source)
        
    
def validaRey(self,source):
        if self.fila >0 and self.fila <7 and self.col >0 and self.col <7:
            if self.matriz[self.fila+1][self.col].getColorPieza() != source.getColorPieza() or self.matriz[self.fila+1][self.col].getColorPieza() == "vacio":
                self.matriz[self.fila+1][self.col].setBackGroundCyan()
            if self.matriz[self.fila-1][self.col].getColorPieza() != source.getColorPieza() or self.matriz[self.fila-1][self.col].getColorPieza() == "vacio":
                self.matriz[self.fila-1][self.col].setBackGroundCyan()
            
            if self.matriz[self.fila][self.col+1].getColorPieza() != source.getColorPieza() or self.matriz[self.fila][self.col+1].getColorPieza() == "vacio":
                self.matriz[self.fila][self.col+1].setBackGroundCyan()
            if self.matriz[self.fila][self.col-1].getColorPieza() != source.getColorPieza() or self.matriz[self.fila][self.col-1].getColorPieza() == "vacio":
                self.matriz[self.fila][self.col-1].setBackGroundCyan()
            
            if self.matriz[self.fila-1][self.col+1].getColorPieza() != source.getColorPieza() or self.matriz[self.fila-1][self.col+1].getColorPieza() == "vacio":
                self.matriz[self.fila-1][self.col+1].setBackGroundCyan()
            if self.matriz[self.fila-1][self.col-1].getColorPieza() != source.getColorPieza() or self.matriz[self.fila-1][self.col-1].getColorPieza() == "vacio":
                self.matriz[self.fila-1][self.col-1].setBackGroundCyan()
            
            if self.matriz[self.fila+1][self.col+1].getColorPieza() != source.getColorPieza() or self.matriz[self.fila+1][self.col+1].getColorPieza() == "vacio":
                self.matriz[self.fila+1][self.col+1].setBackGroundCyan()
            if self.matriz[self.fila+1][self.col-1].getColorPieza() != source.getColorPieza() or self.matriz[self.fila+1][self.col-1].getColorPieza() == "vacio":
                self.matriz[self.fila+1][self.col-1].setBackGroundCyan()
        
        if self.fila ==0 and self.col >0 and self.col <7:
            if self.matriz[self.fila+1][self.col].getColorPieza() != source.getColorPieza() or self.matriz[self.fila+1][self.col].getColorPieza() == "vacio":
                self.matriz[self.fila+1][self.col].setBackGroundCyan()
            if self.matriz[self.fila][self.col+1].getColorPieza() != source.getColorPieza() or self.matriz[self.fila][self.col+1].getColorPieza() == "vacio":
                self.matriz[self.fila][self.col+1].setBackGroundCyan()
            if self.matriz[self.fila][self.col-1].getColorPieza() != source.getColorPieza() or self.matriz[self.fila][self.col-1].getColorPieza() == "vacio":
                self.matriz[self.fila][self.col-1].setBackGroundCyan()
            if self.matriz[self.fila+1][self.col+1].getColorPieza() != source.getColorPieza() or self.matriz[self.fila+1][self.col+1].getColorPieza() == "vacio":
                self.matriz[self.fila+1][self.col+1].setBackGroundCyan()
            if self.matriz[self.fila+1][self.col-1].getColorPieza() != source.getColorPieza() or self.matriz[self.fila+1][self.col-1].getColorPieza() == "vacio":
                self.matriz[self.fila+1][self.col-1].setBackGroundCyan()
        
        if self.fila ==7 and self.col >0 and self.col <7:
            if self.matriz[self.fila-1][self.col].getColorPieza() != source.getColorPieza() or self.matriz[self.fila-1][self.col].getColorPieza() == "vacio":
                self.matriz[self.fila-1][self.col].setBackGroundCyan()
            if self.matriz[self.fila][self.col+1].getColorPieza() != source.getColorPieza() or self.matriz[self.fila][self.col+1].getColorPieza() == "vacio":
                self.matriz[self.fila][self.col+1].setBackGroundCyan()
            if self.matriz[self.fila][self.col-1].getColorPieza() != source.getColorPieza() or self.matriz[self.fila][self.col-1].getColorPieza() == "vacio":
                self.matriz[self.fila][self.col-1].setBackGroundCyan()
            if self.matriz[self.fila-1][self.col+1].getColorPieza() != source.getColorPieza() or self.matriz[self.fila-1][self.col+1].getColorPieza() == "vacio":
                self.matriz[self.fila-1][self.col+1].setBackGroundCyan()
            if self.matriz[self.fila-1][self.col-1].getColorPieza() != source.getColorPieza() or self.matriz[self.fila-1][self.col-1].getColorPieza() == "vacio":
                self.matriz[self.fila-1][self.col-1].setBackGroundCyan()
        
        if self.fila ==0 and self.col ==0:
            if self.matriz[self.fila+1][self.col].getColorPieza() != source.getColorPieza() or self.matriz[self.fila+1][self.col].getColorPieza() == "vacio":
                self.matriz[self.fila+1][self.col].setBackGroundCyan()
            if self.matriz[self.fila][self.col+1].getColorPieza() != source.getColorPieza() or self.matriz[self.fila][self.col+1].getColorPieza() == "vacio":
                self.matriz[self.fila][self.col+1].setBackGroundCyan()
            if self.matriz[self.fila+1][self.col+1].getColorPieza() != source.getColorPieza() or self.matriz[self.fila+1][self.col+1].getColorPieza() == "vacio":
                self.matriz[self.fila+1][self.col+1].setBackGroundCyan()
        
        if self.fila ==7 and self.col ==0:
            if self.matriz[self.fila-1][self.col].getColorPieza() != source.getColorPieza() or self.matriz[self.fila-1][self.col].getColorPieza() == "vacio":
                self.matriz[self.fila-1][self.col].setBackGroundCyan()
            if self.matriz[self.fila][self.col+1].getColorPieza() != source.getColorPieza() or self.matriz[self.fila][self.col+1].getColorPieza() == "vacio":
                self.matriz[self.fila][self.col+1].setBackGroundCyan()
            if self.matriz[self.fila-1][self.col+1].getColorPieza() != source.getColorPieza() or self.matriz[self.fila-1][self.col+1].getColorPieza() == "vacio":
                self.matriz[self.fila-1][self.col+1].setBackGroundCyan()
        
        if self.fila ==0 and self.col ==7:
            if self.matriz[self.fila+1][self.col].getColorPieza() != source.getColorPieza() or self.matriz[self.fila+1][self.col].getColorPieza() == "vacio":
                self.matriz[self.fila+1][self.col].setBackGroundCyan()
            if self.matriz[self.fila][self.col-1].getColorPieza() != source.getColorPieza() or self.matriz[self.fila][self.col-1].getColorPieza() == "vacio":
                self.matriz[self.fila][self.col-1].setBackGroundCyan()
            if self.matriz[self.fila+1][self.col-1].getColorPieza() != source.getColorPieza() or self.matriz[self.fila+1][self.col-1].getColorPieza() == "vacio":
                self.matriz[self.fila+1][self.col-1].setBackGroundCyan()
        
        if self.fila ==7 and self.col ==7:
            if self.matriz[self.fila-1][self.col].getColorPieza() != source.getColorPieza() or self.matriz[self.fila-1][self.col].getColorPieza() == "vacio":
                self.matriz[self.fila-1][self.col].setBackGroundCyan()
            if self.matriz[self.fila][self.col-1].getColorPieza() != source.getColorPieza() or self.matriz[self.fila][self.col-1].getColorPieza() == "vacio":
                self.matriz[self.fila][self.col-1].setBackGroundCyan()
            if self.matriz[self.fila-1][self.col-1].getColorPieza() != source.getColorPieza() or self.matriz[self.fila-1][self.col-1].getColorPieza() == "vacio":
                self.matriz[self.fila-1][self.col-1].setBackGroundCyan()
        
        if self.fila >0 and self.fila <7 and self.col ==0:
            if self.matriz[self.fila+1][self.col].getColorPieza() != source.getColorPieza() or self.matriz[self.fila+1][self.col].getColorPieza() == "vacio":
                self.matriz[self.fila+1][self.col].setBackGroundCyan()
            if self.matriz[self.fila-1][self.col].getColorPieza() != source.getColorPieza() or self.matriz[self.fila-1][self.col].getColorPieza() == "vacio":
                self.matriz[self.fila-1][self.col].setBackGroundCyan()
            if self.matriz[self.fila][self.col+1].getColorPieza() != source.getColorPieza() or self.matriz[self.fila][self.col+1].getColorPieza() == "vacio":
                self.matriz[self.fila][self.col+1].setBackGroundCyan()
            if self.matriz[self.fila-1][self.col+1].getColorPieza() != source.getColorPieza() or self.matriz[self.fila-1][self.col+1].getColorPieza() == "vacio":
                self.matriz[self.fila-1][self.col+1].setBackGroundCyan()
            if self.matriz[self.fila+1][self.col+1].getColorPieza() != source.getColorPieza() or self.matriz[self.fila+1][self.col+1].getColorPieza() == "vacio":
                self.matriz[self.fila+1][self.col+1].setBackGroundCyan()
        
        if self.fila >0 and self.fila <7 and self.col ==7:
            if self.matriz[self.fila+1][self.col].getColorPieza() != source.getColorPieza() or self.matriz[self.fila+1][self.col].getColorPieza() == "vacio":
                self.matriz[self.fila+1][self.col].setBackGroundCyan()
            if self.matriz[self.fila-1][self.col].getColorPieza() != source.getColorPieza() or self.matriz[self.fila-1][self.col].getColorPieza() == "vacio":
                self.matriz[self.fila-1][self.col].setBackGroundCyan()
            if self.matriz[self.fila][self.col-1].getColorPieza() != source.getColorPieza() or self.matriz[self.fila][self.col-1].getColorPieza() == "vacio":
                self.matriz[self.fila][self.col-1].setBackGroundCyan()
            if self.matriz[self.fila-1][self.col-1].getColorPieza() != source.getColorPieza() or self.matriz[self.fila-1][self.col-1].getColorPieza() == "vacio":
                self.matriz[self.fila-1][self.col-1].setBackGroundCyan()
            if self.matriz[self.fila+1][self.col-1].getColorPieza() != source.getColorPieza() or self.matriz[self.fila+1][self.col-1].getColorPieza() == "vacio":
                self.matriz[self.fila+1][self.col-1].setBackGroundCyan()
        
def validaCaballo(self,source):
        if self.fila >1 and self.fila <6 and self.col >1 and self.col <6:
            if self.matriz[self.fila-2][self.col-1].getColorPieza() == "vacio" or self.matriz[self.fila-2][self.col-1].getColorPieza() != source.getColorPieza():
                self.matriz[self.fila-2][self.col-1].setBackGroundCyan()
            if self.matriz[self.fila-2][self.col+1].getColorPieza() == "vacio" or self.matriz[self.fila-2][self.col+1].getColorPieza() != source.getColorPieza():
                self.matriz[self.fila-2][self.col+1].setBackGroundCyan()
            if self.matriz[self.fila-1][self.col-2].getColorPieza() == "vacio" or self.matriz[self.fila-1][self.col-2].getColorPieza() != source.getColorPieza():
                self.matriz[self.fila-1][self.col-2].setBackGroundCyan()
            if self.matriz[self.fila-1][self.col+2].getColorPieza() == "vacio" or self.matriz[self.fila-1][self.col+2].getColorPieza() != source.getColorPieza():
                self.matriz[self.fila-1][self.col+2].setBackGroundCyan()
            if self.matriz[self.fila+2][self.col-1].getColorPieza() == "vacio" or self.matriz[self.fila+2][self.col-1].getColorPieza() != source.getColorPieza():
                self.matriz[self.fila+2][self.col-1].setBackGroundCyan()
            if self.matriz[self.fila+2][self.col+1].getColorPieza() == "vacio" or self.matriz[self.fila+2][self.col+1].getColorPieza() != source.getColorPieza():
                self.matriz[self.fila+2][self.col+1].setBackGroundCyan()
            if self.matriz[self.fila+1][self.col-2].getColorPieza() == "vacio" or self.matriz[self.fila+1][self.col-2].getColorPieza() != source.getColorPieza():
                self.matriz[self.fila+1][self.col-2].setBackGroundCyan()
            if self.matriz[self.fila+1][self.col+2].getColorPieza() == "vacio" or self.matriz[self.fila+1][self.col+2].getColorPieza() != source.getColorPieza():
                self.matriz[self.fila+1][self.col+2].setBackGroundCyan()
        
        if self.fila ==0 and self.col >1 and self.col <6:
            if self.matriz[self.fila+2][self.col-1].getColorPieza() == "vacio" or self.matriz[self.fila+2][self.col-1].getColorPieza() != source.getColorPieza():
                self.matriz[self.fila+2][self.col-1].setBackGroundCyan()
            if self.matriz[self.fila+2][self.col+1].getColorPieza() == "vacio" or self.matriz[self.fila+2][self.col+1].getColorPieza() != source.getColorPieza():
                self.matriz[self.fila+2][self.col+1].setBackGroundCyan()
            if self.matriz[self.fila+1][self.col-2].getColorPieza() == "vacio" or self.matriz[self.fila+1][self.col-2].getColorPieza() != source.getColorPieza():
                self.matriz[self.fila+1][self.col-2].setBackGroundCyan()
            if self.matriz[self.fila+1][self.col+2].getColorPieza() == "vacio" or self.matriz[self.fila+1][self.col+2].getColorPieza() != source.getColorPieza():
                self.matriz[self.fila+1][self.col+2].setBackGroundCyan()
        
        if self.fila ==1 and self.col >1 and self.col <6:
            if self.matriz[self.fila-1][self.col-2].getColorPieza() == "vacio" or self.matriz[self.fila-1][self.col-2].getColorPieza() != source.getColorPieza():
                self.matriz[self.fila-1][self.col-2].setBackGroundCyan()
            if self.matriz[self.fila-1][self.col+2].getColorPieza() == "vacio" or self.matriz[self.fila-1][self.col+2].getColorPieza() != source.getColorPieza():
                self.matriz[self.fila-1][self.col+2].setBackGroundCyan()
            if self.matriz[self.fila+2][self.col-1].getColorPieza() == "vacio" or self.matriz[self.fila+2][self.col-1].getColorPieza() != source.getColorPieza():
                self.matriz[self.fila+2][self.col-1].setBackGroundCyan()
            if self.matriz[self.fila+2][self.col+1].getColorPieza() == "vacio" or self.matriz[self.fila+2][self.col+1].getColorPieza() != source.getColorPieza():
                self.matriz[self.fila+2][self.col+1].setBackGroundCyan()
            if self.matriz[self.fila+1][self.col-2].getColorPieza() == "vacio" or self.matriz[self.fila+1][self.col-2].getColorPieza() != source.getColorPieza():
                self.matriz[self.fila+1][self.col-2].setBackGroundCyan()
            if self.matriz[self.fila+1][self.col+2].getColorPieza() == "vacio" or self.matriz[self.fila+1][self.col+2].getColorPieza() != source.getColorPieza():
                self.matriz[self.fila+1][self.col+2].setBackGroundCyan()
        
        if self.fila ==7 and self.col >1 and self.col <6:
            if self.matriz[self.fila-2][self.col-1].getColorPieza() == "vacio" or self.matriz[self.fila-2][self.col-1].getColorPieza() != source.getColorPieza():
                self.matriz[self.fila-2][self.col-1].setBackGroundCyan()
            if self.matriz[self.fila-2][self.col+1].getColorPieza() == "vacio" or self.matriz[self.fila-2][self.col+1].getColorPieza() != source.getColorPieza():
                self.matriz[self.fila-2][self.col+1].setBackGroundCyan()
            if self.matriz[self.fila-1][self.col-2].getColorPieza() == "vacio" or self.matriz[self.fila-1][self.col-2].getColorPieza() != source.getColorPieza():
                self.matriz[self.fila-1][self.col-2].setBackGroundCyan()
            if self.matriz[self.fila-1][self.col+2].getColorPieza() == "vacio" or self.matriz[self.fila-1][self.col+2].getColorPieza() != source.getColorPieza():
                self.matriz[self.fila-1][self.col+2].setBackGroundCyan()
        
        if self.fila ==6 and self.col >1 and self.col <6:
            if self.matriz[self.fila-2][self.col-1].getColorPieza() == "vacio" or self.matriz[self.fila-2][self.col-1].getColorPieza() != source.getColorPieza():
                self.matriz[self.fila-2][self.col-1].setBackGroundCyan()
            if self.matriz[self.fila-2][self.col+1].getColorPieza() == "vacio" or self.matriz[self.fila-2][self.col+1].getColorPieza() != source.getColorPieza():
                self.matriz[self.fila-2][self.col+1].setBackGroundCyan()
            if self.matriz[self.fila-1][self.col-2].getColorPieza() == "vacio" or self.matriz[self.fila-1][self.col-2].getColorPieza() != source.getColorPieza():
                self.matriz[self.fila-1][self.col-2].setBackGroundCyan()
            if self.matriz[self.fila-1][self.col+2].getColorPieza() == "vacio" or self.matriz[self.fila-1][self.col+2].getColorPieza() != source.getColorPieza():
                self.matriz[self.fila-1][self.col+2].setBackGroundCyan()
            if self.matriz[self.fila+1][self.col-2].getColorPieza() == "vacio" or self.matriz[self.fila+1][self.col-2].getColorPieza() != source.getColorPieza():
                self.matriz[self.fila+1][self.col-2].setBackGroundCyan()
            if self.matriz[self.fila+1][self.col+2].getColorPieza() == "vacio" or self.matriz[self.fila+1][self.col+2].getColorPieza() != source.getColorPieza():
                self.matriz[self.fila+1][self.col+2].setBackGroundCyan()
        
        if self.fila >1 and self.fila <6 and self.col ==0:
            if self.matriz[self.fila-2][self.col+1].getColorPieza() == "vacio" or self.matriz[self.fila-2][self.col+1].getColorPieza() != source.getColorPieza():
                self.matriz[self.fila-2][self.col+1].setBackGroundCyan()
            if self.matriz[self.fila-1][self.col+2].getColorPieza() == "vacio" or self.matriz[self.fila-1][self.col+2].getColorPieza() != source.getColorPieza():
                self.matriz[self.fila-1][self.col+2].setBackGroundCyan()
            if self.matriz[self.fila+2][self.col+1].getColorPieza() == "vacio" or self.matriz[self.fila+2][self.col+1].getColorPieza() != source.getColorPieza():
                self.matriz[self.fila+2][self.col+1].setBackGroundCyan()
            if self.matriz[self.fila+1][self.col+2].getColorPieza() == "vacio" or self.matriz[self.fila+1][self.col+2].getColorPieza() != source.getColorPieza():
                self.matriz[self.fila+1][self.col+2].setBackGroundCyan()
        
        if self.fila >1 and self.fila <6 and self.col ==1:
            if self.matriz[self.fila-2][self.col+1].getColorPieza() == "vacio" or self.matriz[self.fila-2][self.col+1].getColorPieza() != source.getColorPieza():
                self.matriz[self.fila-2][self.col+1].setBackGroundCyan()
            if self.matriz[self.fila-1][self.col+2].getColorPieza() == "vacio" or self.matriz[self.fila-1][self.col+2].getColorPieza() != source.getColorPieza():
                self.matriz[self.fila-1][self.col+2].setBackGroundCyan()
            if self.matriz[self.fila+2][self.col+1].getColorPieza() == "vacio" or self.matriz[self.fila+2][self.col+1].getColorPieza() != source.getColorPieza():
                self.matriz[self.fila+2][self.col+1].setBackGroundCyan()
            if self.matriz[self.fila+1][self.col+2].getColorPieza() == "vacio" or self.matriz[self.fila+1][self.col+2].getColorPieza() != source.getColorPieza():
                self.matriz[self.fila+1][self.col+2].setBackGroundCyan()
            if self.matriz[self.fila-2][self.col-1].getColorPieza() == "vacio" or self.matriz[self.fila-2][self.col-1].getColorPieza() != source.getColorPieza():
                self.matriz[self.fila-2][self.col-1].setBackGroundCyan()
            if self.matriz[self.fila+2][self.col-1].getColorPieza() == "vacio" or self.matriz[self.fila+2][self.col-1].getColorPieza() != source.getColorPieza():
                self.matriz[self.fila+2][self.col-1].setBackGroundCyan()
        
        if self.fila >1 and self.fila <6 and self.col ==7:
            if self.matriz[self.fila-2][self.col-1].getColorPieza() == "vacio" or self.matriz[self.fila-2][self.col-1].getColorPieza() != source.getColorPieza():
                self.matriz[self.fila-2][self.col-1].setBackGroundCyan()
            if self.matriz[self.fila-1][self.col-2].getColorPieza() == "vacio" or self.matriz[self.fila-1][self.col-2].getColorPieza() != source.getColorPieza():
                self.matriz[self.fila-1][self.col-2].setBackGroundCyan()
            if self.matriz[self.fila+2][self.col-1].getColorPieza() == "vacio" or self.matriz[self.fila+2][self.col-1].getColorPieza() != source.getColorPieza():
                self.matriz[self.fila+2][self.col-1].setBackGroundCyan()
            if self.matriz[self.fila+1][self.col-2].getColorPieza() == "vacio" or self.matriz[self.fila+1][self.col-2].getColorPieza() != source.getColorPieza():
                self.matriz[self.fila+1][self.col-2].setBackGroundCyan()    
        
        if self.fila >1 and self.fila <6 and self.col ==6:
            if self.matriz[self.fila-2][self.col-1].getColorPieza() == "vacio" or self.matriz[self.fila-2][self.col-1].getColorPieza() != source.getColorPieza():
                self.matriz[self.fila-2][self.col-1].setBackGroundCyan()
            if self.matriz[self.fila-1][self.col-2].getColorPieza() == "vacio" or self.matriz[self.fila-1][self.col-2].getColorPieza() != source.getColorPieza():
                self.matriz[self.fila-1][self.col-2].setBackGroundCyan()
            if self.matriz[self.fila+2][self.col-1].getColorPieza() == "vacio" or self.matriz[self.fila+2][self.col-1].getColorPieza() != source.getColorPieza():
                self.matriz[self.fila+2][self.col-1].setBackGroundCyan()
            if self.matriz[self.fila+1][self.col-2].getColorPieza() == "vacio" or self.matriz[self.fila+1][self.col-2].getColorPieza() != source.getColorPieza():
                self.matriz[self.fila+1][self.col-2].setBackGroundCyan()    
            if self.matriz[self.fila-2][self.col+1].getColorPieza() == "vacio" or self.matriz[self.fila-2][self.col+1].getColorPieza() != source.getColorPieza():
                self.matriz[self.fila-2][self.col+1].setBackGroundCyan()
            if self.matriz[self.fila+2][self.col+1].getColorPieza() == "vacio" or self.matriz[self.fila+2][self.col+1].getColorPieza() != source.getColorPieza():
                self.matriz[self.fila+2][self.col+1].setBackGroundCyan()
        
        if self.fila ==0 and self.col ==0:
            if self.matriz[self.fila+2][self.col+1].getColorPieza() == "vacio" or self.matriz[self.fila+2][self.col+1].getColorPieza() != source.getColorPieza():
                self.matriz[self.fila+2][self.col+1].setBackGroundCyan()
            if self.matriz[self.fila+1][self.col+2].getColorPieza() == "vacio" or self.matriz[self.fila+1][self.col+2].getColorPieza() != source.getColorPieza():
                self.matriz[self.fila+1][self.col+2].setBackGroundCyan()
        
        if self.fila ==1 and self.col ==0:
            if self.matriz[self.fila+2][self.col+1].getColorPieza() == "vacio" or self.matriz[self.fila+2][self.col+1].getColorPieza() != source.getColorPieza():
                self.matriz[self.fila+2][self.col+1].setBackGroundCyan()
            if self.matriz[self.fila+1][self.col+2].getColorPieza() == "vacio" or self.matriz[self.fila+1][self.col+2].getColorPieza() != source.getColorPieza():
                self.matriz[self.fila+1][self.col+2].setBackGroundCyan()
            if self.matriz[self.fila-1][self.col+2].getColorPieza() == "vacio" or self.matriz[self.fila-1][self.col+2].getColorPieza() != source.getColorPieza():
                self.matriz[self.fila-1][self.col+2].setBackGroundCyan()
        
        if self.fila ==0 and self.col ==1:
            if self.matriz[self.fila+2][self.col+1].getColorPieza() == "vacio" or self.matriz[self.fila+2][self.col+1].getColorPieza() != source.getColorPieza():
                self.matriz[self.fila+2][self.col+1].setBackGroundCyan()
            if self.matriz[self.fila+1][self.col+2].getColorPieza() == "vacio" or self.matriz[self.fila+1][self.col+2].getColorPieza() != source.getColorPieza():
                self.matriz[self.fila+1][self.col+2].setBackGroundCyan()
            if self.matriz[self.fila+2][self.col-1].getColorPieza() == "vacio" or self.matriz[self.fila+2][self.col-1].getColorPieza() != source.getColorPieza():
                self.matriz[self.fila+2][self.col-1].setBackGroundCyan()
        
        if self.fila ==1 and self.col ==1:
            if self.matriz[self.fila+2][self.col+1].getColorPieza() == "vacio" or self.matriz[self.fila+2][self.col+1].getColorPieza() != source.getColorPieza():
                self.matriz[self.fila+2][self.col+1].setBackGroundCyan()
            if self.matriz[self.fila+1][self.col+2].getColorPieza() == "vacio" or self.matriz[self.fila+1][self.col+2].getColorPieza() != source.getColorPieza():
                self.matriz[self.fila+1][self.col+2].setBackGroundCyan()
            if self.matriz[self.fila-1][self.col+2].getColorPieza() == "vacio" or self.matriz[self.fila-1][self.col+2].getColorPieza() != source.getColorPieza():
                self.matriz[self.fila-1][self.col+2].setBackGroundCyan()
            if self.matriz[self.fila+2][self.col-1].getColorPieza() == "vacio" or self.matriz[self.fila+2][self.col-1].getColorPieza() != source.getColorPieza():
                self.matriz[self.fila+2][self.col-1].setBackGroundCyan()
            
        
        if self.fila ==0 and self.col ==7:
            if self.matriz[self.fila+2][self.col-1].getColorPieza() == "vacio" or self.matriz[self.fila+2][self.col-1].getColorPieza() != source.getColorPieza():
                self.matriz[self.fila+2][self.col-1].setBackGroundCyan()
            if self.matriz[self.fila+1][self.col-2].getColorPieza() == "vacio" or self.matriz[self.fila+1][self.col-2].getColorPieza() != source.getColorPieza():
                self.matriz[self.fila+1][self.col-2].setBackGroundCyan()    
        
        if self.fila ==1 and self.col ==7:
            if self.matriz[self.fila+2][self.col-1].getColorPieza() == "vacio" or self.matriz[self.fila+2][self.col-1].getColorPieza() != source.getColorPieza():
                self.matriz[self.fila+2][self.col-1].setBackGroundCyan()
            if self.matriz[self.fila+1][self.col-2].getColorPieza() == "vacio" or self.matriz[self.fila+1][self.col-2].getColorPieza() != source.getColorPieza():
                self.matriz[self.fila+1][self.col-2].setBackGroundCyan()    
            if self.matriz[self.fila-1][self.col-2].getColorPieza() == "vacio" or self.matriz[self.fila-1][self.col-2].getColorPieza() != source.getColorPieza():
                self.matriz[self.fila-1][self.col-2].setBackGroundCyan()
        
        if self.fila ==0 and self.col ==6:
            if self.matriz[self.fila+2][self.col-1].getColorPieza() == "vacio" or self.matriz[self.fila+2][self.col-1].getColorPieza() != source.getColorPieza():
                self.matriz[self.fila+2][self.col-1].setBackGroundCyan()
            if self.matriz[self.fila+1][self.col-2].getColorPieza() == "vacio" or self.matriz[self.fila+1][self.col-2].getColorPieza() != source.getColorPieza():
                self.matriz[self.fila+1][self.col-2].setBackGroundCyan()    
            if self.matriz[self.fila+2][self.col+1].getColorPieza() == "vacio" or self.matriz[self.fila+2][self.col+1].getColorPieza() != source.getColorPieza():
                self.matriz[self.fila+2][self.col+1].setBackGroundCyan()    
        
        if self.fila ==1 and self.col ==6:
            if self.matriz[self.fila+2][self.col-1].getColorPieza() == "vacio" or self.matriz[self.fila+2][self.col-1].getColorPieza() != source.getColorPieza():
                self.matriz[self.fila+2][self.col-1].setBackGroundCyan()
            if self.matriz[self.fila+1][self.col-2].getColorPieza() == "vacio" or self.matriz[self.fila+1][self.col-2].getColorPieza() != source.getColorPieza():
                self.matriz[self.fila+1][self.col-2].setBackGroundCyan()    
            if self.matriz[self.fila+2][self.col+1].getColorPieza() == "vacio" or self.matriz[self.fila+2][self.col+1].getColorPieza() != source.getColorPieza():
                self.matriz[self.fila+2][self.col+1].setBackGroundCyan()    
            if self.matriz[self.fila-1][self.col-2].getColorPieza() == "vacio" or self.matriz[self.fila-1][self.col-2].getColorPieza() != source.getColorPieza():
                self.matriz[self.fila-1][self.col-2].setBackGroundCyan()
            
        
        if self.fila ==7 and self.col ==0:
            if self.matriz[self.fila-1][self.col+2].getColorPieza() == "vacio" or self.matriz[self.fila-1][self.col+2].getColorPieza() != source.getColorPieza():
                self.matriz[self.fila-1][self.col+2].setBackGroundCyan()
            if self.matriz[self.fila-2][self.col+1].getColorPieza() == "vacio" or self.matriz[self.fila-2][self.col+1].getColorPieza() != source.getColorPieza():
                self.matriz[self.fila-2][self.col+1].setBackGroundCyan()
        
        if self.fila ==6 and self.col ==0:
            if self.matriz[self.fila-1][self.col+2].getColorPieza() == "vacio" or self.matriz[self.fila-1][self.col+2].getColorPieza() != source.getColorPieza():
                self.matriz[self.fila-1][self.col+2].setBackGroundCyan()
            if self.matriz[self.fila-2][self.col+1].getColorPieza() == "vacio" or self.matriz[self.fila-2][self.col+1].getColorPieza() != source.getColorPieza():
                self.matriz[self.fila-2][self.col+1].setBackGroundCyan()
            if self.matriz[self.fila-1][self.col+2].getColorPieza() == "vacio" or self.matriz[self.fila-1][self.col+2].getColorPieza() != source.getColorPieza():
                self.matriz[self.fila-1][self.col+2].setBackGroundCyan()
        
        if self.fila ==7 and self.col ==1:
            if self.matriz[self.fila-1][self.col+2].getColorPieza() == "vacio" or self.matriz[self.fila-1][self.col+2].getColorPieza() != source.getColorPieza():
                self.matriz[self.fila-1][self.col+2].setBackGroundCyan()
            if self.matriz[self.fila-2][self.col+1].getColorPieza() == "vacio" or self.matriz[self.fila-2][self.col+1].getColorPieza() != source.getColorPieza():
                self.matriz[self.fila-2][self.col+1].setBackGroundCyan()
            if self.matriz[self.fila-2][self.col-1].getColorPieza() == "vacio" or self.matriz[self.fila-2][self.col-1].getColorPieza() != source.getColorPieza():
                self.matriz[self.fila-2][self.col-1].setBackGroundCyan()
        
        if self.fila ==6 and self.col ==1:
            if self.matriz[self.fila-1][self.col+2].getColorPieza() == "vacio" or self.matriz[self.fila-1][self.col+2].getColorPieza() != source.getColorPieza():
                self.matriz[self.fila-1][self.col+2].setBackGroundCyan()
            if self.matriz[self.fila-2][self.col+1].getColorPieza() == "vacio" or self.matriz[self.fila-2][self.col+1].getColorPieza() != source.getColorPieza():
                self.matriz[self.fila-2][self.col+1].setBackGroundCyan()
            if self.matriz[self.fila-2][self.col-1].getColorPieza() == "vacio" or self.matriz[self.fila-2][self.col-1].getColorPieza() != source.getColorPieza():
                self.matriz[self.fila-2][self.col-1].setBackGroundCyan()
            if self.matriz[self.fila+1][self.col+2].getColorPieza() == "vacio" or self.matriz[self.fila+1][self.col+2].getColorPieza() != source.getColorPieza():
                self.matriz[self.fila+1][self.col+2].setBackGroundCyan()
        
        if self.fila ==7 and self.col ==7:
            if self.matriz[self.fila-2][self.col-1].getColorPieza() == "vacio" or self.matriz[self.fila-2][self.col-1].getColorPieza() != source.getColorPieza():
                self.matriz[self.fila-2][self.col-1].setBackGroundCyan()
            if self.matriz[self.fila-1][self.col-2].getColorPieza() == "vacio" or self.matriz[self.fila-1][self.col-2].getColorPieza() != source.getColorPieza():
                self.matriz[self.fila-1][self.col-2].setBackGroundCyan()
        
        if self.fila ==6 and self.col ==7:
            if self.matriz[self.fila-2][self.col-1].getColorPieza() == "vacio" or self.matriz[self.fila-2][self.col-1].getColorPieza() != source.getColorPieza():
                self.matriz[self.fila-2][self.col-1].setBackGroundCyan()
            if self.matriz[self.fila-1][self.col-2].getColorPieza() == "vacio" or self.matriz[self.fila-1][self.col-2].getColorPieza() != source.getColorPieza():
                self.matriz[self.fila-1][self.col-2].setBackGroundCyan()
            if self.matriz[self.fila+1][self.col-2].getColorPieza() == "vacio" or self.matriz[self.fila+1][self.col-2].getColorPieza() != source.getColorPieza():
                self.matriz[self.fila+1][self.col-2].setBackGroundCyan()    
        
        if self.fila ==7 and self.col ==6:
            if self.matriz[self.fila-2][self.col-1].getColorPieza() == "vacio" or self.matriz[self.fila-2][self.col-1].getColorPieza() != source.getColorPieza():
                self.matriz[self.fila-2][self.col-1].setBackGroundCyan()
            if self.matriz[self.fila-1][self.col-2].getColorPieza() == "vacio" or self.matriz[self.fila-1][self.col-2].getColorPieza() != source.getColorPieza():
                self.matriz[self.fila-1][self.col-2].setBackGroundCyan()
            if self.matriz[self.fila-2][self.col+1].getColorPieza() == "vacio" or self.matriz[self.fila-2][self.col+1].getColorPieza() != source.getColorPieza():
                self.matriz[self.fila-2][self.col+1].setBackGroundCyan()
        
        if self.fila ==6 and self.col ==6:
            if self.matriz[self.fila-2][self.col-1].getColorPieza() == "vacio" or self.matriz[self.fila-2][self.col-1].getColorPieza() != source.getColorPieza():
                self.matriz[self.fila-2][self.col-1].setBackGroundCyan()
            if self.matriz[self.fila-1][self.col-2].getColorPieza() == "vacio" or self.matriz[self.fila-1][self.col-2].getColorPieza() != source.getColorPieza():
                self.matriz[self.fila-1][self.col-2].setBackGroundCyan()
            if self.matriz[self.fila-2][self.col+1].getColorPieza() == "vacio" or self.matriz[self.fila-2][self.col+1].getColorPieza() != source.getColorPieza():
                self.matriz[self.fila-2][self.col+1].setBackGroundCyan()
            if self.matriz[self.fila+1][self.col-2].getColorPieza() == "vacio" or self.matriz[self.fila+1][self.col-2].getColorPieza() != source.getColorPieza():
                self.matriz[self.fila+1][self.col-2].setBackGroundCyan()