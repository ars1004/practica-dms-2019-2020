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
        """ User creation handler.
        ---
        Performs the user creation operation, generating a new user in the database.

        Parameters:
            - request: The HTTP request received in the REST endpoint.
        Returns:
            A tuple with the following values:
                - (200, 'OK') on a successful creation.
                - (500, 'Server error') on a failed creation.
        """
        token = request.form['token']
        nombre = request.form['nombre']


        return (200, 'OK')

    def dar_de_alta(self, request):
        """ User login handler.
        ---
        Performs the user login operation, generating a new token to be used in future operations.

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