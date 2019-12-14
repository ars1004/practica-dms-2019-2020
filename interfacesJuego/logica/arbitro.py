"""
Interfaz Arbitro
"""

class Arbitro(object):
    
    num = 0
    grid = []
    jugadores = []
    turno = 0
    def __init__(self,tablero,jugadores):
        self.grid = tablero
        self.jugadores = jugadores
        
    def moverPieza(self,row,column):
        pass
    
    def obtenerJugadorConTurno(self):
        if self.turno % 2 == 0:
            self.turno = self.jugadores[0]
        else:
            self.turno = self.jugadores[1]
        return self.turno
    
    def esLegal(self,row,column):
        pass
    
    def estaAcabado(self):
        pass