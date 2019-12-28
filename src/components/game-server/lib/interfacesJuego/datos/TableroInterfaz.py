"""
Clase abstracta del Tablero
se encarga de crear el tablero modelo 
"""

class Tablero:
    
    def __init__(self,size):
        self.grid = []
        for fila in range(size):
            self.grid.append([])
            for columna in range(size):
                self.grid[fila].append(0)
    
    def colocar(self,fila,columna,pieza):
        pass
    
    def quitarPieza(self,fila,columna):
        pass
    
    
