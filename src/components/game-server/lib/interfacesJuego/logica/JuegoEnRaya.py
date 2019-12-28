"""
Clase concreta Juego Tres en Raya
Será el punto donde se inicie el juego
"""
from lib.interfacesJuego.logica.Juego import Juego

class JuegoEnRaya(Juego):
    def __init__(self):
        super().__init__(self,self.obtenerTamañoJuego,self.crearJugador)
    
    def obtenerTamañoJuego(self):
        return 3
     
    def crearJugador (self):
        super().crearJugador()

