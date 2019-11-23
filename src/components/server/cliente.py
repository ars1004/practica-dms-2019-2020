import conexionauthserver as auth
import conexionhub as hub
import conexionservidor as servidor

class cliente:
    #hub = 
    #servidor = 
    def registrarse():
        print('1.Registrar usuario')
        print('2.Login')
        opcion = input('Bienvenido, indique que opcion desea realizar:')
        print(opcion)
        comprobacion = False
        while comprobacion == False:
            if opcion == '1':
                nombre = input('Nombre de usuario: ')
                contrasena = input('Contraseña: ')
                verificar = input('Vuelve a escribir la contraseña:')
                if contrasena != verificar:
                    bandera = 1
                    while bandera==1:
                        print('Error, vuelva a introducir la contraseña')
                        contrasena = input('Contraseña: ')
                        verificar = input('Vuelve a escribir la contraseña:')
                        if contrasena == verificar:
                            bandera = 0
                auth.register(nombre,contrasena)
                print('Registro realizado con exito, ahora se hara el login')
                token = auth.login(nombre,contrasena)
                comprobacion == True
            elif opcion == '2':
                nombre = input('Nombre de usuario: ')
                contrasena = input('Contraseña: ')
                token = auth.login(nombre,contrasena)
                comprobacion == True
            else :
                print('Te has equivocado hijo de la gran puta que eres tontisimo, vuelve a introducirlo')
                cliente.registrarse()
            

cliente.registrarse()