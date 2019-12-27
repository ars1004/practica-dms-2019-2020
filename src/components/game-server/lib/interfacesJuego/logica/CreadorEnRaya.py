"""
Creador del juego Tres en Raya
Se encarga de llevar el tablero y crear el arbitro
"""
import Creador
from datos import TableroEnRaya
import ArbitroEnRaya

class CreadorEnRaya(Creador.Creador):
    
    def __init__(self,tamaño,jugadores):
        self.adjudicarTamaño(tamaño)
        self.tablero = self.crearTablero(self.tamaño)
        self.jugadores = jugadores
        self.arbitro = ArbitroEnRaya.ArbitroEnRaya(self.tablero,self.jugadores)
    
    def adjudicarTamaño(self,size):
        Creador.Creador.adjudicarTamaño(size)
        
    def crearTablero(self,tamaño):
        self.board = TableroEnRaya.TableroEnRaya(tamaño)
        grid = self.board.devolverTablero
        return grid
   
    def obtenerEstado(self):
        player = self.arbitro.jugadorTurno
        tablero = self.tablero
        acabado = self.arbitro.estaAcabado()
        return player, tablero, acabado
    

