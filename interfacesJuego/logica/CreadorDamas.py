"""
Creador del juego Damas
Se encarga de llevar el tablero y crear el arbitro
"""
import Creador
import ArbitroDamas
from datos import TableroDamas

class CreadorDamas(Creador.Creador):
    
    def __init__(self,tamaño,jugadores):
        self.adjudicarTamaño(tamaño)
        self.tablero = self.crearTablero(self.tamaño)
        self.jugadores = jugadores
        self.arbitro = ArbitroDamas.ArbitroDamas(self.tablero,self.jugadores)
    
    def adjudicarTamaño(self,size):
        Creador.Creador.adjudicarTamaño(size)
        
    def crearTablero(self,tamaño):
        self.board = TableroDamas.TableroDamas(tamaño)
        grid = self.board.devolverTablero
        return grid
    
    def obtenerEstado(self):
        player = self.arbitro.jugadorTurno
        tablero = self.tablero
        acabado = self.arbitro.estaAcabado()
        return player, tablero, acabado
    

