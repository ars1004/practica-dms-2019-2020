from datos import *
from interfaz import *
class main:
    nombre,password,opcion = interfaz.interfazUsuario()
    if opcion == '1':
        token = datos.registrarse(nombre,password)
    elif opcion == '2':
        token = datos.login(nombre,password)
    listaserver = datos.obtenerListaServidores(token)
    opcion,listasserver = interfaz.listaServidores(listaserver)
    servidor = datos.conectarServidor(listasserver,opcion,nombre,token)
    listajuego = datos.obtenerJuego(listasserver,opcion)
    opcion,listasjuego = interfaz.listaJuego(listajuego)
    datos.conectarJuego(listasserver,opcion,listasjuego,token)
    estaacabado = False
    while(estaacabado == False):
        estado = datos.obtenerEstado(servidor)
        datos.imprimir_estado(estado,nombre)
        opcion = interfaz.mostraropciones()
        if opcion == '1':
            datos.imprimir_estado(estado,nombre)
        elif opcion == '2':
            datos.realizarMoviento(token,servidor)
            estadomovimiento = datos.obtenerEstado(servidor)
            datos.imprimir_estado(estadomovimiento,nombre)
            if datos.estaacabado(estadomovimiento):
                estaacabado = datos.estaacabado(estadomovimiento)
        else:
            print('Opcion incorrecta vuelva a intentarlo:')
            
            
