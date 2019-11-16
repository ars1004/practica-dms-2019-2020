from flask import Flask, escape, request, abort

from lib.util.auth_server_util import authServerCon
from lib.util.hub_server_util import hubServerCon

import json

class RestApi():
    """ REST API facade.
    ---
    This class is a facade with the operations provided through the REST API.
    """
    def __init__(self):
        self.authCon = authServerCon()
        self.hubCon = hubServerCon()

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
                - (401, 'Error al verificar al usuario') cuando el token es erroneo
                - (500, 'Server error') cuando ocurre un error.
        """
        try:
            token = request.form['token']
            nombre = ''
            if 'nombre' in request.form:
                nombre = request.form['nombre']
            
            if self.authCon.verificar_usuario(token):
                #TODO unir al usuario al servidor
                return (200, 'OK')
            else:
                return (401, 'Error al verificar al usuario')
        except:
            return (500, 'Server error')

    def dar_de_alta(self, request):
        """ Da de alta el servidor en el hub.

        Parameters:
            - request: The HTTP request received in the REST endpoint.
        Returns:
            A tuple with the following values:
                - (200, authentication token) on a successful login.
                - (401, 'Unauthorized') on a failed login.
        """
        if self.hubCon.darDeAlta():
            return (200, 'OK')
        else:
            return (500, 'Error')

    def dar_de_baja(self, request):
        """ Token checking handler.
        ---
        Checks the validity of an authentication token.

        Parameters:
            - request: The HTTP request received in the REST endpoint.
        Returns:
            A tuple with the following values:
                - (200, 'OK') when the provided token is valid.
                - (401, 'Unauthorized') for an incorrect token.
        """
        if self.hubCon.darDeBaja():
            return (200, 'OK')
        else:
            return (500, 'Error')

    def obtener_estado(self, request):
        """ Scores listing handler.
        ---
        Retrieves a list of scores.

        Parameters:
            - request: The HTTP request received in the REST endpoint.
        Returns:
            A tuple with the following values:
                - (200, list of score records) when the list was successfully retrieved.
        """
        #TODO llamar a obtener estado del juego.
        return (200, 'estado')

    def hacer_movimiento(self, request):
        """ Scores increasing handler.
        ---
        Increments (or decrements) the score of a user

        Parameters:
            - request: The HTTP request received in the REST endpoint.
        Returns:
            A tuple with the following values:
                - (200, 'OK') when the score was successfully updated.
                - (401, 'Unauthorized') when the user cannot update the scores.
        """
        try:
            movimiento = request.form['movimiento']
        except:
            return (500, 'Error en el envio')


        #TODO llamar a hacer movimiento con el movimiento obtenido de request

        return (200, 'movimiento hecho')

    def obtener_juegos(self, request):
        #TODO obtener los juegos disponibles

        return (200, 'juego')

    def seleccionar_juego(self, request):
        #TODO seleccionar juego

        return (200, 'Juego seleccionado correctamente')