"""
Clase concreta del tablero de las damas
Crea el tablero
"""
from lib.interfacesJuego.datos.TableroInterfaz import Tablero

class TableroDamas(Tablero):
    
    def __init__(self,size):
       super().__init__(self,size)
       self.colocarPeonesIniciales()

    def colocarPeonesIniciales (self):
        self.grid = [[0, 'n', 0, 'n', 0, 'n', 0, 'n'],
           ['n', 0, 'n', 0, 'n', 0, 'n', 0],
           [0, 'n', 0, 'n', 0, 'n', 0, 'n'],
           [0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0],
           ['b', 0, 'b', 0, 'b', 0, 'b', 0],
           [0, 'b', 0, 'b', 0, 'b', 0, 'b'],
           ['b', 0, 'b', 0, 'b', 0, 'b', 0]]

    def colocar(self,fila,columna,pieza):
        self.grid[fila][columna] = pieza
    
    def quitarPieza(self,fila,columna):
        self.grid[fila][columna] = 0
    
    def devolverTablero(self):
        return self.grid
