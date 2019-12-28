"""
Clase concreta Juego damas
Va a crear los jugadores y el creador
Contendrá el tamaño del juego correspondiente (8x8)
"""
from lib.interfacesJuego.logica.Juego import Juego
from lib.interfacesJuego.logica.CreadorDamas import CreadorDamas

class JuegoDamas(Juego):
    
    def __init__(self, jugadores):
        super().__init__(jugadores)
        self.creador = CreadorDamas(self.obtenerTamañoJuego(), jugadores)
    
    def obtenerTamañoJuego(self):
        return 8

