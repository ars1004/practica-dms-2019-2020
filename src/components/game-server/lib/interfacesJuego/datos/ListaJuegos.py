from lib.interfacesJuego.logica.JuegoDamas import JuegoDamas
from lib.interfacesJuego.logica.JuegoEnRaya import JuegoEnRaya


class ListaJuegos:
    """ Contiene una lista de juegos que se pueden juegar.
    Cada juego esta en un diccionario donde la clave es el nombre y el
    valor es la clase del juego.
    Para añadir un juego a la lista se importa la clase que hereda de logica.Juego
    y se añade al diccionario con el nombre del juego.
    Ejemplo:
        'from logica.JuegoGo import JuegoGo'


        'self.dict_juegos = {
        ...
        "Go": JuegoGo,
        ...
        }'

    """

    def __init__(self):
        self.dict_juegos = {
            "Damas": JuegoDamas,
            "Tres en raya": JuegoEnRaya
        }

    def obtener_juegos(self):
        """ Obtiene la lista de juegos disponibles.
        """
        return list(self.dict_juegos.keys())

    def obtener_juego(self, juego):
        return self.dict_juegos[juego]