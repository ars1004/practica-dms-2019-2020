"""
Clase concreta del tablero de las damas
Crea el tablero
"""
from lib.interfacesJuego.datos.TableroInterfaz import Tablero

class TableroDamas(Tablero):
    
    def __init__(self,size):
       super().__init__(self,size)
    
    def colocar(self,fila,columna,pieza):
        self.grid[fila][columna] = pieza
    
    def quitarPieza(self,fila,columna):
        self.grid[fila][columna] = 0
    
    def devolverTablero(self):
        return self.grid
