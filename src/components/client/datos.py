from logica import *
import json
import time
class datos:
    def interfazUsuario():
        print('1.Registrar usuario')
        print('2.Login')
        opcion = input('Bienvenido, indique que opcion desea realizar:')
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
        elif opcion == '2':
            nombre = input('Nombre de usuario: ')
            password = input('Contraseña: ')
        return nombre,password,opcion
    
    def listaServidores(lista):
        listas = json.loads(lista)
        for i in range(len(listas)):
            print(str(i) + ' ' + listas[i]['name'])
        opcion = int(input('Seleccione el server al que desea unirse: '))
        return opcion,listas
    def listaJuego(lista):
        listas = json.loads(lista)
        for i in range(len(listas)):
            print(str(i) + ' ' + listas[i])
        opcion = int(input('Seleccione el juego al que desea jugar: '))
        return opcion,listas
    def posiblesJuegos(lista):
        return 0
    def mostraropciones():
        print('Lista de cosas disponibles:')
        print('1.Obtener estado del juego')
        print('2.Realizar un movimiento')
        opcion = input('Indique que opcion desea realizar:')
        return opcion
    