from flask import Flask, escape, request, abort

from lib.util.auth_server_util import authServerCon
from lib.util.hub_server_util import hubServerCon
from lib.game.arbitroEnRaya import Arbitro
import json


import json

class RestApi():
    """ REST API facade.
    ---
    This class is a facade with the operations provided through the REST API.
    """
    def __init__(self):
        self.authCon = authServerCon()
        self.hubCon = hubServerCon()
        self.juego = Arbitro()

    def status(self, request):
        """ Status handler.
        ---
        Always returns a tuple with the 200 status code and an "OK" message.
        """
        return (200, 'OK')

    def unirse(self, request):
        """ Gestor de union de usuario.
        ---
        Une un usuario a la partida.

        Parameters:
            - request: The HTTP request received in the REST endpoint.
        Returns:
            A tuple with the following values:
                - (200, 'OK') cuando se une con exito.
                - (401, 'Unauthorized') cuando el token es erroneo
                - (500, 'Server error') cuando ocurre un error.
        """
        try:
            token = request.form['token']
            
            if self.authCon.verificar_usuario(token):
                nombre = ''
                if 'nombre' in request.form:
                    nombre = request.form['nombre']
                self.juego.crearJugador()
                return (200, 'OK')
            else:
                return (401, 'Unauthorized')
        except:
            return (500, 'Server error')

    def dar_de_alta(self, request):
        """ Da de alta el servidor en el hub.

        Parameters:
            - request: The HTTP request received in the REST endpoint.
        Returns:
            A tuple with the following values:
                - (200, 'OK') cuando se da de alta correctamente.
                - (401, 'Unauthorized') cuando no se puede verificar al usuario.
                - (500, 'Error) cuando falla el servidor.
        """
        try:
            token = request.form['token']

            if self.authCon.verificar_usuario(token):
                if self.hubCon.darDeAlta():
                    return (200, 'OK')
                else:
                    return (500, 'Error')
            else:
                return (401, 'Unauthorized')
        except:
            return (500, 'Error')

    def dar_de_baja(self, request):
        """ Da de baja el servidor en el hub.

        Parameters:
            - request: The HTTP request received in the REST endpoint.
        Returns:
            A tuple with the following values:
                - (200, 'OK') cuando se da de alta correctamente.
                - (401, 'Unauthorized') cuando no se puede verificar al usuario.
                - (500, 'Error) cuando falla el servidor.
        """

        try:
            token = request.form['token']

            if self.authCon.verificar_usuario(token):
                if self.hubCon.darDeBaja():
                    return (200, 'OK')
                else:
                    return (500, 'Error')
            else :
                return (401, 'Unauthorized')
        except:
            return (500, 'Error')

    def obtener_estado(self, request):
        """ Obtiene el estado de una partida.

        Parameters:
            - request: The HTTP request received in the REST endpoint.
        Returns:
            A tuple with the following values:
                - (200, estado) cuando se obtiene el estado correctamente.
                - (500, 'Error) cuando falla el servidor.
        """
        try:
            estado = self.juego.obtenerEstado()
            return (200, estado)
        except:
            return (500, 'Error')

    def hacer_movimiento(self, request):
        """ Hace un movimiento.

        Parameters:
            - request: The HTTP request received in the REST endpoint.
        Returns:
            A tuple with the following values:
                - (200, 'OK') cuando el movimiento se ha realizado correctamente.
                - (401, 'Unauthorized') cuando no se puede verificar al usuario.
                - (500, 'Error) cuando falla el servidor.
        """
        try:
            token = request.form['token']

            if self.authCon.verificar_usuario(token):
                movimiento = request.form['movimiento']
                mov = json.loads(movimiento)
                x,y = mov['x'], mov['y']
                self.juego.movePiece(y,x)
                return (200, 'OK')
            else:
                return (401, 'Unauthorized')
        except:
            return (500, 'Error')


    def obtener_juegos(self, request):
        """ Obtiene un listado de los juegos disponibles.

        Parameters:
            - request: The HTTP request received in the REST endpoint.
        Returns:
            A tuple with the following values:
                - (200, 'OK') cuando se obtienen correctamente los juegos.
                - (500, 'Error) cuando falla el servidor.
        """
        try:
            #TODO obtener los juegos disponibles

            return (200, 'OK')
        except:
            return (500, 'Error')

    def seleccionar_juego(self, request):
        """ Selecciona el juego del servidor.

        Parameters:
            - request: The HTTP request received in the REST endpoint.
        Returns:
            A tuple with the following values:
                - (200, 'OK') cuando el juego se ha seleccionado correctamente.
                - (401, 'Unauthorized') cuando no se puede verificar al usuario.
                - (500, 'Error) cuando falla el servidor.
        """

        try:
            token = request.form['token']

            if self.authCon.verificar_usuario(token):
                #TODO seleccionar juego

                return (200, 'OK')
            else:
                return (401, 'Unauthorized')
        except:
            return (500, 'Error')