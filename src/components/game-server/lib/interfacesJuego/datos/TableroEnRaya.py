"""
Tablero concreto del juego tres en raya
Crea el tablero e implementa los métodos
    colocar pieza
    quitar pieza
"""
from lib.interfacesJuego.datos.TableroInterfaz import Tablero

class TableroEnRaya(Tablero):
    
    
    def __init__(self,size):
        super().__init__(size)
        
    def colocar(self,fila,columna,pieza):
        self.grid[fila][columna] = pieza
    
    def quitarPieza(self,fila,columna):
        self.grid[fila][columna] = 0
    
    def devolverTablero(self):
        return self.grid
