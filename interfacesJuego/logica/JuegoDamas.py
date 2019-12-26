"""
Clase concreta Juego damas
Va a crear los jugadores y el creador
Contendrá el tamaño del juego correspondiente (8x8)
"""
import Juego

class JuegoDamas(Juego.Juego):
    
    def __init__(self):
        Juego.Juego.__init__(self,self.obtenerTamañoJuego,self.crearJugador)
    
    def obtenerTamañoJuego(self):
        return 8
     
    def crearJugador (self):
        Juego.Juego.crearJugador()

