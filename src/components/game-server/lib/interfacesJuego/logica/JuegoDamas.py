"""
Clase concreta Juego damas
Va a crear los jugadores y el creador
Contendrá el tamaño del juego correspondiente (8x8)
"""
from lib.interfacesJuego.logica.Juego import Juego

class JuegoDamas(Juego):
    
    def __init__(self):
        super().__init__(self,self.obtenerTamañoJuego,self.crearJugador)
    
    def obtenerTamañoJuego(self):
        return 8
     
    def crearJugador (self):
        super().crearJugador()

