from conexionauthserver import *
from conexionhub import *
from conexionservidor import *

import json
import time

class datos:
    def registrarse(nombre,contraseña):
        x = conexionauthserver()
        x.register(nombre,contraseña)
        print('Registro realizado con exito')
        token = x.login(nombre,contraseña)
        return token
    def login(nombre,contraseña):
        x = conexionauthserver()
        token = x.login(nombre,contraseña)
        return token
    
    def obtenerListaServidores(token):
        hub = conexionhub()
        lista = hub.obtenerLista(token)
        return lista 
    
    def seleccionarServer(lista,nombre,token,opcion):
        servidor = conexionservidor(listas[opcion]['host'],listas[opcion]['port'])
        cliente.n = servidor.unirse(token,nombre)
        return servidor
    
    def conectarServidor(listas,opcion,nombre,token):
        servidor = conexionservidor(listas[opcion]['host'],listas[opcion]['port'])
        servidor.unirse(token,nombre)
        return servidor
    
    def seleccionJuego():
        return 0
    def obtenerEstado(servidor):
        estado = servidor.obtenerEstado()
        estados = json.loads(estado)
        return estados
    def realizarMoviento(token,servidor):
        row = input('introduce fila ')
        column = input('introduce columna ')
        data = {
            'x': row,
            'y': column
        }
        print(data)
        servidor.mover(token,json.dumps(data))
    def imprimir_estado(estado,nombre):
        print(f"Jugador: {nombre}")
        print(f"Turno: {estado[0]}")
        for fila in estado[1]:
            print(fila)
        print(f"Terminado: {estado[2]}")
    def estaacabado(estado):
        if estado[2]:
            print('El ganador es' + str(estado[0]))
            return True
        else:
            return False

    def obtenerJuego(listas,opcion):
        hub = conexionservidor(listas[opcion]['host'],listas[opcion]['port'])
        lista = hub.obtenerJuegos()
        print(lista)
        return lista