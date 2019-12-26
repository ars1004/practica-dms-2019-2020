"""
Clase concreta Juego Tres en Raya
Será el punto donde se inicie el juego
"""
import Juego

class JuegoEnRaya(Juego):
    def __init__(self):
        Juego.Juego.__init__(self,self.obtenerTamañoJuego,self.crearJugador)
    
    def obtenerTamañoJuego(self):
        return 3
     
    def crearJugador (self):
        Juego.Juego.crearJugador()

