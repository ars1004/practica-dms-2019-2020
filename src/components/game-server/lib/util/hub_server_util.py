import requests
import os

class hubServerCon():

    def __init__(self):
        self.hub_ip = os.getenv('HUB_SERVER_HOST', '127.0.0.1')
        self.hub_puerto = os.getenv('HUB_SERVER_PORT', '1234')
        self.nombre = os.getenv('GAME_SERVER_NAME', 'Prueba')
        self.game_ip = os.getenv('GAME_SERVER_HOST', '127.0.0.1')
        self.game_puerto = os.getenv('GAME_SERVER_PORT', '9876')
        # self.darDeAlta()
        

    def darDeAlta(self, nombre = None):
        """ Da de alta un servidor en el hub

        Parameters:
            - nombre: (opcional) Nombre del servidor. Si no se pasa ningun nombre,
                se utiliza el nombre obtenido de las variables de entorno.
        Returns:
            - True cuando el servidor se da de alta correctamente
            - False cuando no se puede dar de alta el servidor
        """

        if not nombre:
            nombre = self.nombre

        data = {'name': nombre, 'host': self.game_ip, 'port': self.game_puerto}
        respuesta = requests.post('http://'+self.hub_ip+':'+self.hub_puerto+'/server/register', data = data)
        
        if respuesta:
            return True
        else:
            return False

    def darDeBaja(self, nombre = None):
        """ Da de baja un servidor en el hub

        Parameters:
            - nombre: (opcional) Nombre del servidor. Si no se pasa ningun nombre,
                se utiliza el nombre obtenido de las variables de entorno.
        Returns:
            - True cuando el servidor se da de baja correctamente
            - False cuando no se puede dar de baja el servidor
        """

        if not nombre:
            nombre = self.nombre

        data = {'name': nombre}
        respuesta = requests.post('http://'+self.hub_ip+':'+self.hub_puerto+'/server/unregister', data = data)

        if respuesta:
            return True
        else:
            return False