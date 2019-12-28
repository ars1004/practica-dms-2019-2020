"""
Clase abstacta Juego
Va a crear los jugadores y el creador
Contendrá el tamaño del juego correspondiente
"""
from datos import Jugador
import Creador

class Juego(object):
    
    def __init__(self):
        self.num = 1
        self.creador = Creador.Creador(self.obtenerTamañoJuego,self.crearJugador)
    
    def obtenerTamañoJuego(self):
        pass
     
    def crearJugador (self):
        if self.num == 3:
            raise # si se intentan unir mas de dos personas
        jugador = Jugador.Jugador(self.num)
        return self.jugador

    def obtener_estado(self):
        return self.creador.obtenerEstado()