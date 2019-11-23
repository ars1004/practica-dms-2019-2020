from conexionauthserver import *
from conexionhub import *
from conexionservidor import *

import json

class cliente:
    def registrarse():
        x = conexionauthserver()
        print('1.Registrar usuario')
        print('2.Login')
        opcion = input('Bienvenido, indique que opcion desea realizar:')
        print(opcion)
        comprobacion = 1
        if opcion == '1':
            nombre = input('Nombre de usuario: ')
            password = input('Contraseña: ')
            verificar = input('Vuelve a escribir la contraseña:')
            if password != verificar:
                bandera = 1
                while bandera==1:
                    print('Error, vuelva a introducir la contraseña')
                    password = input('Contraseña: ')
                    verificar = input('Vuelve a escribir la contraseña:')
                    if password == verificar:
                        bandera = 0
            x.register(nombre,password)
            print('Registro realizado con exito, ahora se hara el login')
            token = x.login(nombre,password)
        elif opcion == '2':
            nombre = input('Nombre de usuario: ')
            contrasena = input('Contraseña: ')
            token = x.login(nombre,contrasena)

        else :
            print('Te has equivocado hijo de la gran puta que eres tontisimo, vuelve a introducirlo')
            cliente.registrarse()
        return token
    def obtenerListaServidores(token):
        hub = conexionhub()
        lista = hub.obtenerLista(token)
        return lista 
    def seleccionarServidor(lista): 
        listas = json.loads(lista)
        for i in range(len(listas)):
            print(str(i) + ' ' + listas[i]['name'])
        opcion = int(input('Seleccione el server al que desea unirse: '))
        servidor = conexionservidor(listas[opcion]['host'],listas[opcion]['port'])
        servidor.unirse(token,nombre)
        return servidor
    def seleccionarOpciones(servidor,token):
        juegos = servidor.obtenerJuegos()
        lista_juego = json.loads(juegos)
        for i in range(len(juegos)):
            print(str(i) + ' ' + listas[i])
        

token = cliente.registrarse()
lista = cliente.obtenerListaServidores(token)
opcion = cliente.seleccionarServidor(lista)
seleccionarOpciones(opcion,token)
