#!/usr/bin/env python3

from flask import Flask, escape, request, abort
from lib.presentation.restapi import RestApi

rest_api = RestApi()

app = Flask(__name__)

@app.route('/')
def status():
    """ Endpoint de verificación de estado. 
    Util para comprobar la conexión con el servidor.
    ---
    get:
        resumen: Verificación de estado.
        respuestas:
            200:
                descripción: El servidor se está ejecutando correctamente.
    """
    (code, message) = rest_api.status(request)
    if (code == 200):
        return 'Running'
    else:
        abort(code)

@app.route('/unirse', methods = ['POST'])
def unirse():
    """ Endpoint de conexion de usuarios.
    ---
    post:
        resumen: Usuario se une al servidor.
        descripción: El endpoint se usa para que un usuario se conecte al servidor.
        parámetros:
            - token: Token del usuario.
            - nombre: (opcional) Nombre del usuario en la partida.
        respuestas:
            200:
                descripción: El usuario se ha unido correctamente.
            401:
                descripción: El token del usuario no se ha podido verificar.
            500:
                descripción: El usuario no se ha podido unir.
    """
    (code, message) = rest_api.unirse(request)
    if (code == 200):
        return message
    else:
        abort(code)

@app.route('/register', methods = ['POST'])
def dar_de_alta():
    """ Endpoint de registro de servidor.
    ---
    post:
        resumen: Registra el servidor en el hub.
        parámetros:
            - nombre: (opcional) Nombre del servidor.
            - token: token de usuario
        respuestas:
            200:
                descripción: El servidor se ha registrado correctamente.
            401:
                descripción: El token del usuario no se ha podido verificar.
            500:
                descripción: El servidor no se ha podido registrar.
    """
    (code, message) = rest_api.dar_de_alta(request)
    if (code == 200):
        return message # token
    else:
        abort(code)

@app.route('/unregister', methods = ['POST'])
def dar_de_baja():
    """ Endpoint de borrado de servidor.
    ---
    post:
        resumen: Borra el servidor del hub.
        parámetros:
            - name: (opcional) Nombre del servidor.
            - token: token de usuario
        respuestas:
            200:
                descripción: El servidor se ha borrado correctamente.
            401:
                descripción: El token del usuario no se ha podido verificar.
            500:
                descripción: El servidor no se ha podido borrar.
    """
    (code, message) = rest_api.dar_de_baja(request)
    if (code == 200):
        return message
    else:
        abort(code)

@app.route('/obtener/estado', methods = ['GET'])
def obtener_estado():
    """ Endpoint de obtencion del estado de la partida.
    ---
    post:
        resumen: Obtiene el estado de la partida.
        respuestas:
            200:
                descripción: Se ha obtenido el estado. El contenido de la respuesta
                    contiene el estado en formato JSON.
            500:
                descripción: No se ha podido obtener el estado de la partida.
    """
    (code, message) = rest_api.obtener_estado(request)
    if (code == 200):
        return message
    else:
        abort(code)

@app.route('/obtener/juegos', methods = ['GET'])
def obtener_juegos():
    """ Endpoint de obtencion de los juegos que dispone el servidor.
    ---
    post:
        resumen: Obtiene los juegos que tiene el servidor.
        respuestas:
            200:
                descripción: Se han obtenido los juegos. El contenido de la respuesta
                    contiene los juegos en formato JSON.
            500:
                descripción: No se han podido obtener los juegos.
    """
    (code, message) = rest_api.obtener_juegos(request)
    if code == 200:
        return message
    else:
        abort(code)

@app.route('/seleccionar/juego', methods = ['POST'])
def seleccionar_juego():
    """ Endpoint de seleccion de juego.
    ---
    post:
        resumen: Selecciona el juego que se va a jugar en el servidor.
        parámetros:
            - token: Token del usuario.
            - juego: Juego que se quiere seleccionar.
        respuestas:
            200:
                descripción: El juego se ha seleccionado correctamente.
            401:
                descripción: El token del usuario no se ha podido verificar.
            500:
                descripción: El juego no se ha podido seleccionar.
    """
    (code, message) = rest_api.seleccionar_juego(request)
    if code == 200:
        return message
    else:
        abort(code)

@app.route('/mover', methods = ['POST'])
def hacer_movimiento():
    """ Endpoint de realizacion de movimiento.
    ---
    post:
        resumen: Hace un movimiento en el juego.
        parámetros:
            - token: Token del usuario.
            - movimiento: Movimiento del usuario.
        respuestas:
            200:
                descripción: El movimiento se ha realizado correctamente.
            401:
                descripción: El token del usuario no se ha podido verificar.
            500:
                descripción: El movimiento no se ha podido realizar.
    """
    (code, message) = rest_api.hacer_movimiento(request)
    if (code == 200):
        return message
    else:
        abort(code)