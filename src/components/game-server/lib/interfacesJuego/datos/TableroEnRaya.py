"""
Tablero concreto del juego tres en raya
Crea el tablero e implementa los métodos
    colocar pieza
    quitar pieza
"""
import lib.interfacesJuego.datos.TableroInterfaz

class TableroEnRaya(TableroInterfaz.Tablero):
    
    
    def __init__(self,size):
        TableroInterfaz.Tablero.__init__(self,size)
        
    def colocar(self,fila,columna,pieza):
        self.grid[fila][columna] = pieza
    
    def quitarPieza(self,fila,columna):
        self.grid[fila][columna] = 0
    
    def devolverTablero(self):
        return self.grid
