# -*- coding: utf-8 -*-
from conexionauthserver import *
from conexionhub import *
from conexionservidor import *

import json
import time


class logica:
    def registrarse(nombre, contraseña):
        x = conexionauthserver()
        x.register(nombre, contraseña)
        print('Registro realizado con exito')
        token = x.login(nombre, contraseña)
        return token

    def login(nombre, contraseña):
        x = conexionauthserver()
        token = x.login(nombre, contraseña)
        return token

    def obtenerListaServidores(token):
        hub = conexionhub()
        lista = hub.obtenerLista(token)
        return lista

    def seleccionarServer(lista, nombre, token, opcion):
        servidor = conexionservidor(
            listas[opcion]['host'], listas[opcion]['port'])
        cliente.n = servidor.unirse(token, nombre)
        return servidor

    def conectarServidor(listas, opcion, nombre, token):
        servidor = conexionservidor(
        listas[opcion]['host'], listas[opcion]['port'])
        servidor.unirse(token, nombre)
        return servidor

    def seleccionJuego():
        return 0

    def obtenerEstado(servidor):
        estado = servidor.obtenerEstado()
        estados = json.loads(estado)
        return estados

    def realizarMoviento(token, servidor):
        row = input('introduce fila ')
        column = input('introduce columna ')
        data = [row, column]
        servidor.mover(token, json.dumps(data))

    def imprimir_estado(estado, nombre):
        print(f"Jugador: {nombre}")
        print(f"Turno: {estado[0]}")
        for fila in estado[1]:
            print(fila)
        print(f"Terminado: {estado[2]}")

    def estaacabado(estado):
        if estado[2]:
            print('El ganador es el jugador ' + str(estado[0]))
            return True
        else:
            return False

    def obtenerJuego(listas, opcion):
        servidor = conexionservidor(
            listas[opcion]['host'], listas[opcion]['port'])
        lista = servidor.obtenerJuegos()
        return lista

    def conectarJuego(listasservidor, opcionjuego,opcionserver, listajuego, token):
        servidor = conexionservidor(
            listasservidor[opcionserver]['host'], listasservidor[opcionserver]['port'])
        servidor.seleccionarJuego(token, listajuego[opcionjuego])
        return 'ok'
