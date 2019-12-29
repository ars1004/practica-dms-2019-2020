"""
Clase concreta arbitro del juego 3 en raya
"""
from lib.interfacesJuego.logica.arbitro import Arbitro
import sys

class ArbitroEnRaya(Arbitro):
    num = 0
    jugadores = []
    jugadorTurno = 1
    def __init__(self,tablero,jugadores):
        super().__init__(tablero,jugadores)
        self.grid = tablero
        self.tablero = self.grid.grid

    def moverPieza(self,fila,columna,jugador):
        if self.jugadorTurno == jugador and self.movimientoLegal(fila,columna):
            self.grid.colocar(fila,columna,self.jugadorTurno)
            self.jugadorTurno = self.obtenerJugadorConTurno()
        else:
            raise
    
    def movimientoLegal(self,fila,columna):
        if fila >= 0 and fila < len(self.tablero) and columna >= 0 and columna < len(self.tablero):
            if self.tablero[fila][columna] == 0:
                return True
        return False
    
    def obtenerJugadorConTurno(self):
        self.jugadorTurno = super().obtenerJugadorConTurno()
        return self.jugadorTurno
    
    def estaAcabado(self):
        noZero = 0
        for i in range(len(self.tablero)):
            if self.enFila(i) == True:
                return True
            for j in range(len(self.tablero)):
                if self.enColumna(j) == True:
                   return True
                if self.tablero[i][j] != 0:
                    noZero += 1
        if self.enDiagonal() == True:
                    return True        
        if noZero ==  len(self.tablero)*len(self.tablero):
            return True
        else:
            return False
        
    def enFila(self,row):
        noZero = 0
        valor = 0
        for x in self.tablero[row]:
            if x != 0:
                valor += x
                noZero += 1
        if (noZero == valor or noZero == valor/2) and noZero == len(self.tablero):
            return True
        else:
            return False
    
    def enColumna(self,column):
        noZero = 0
        valor = 0
        for i in range(len(self.tablero)):
            for j in range(len(self.tablero)):
                if j == column:
                    if self.tablero[i][j] != 0:
                        valor += self.tablero[i][j]
                        noZero += 1
        if noZero == len(self.tablero) and (noZero == valor or noZero == valor/2):
            return True
        else:
            return False
    
    def enDiagonal(self):
        noZero = 0
        diagonal = 0
        for i in range(len(self.tablero)):
            for j in range(len(self.tablero)):
                if i == j:
                    if self.tablero[i][j] != 0:
                        diagonal += self.tablero[i][j]
                        noZero += 1
        if noZero == len(self.tablero) and (noZero == diagonal or noZero == diagonal/2):
            return True
        else:
            return False
    
        
    def check(self):
        return True
