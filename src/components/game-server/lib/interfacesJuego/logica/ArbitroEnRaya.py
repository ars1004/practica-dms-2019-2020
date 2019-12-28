"""
Clase concreta arbitro del juego 3 en raya
"""
from lib.interfacesJuego.logica.arbitro import Arbitro

class ArbitroEnRaya(Arbitro):
    num = 0
    grid = []
    jugadores = []
    jugadorTurno = 0
    def __init__(self,tablero,jugadores):
        super().__init__(tablero,jugadores)
        
    def moverPieza(self,fila,columna,jugador):
        if self.jugadorTurno == jugador and self.movimientoLegal(fila,columna):
            self.grid.colocar(fila,columna,self.jugadorTurno)
            self.jugadorTurno = self.obtenerJugadorConTurno()
        else:
            raise
    
    def movimientoLegal(self,fila,columna):
        if fila >= 0 and fila < len(self.grid) and columna >= 0 and columna < len(self.grid):
            if self.grid[fila][columna] == 0:
                return True
        return False
    
    def obtenerJugadorConTurno(self):
        self.jugadorTurno = super().obtenerJugadorConTurno()
        return self.jugadorTurno
    
    def estaAcabado(self):
        noZero = 0
        for i in range(len(self.grid)):
            if self.enFila(i) == True:
                return True
            for j in range(len(self.grid)):
                if self.enColumna(j) == True:
                   return True
                if self.grid[i][j] != 0:
                    noZero += 1
        if self.enDiagonal() == True:
                    return True        
        if noZero ==  len(self.grid)*len(self.grid):
            return True
        else:
            return False
        
    def enFila(self,row):
        noZero = 0
        valor = 0
        for x in self.grid[row]:
            if x != 0:
                valor += x
                noZero += 1
        if (noZero == valor or noZero == valor/2) and noZero == len(self.grid):
            return True
        else:
            return False
    
    def enColumna(self,column):
        noZero = 0
        valor = 0
        for i in range(len(self.grid)):
            for j in range(len(self.grid)):
                if j == column:
                    if self.grid[i][j] != 0:
                        valor += self.grid[i][j]
                        noZero += 1
        if noZero == len(self.grid) and (noZero == valor or noZero == valor/2):
            return True
        else:
            return False
    
    def enDiagonal(self):
        noZero = 0
        diagonal = 0
        for i in range(len(self.grid)):
            for j in range(len(self.grid)):
                if i == j:
                    if self.grid[i][j] != 0:
                        diagonal += self.grid[i][j]
                        noZero += 1
        if noZero == len(self.grid) and (noZero == diagonal or noZero == diagonal/2):
            return True
        else:
            return False
    
        
    def check(self):
        return True
