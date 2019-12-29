import requests
import os


class AuthServerCon():

    def __init__(self):
        self.ip = os.getenv('AUTH_SERVER_HOST', '127.0.0.1')
        self.puerto = os.getenv('AUTH_SERVER_PORT', '1234')

    def verificar_usuario(self, token):
        """ Verifica si un usuario ha iniciado sesion.

        Parameters:
            - token: Token que un usuario obtiene al iniciar sesion.
        Returns:
            - True cuando el token ha sido verificado correctamente
            - False cuando no se puede verificar el token
        """
        respuesta = requests.get(
            'http://'+self.ip+':'+self.puerto+'/token/check', data={'token': token})
        if respuesta:
            return True
        else:
            return False
