"""
Interfaz Arbitro
"""

class Arbitro(object):
    
    num = 0
    jugadores = []
    turno = 1
    def __init__(self,tablero,jugadores):
        self.grid = tablero
        self.jugadores = jugadores
        
    def moverPieza(self,fila,columna,jugador):
        pass
    
    def obtenerJugadorConTurno(self):
        self.turno = 3 - self.turno
        return self.turno
    
    def movimientoLegal(self,row,column):
        pass
    
    def estaAcabado(self):
        pass