from flask import Flask, escape, request, abort

from lib.util.auth_server_util import authServerCon
from lib.util.hub_server_util import hubServerCon
from lib.interfacesJuego.logica.GestorJuegos import GestorJuegos
import lib.util.json_util as json_util
from lib.util.player_util import PlayerUtil

import sys

class RestApi():
    """ Fachada de la API REST.
    ---
    Esta clase es una fachada con las operaciones proporcionadas por la API REST.
    """
    def __init__(self):
        self.authCon = authServerCon()
        self.hubCon = hubServerCon()
        self.gestor_juegos = GestorJuegos()
        self.player_util = PlayerUtil()
        # self.juego.check()

    def status(self, request):
        """ Comprobar estado.
        ---
        Siempre devuelve una tupla con el código de estado 200 y el mensaje "OK".
        """
        return (200, 'OK')

    def unirse(self, request):
        """ Gestor de unión de usuario.
        ---
        Une un usuario a la partida.

        parámetros:
            - request: La petición HTTP recibida en el endpoint.
        devuelve:
            Una tupla con los siguientes valores:
                - (200, n) cuando se une con exito. n es el numero del jugador.
                - (401, 'Acceso denegado') cuando el token es erroneo
                - (500, 'Error del servidor') cuando ocurre un error.
        """
        try:
            token = request.form['token']
            print(token)
            if self.authCon.verificar_usuario(token):
                nombre = ''
                if 'nombre' in request.form:
                    nombre = request.form['nombre']
                n = self.gestor_juegos.añadir_jugador(token)
                return (200, str(n))
            else:
                return (401, 'Acceso denegado')
        except Exception as e: 
            print(e, file=sys.stderr)
            return (500, 'Error del servidor')

    def dar_de_alta(self, request):
        """ Da de alta el servidor en el hub.

        parámetros:
            - request: La petición HTTP recibida en el endpoint.
        devuelve:
            Una tupla con los siguientes valores:
                - (200, 'OK') cuando se da de alta correctamente.
                - (401, 'Acceso denegado') cuando no se puede verificar al usuario.
                - (500, 'Error del servidor') cuando falla el servidor.
        """
        try:
            token = request.form['token']

            if self.authCon.verificar_usuario(token):
                if self.hubCon.darDeAlta():
                    return (200, 'OK')
                else:
                    return (500, 'Error del servidor')
            else:
                return (401, 'Acceso denegado')
        except Exception as e: 
            print(e, file=sys.stderr)
            return (500, 'Error del servidor')

    def dar_de_baja(self, request):
        """ Da de baja el servidor en el hub.

        parámetros:
            - request: La petición HTTP recibida en el endpoint.
        devuelve:
            Una tupla con los siguientes valores:
                - (200, 'OK') cuando se da de alta correctamente.
                - (401, 'Acceso denegado') cuando no se puede verificar al usuario.
                - (500, 'Error del servidor') cuando falla el servidor.
        """

        try:
            token = request.form['token']

            if self.authCon.verificar_usuario(token):
                if self.hubCon.darDeBaja():
                    return (200, 'OK')
                else:
                    return (500, 'Error del servidor')
            else :
                return (401, 'Acceso denegado')
        except Exception as e: 
            print(e, file=sys.stderr)
            return (500, 'Error del servidor')

    def obtener_estado(self, request):
        """ Obtiene el estado de una partida.

        parámetros:
            - request: La petición HTTP recibida en el endpoint.
        devuelve:
            Una tupla con los siguientes valores:
                - (200, estado) cuando se obtiene el estado correctamente.
                - (500, 'Error del servidor') cuando falla el servidor.
        """
        try:
            estado = self.gestor_juegos.obtener_estado()
            estado_json = json_util.estado_a_json(estado)
            return (200, estado_json)
        except Exception as e: 
            print(e, file=sys.stderr)
            return (500, 'Error del servidor')

    def hacer_movimiento(self, request):
        """ Hace un movimiento.

        parámetros:
            - request: La petición HTTP recibida en el endpoint.
        devuelve:
            Una tupla con los siguientes valores:
                - (200, 'OK') cuando el movimiento se ha realizado correctamente.
                - (401, 'Acceso denegado') cuando no se puede verificar al usuario.
                - (500, 'Error del servidor') cuando falla el servidor.
        """
        try:
            token = request.form['token']

            if self.authCon.verificar_usuario(token):
                movimiento_json = request.form['movimiento']
                movimiento = json_util.json_a_objeto(movimiento_json)
                self.gestor_juegos.hacer_movimiento(movimiento, token)
                return (200, 'OK')
            else:
                return (401, 'Acceso denegado')
        except Exception as e: 
            print(e, file=sys.stderr)
            print(n, file=sys.stderr)
            return (500, 'Error del servidor')

    def obtener_juegos(self, request):
        """ Obtiene un listado de los juegos disponibles.

        parámetros:
            - request: La petición HTTP recibida en el endpoint.
        devuelve:
            Una tupla con los siguientes valores:
                - (200, 'OK') cuando se obtienen correctamente los juegos.
                - (500, 'Error del servidor') cuando falla el servidor.
        """
        try:
            juegos = self.gestor_juegos.obtener_juegos()
            juegos_json = json_util.objeto_a_json(juegos)
            return (200, juegos_json)
        except Exception as e: 
            print(e, file=sys.stderr)
            return (500, 'Error del servidor')

    def seleccionar_juego(self, request):
        """ Selecciona el juego del servidor.

        parámetros:
            - request: La petición HTTP recibida en el endpoint.
        devuelve:
            Una tupla con los siguientes valores:
                - (200, 'OK') cuando el juego se ha seleccionado correctamente.
                - (401, 'Acceso denegado') cuando no se puede verificar al usuario.
                - (500, 'Error del servidor') cuando falla el servidor.
        """

        try:
            token = request.form['token']

            if self.authCon.verificar_usuario(token):
                juego = request.form['juego']
                self.gestor_juegos.seleccionar_juego(juego)

                return (200, 'OK')
            else:
                return (401, 'Acceso denegado')
        except Exception as e: 
            print(e, file=sys.stderr)
            return (500, 'Error del servidor')