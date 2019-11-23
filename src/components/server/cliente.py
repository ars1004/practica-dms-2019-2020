from conexionauthserver import *
import conexionhub as hub
import conexionservidor as servidor

class cliente:
    def registrarse():
        x = conexionauthserver
        print('1.Registrar usuario')
        print('2.Login')
        opcion = input('Bienvenido, indique que opcion desea realizar:')
        print(opcion)
        comprobacion = False
        while comprobacion == False:
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
                comprobacion == True
            elif opcion == '2':
                nombre = input('Nombre de usuario: ')
                contrasena = input('Contraseña: ')
                token = auth.login(nombre,contrasena)
                comprobacion == True
            else :
                print('Te has equivocado hijo de la gran puta que eres tontisimo, vuelve a introducirlo')
                cliente.registrarse()
    def obtenerListaServidores():
        hub.obtenerLista()      

cliente.registrarse()
cliente.obtenerListaServidores()