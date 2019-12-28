"""
Clase concreta del tablero de las damas
Crea el tablero
"""
import lib.interfacesJuego.datos.TableroInterfaz

class TableroDamas(TableroInterfaz.Tablero):
    
    def __init__(self,size):
       TableroInterfaz.Tablero.__init__(self,size)
    
    def colocar(self,fila,columna,pieza):
        self.grid[fila][columna] = pieza
    
    def quitarPieza(self,fila,columna):
        self.grid[fila][columna] = 0
    
    def devolverTablero(self):
        return self.grid
