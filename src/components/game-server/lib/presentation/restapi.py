from flask import Flask, escape, request, abort

from lib.util.auth_server_util import authServerCon
from lib.util.hub_server_util import hubServerCon
from lib.game.arbitroEnRaya import Arbitro
import lib.util.json_util as json_util
from lib.util.player_util import PlayerUtil

import sys

class RestApi():
    """ REST API facade.
    ---
    This class is a facade with the operations provided through the REST API.
    """
    def __init__(self):
        self.authCon = authServerCon()
        self.hubCon = hubServerCon()
        self.juego = Arbitro()
        self.player_util = PlayerUtil()
        # self.juego.check()

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
                - (200, n) cuando se une con exito. n es el numero del jugador.
                - (401, 'Unauthorized') cuando el token es erroneo
                - (500, 'Server error') cuando ocurre un error.
        """
        try:
            token = request.form['token']
            print(token)
            if self.authCon.verificar_usuario(token):
                nombre = ''
                if 'nombre' in request.form:
                    nombre = request.form['nombre']
                n = self.juego.crearJugador()
                self.player_util.add_player(token, n)
                return (200, str(n))
            else:
                return (401, 'Unauthorized')
        except Exception as e: 
            print(e, file=sys.stderr)
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
        except Exception as e: 
            print(e, file=sys.stderr)
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
        except Exception as e: 
            print(e, file=sys.stderr)
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
            estado_json = json_util.estado_a_json(estado)
            return (200, estado_json)
        except Exception as e: 
            print(e, file=sys.stderr)
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
                x, y = json_util.json_a_movimiento(movimiento)
                n = self.player_util.token_to_player(token)
                self.juego.movePiece(x, y, n)
                return (200, 'OK')
            else:
                return (401, 'Unauthorized')
        except Exception as e: 
            print(e, file=sys.stderr)
            print(n, file=sys.stderr)
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
        except Exception as e: 
            print(e, file=sys.stderr)
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
        except Exception as e: 
            print(e, file=sys.stderr)
            return (500, 'Error')