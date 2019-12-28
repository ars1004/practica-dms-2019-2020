"""
Creador del juego Damas
Se encarga de llevar el tablero y crear el arbitro
"""
from lib.interfacesJuego.logica.Creador import Creador
from lib.interfacesJuego.logica.ArbitroDamas import ArbitroDamas
from lib.interfacesJuego.datos.TableroDamas import TableroDamas

class CreadorDamas(Creador):
    
    def __init__(self,tamaño,jugadores):
        self.adjudicarTamaño(tamaño)
        self.tablero = self.crearTablero(self.tamaño)
        self.jugadores = jugadores
        self.arbitro = ArbitroDamas(self.tablero,self.jugadores)
    
    def adjudicarTamaño(self,size):
        super().adjudicarTamaño(size)
        
    def crearTablero(self,tamaño):
        self.board = TableroDamas(tamaño)
        grid = self.board.devolverTablero()
        return grid
    
    def obtenerEstado(self):
        player = self.arbitro.jugadorTurno
        tablero = self.tablero
        acabado = self.arbitro.estaAcabado()
        return player, tablero, acabado
    

