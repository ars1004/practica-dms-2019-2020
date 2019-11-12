import requests
import os

class hubServerCon():

    def __init__(self):
        self.hub_ip = os.getenv('HUB_SERVER_HOST', '127.0.0.1')
        self.hub_puerto = os.getenv('HUB_SERVER_PORT', '1234')
        self.nombre = os.getenv('GAME_SERVER_NAME', 'Prueba')
        self.game_ip = os.getenv('GAME_SERVER_HOST', '127.0.0.1')
        self.game_puerto = os.getenv('GAME_SERVER_PORT', '9876')
        

    def darDeAlta(self):
        respuesta = requests.post('http://'+self.hub_ip+':'+self.hub_puerto+'/server/register', data = {'name': self.nombre, 'host': self.game_ip, 'port': self.game_puerto})
        if respuesta:
            return True
        else:
            return False

    def darDeBaja(self):
        respuesta = requests.post('http://'+self.hub_ip+':'+self.hub_puerto+'/server/unregister', data = {'name': self.nombre})
        if respuesta:
            return True
        else:
            return False