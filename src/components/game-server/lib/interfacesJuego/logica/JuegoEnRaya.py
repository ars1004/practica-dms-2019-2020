"""
Clase concreta Juego Tres en Raya
Será el punto donde se inicie el juego
"""
from lib.interfacesJuego.logica.Juego import Juego

class JuegoEnRaya(Juego):
    def __init__(self, jugadores):
        super().__init__(jugadores)
    
    def obtenerTamañoJuego(self):
        return 3

