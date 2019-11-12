import requests
import os

class authServerCon():

    def __init__(self):
        self.ip = os.getenv('AUTH_SERVER_HOST', '127.0.0.1')
        self.puerto = os.getenv('AUTH_SERVER_PORT', '1234')
        

    def verificar_usuario(self, token):
        respuesta = requests.get('http://'+self.ip+':'+self.puerto+'/token/check', data = {'token':token})
        if respuesta:
            return True
        else:
            return False
    