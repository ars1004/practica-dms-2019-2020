#!/usr/bin/env python3

from flask import Flask, escape, request, abort
from lib.presentation.restapi import RestApi

rest_api = RestApi()

app = Flask(__name__)

@app.route('/')
def status():
    """ Status handler. Useful to test whether the server is running or not.
    ---
    get:
        summary: Status handler.
        description: Status testing endpoing.
        responses:
            200:
                description: The server is running correctly.
    """
    (code, message) = rest_api.status(request)
    if (code == 200):
        return 'Running'
    else:
        abort(code)

@app.route('/unirse', methods = ['POST'])
def unirse():
    (code, message) = rest_api.unirse(request)
    if (code == 200):
        return message
    else:
        abort(code)

@app.route('/register', methods = ['POST'])
def dar_de_alta():
    (code, message) = rest_api.dar_de_alta(request)
    if (code == 200):
        return message # token
    else:
        abort(code)

@app.route('/unregister', methods = ['POST'])
def dar_de_baja():
    (code, message) = rest_api.dar_de_baja(request)
    if (code == 200):
        return message
    else:
        abort(code)

@app.route('/obtener/estado', methods = ['GET'])
def obtener_estado():
    (code, message) = rest_api.obtener_estado(request)
    if (code == 200):
        return message
    else:
        abort(code)

@app.route('/obtener/juegos', methods = ['GET'])
def obtener_juegos():
    (code, message) = rest_api.obtener_juegos(request)
    if code == 200:
        return message
    else:
        abort(code)

@app.route('/seleccionar/juego', methods = ['POST'])
def seleccionar_juego():
    (code, message) = rest_api.seleccionar_juego(request)
    if code == 200:
        return message
    else:
        abort(code)

@app.route('/mover', methods = ['POST'])
def hacer_movimiento():
    (code, message) = rest_api.hacer_movimiento(request)
    if (code == 200):
        return message
    else:
        abort(code)