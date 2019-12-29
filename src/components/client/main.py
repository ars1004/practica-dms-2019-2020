from logica import *
from datos import *
class main:
    nombre,password,opcion = datos.interfazUsuario()
    if opcion == '1':
        token = logica.registrarse(nombre,password)
    elif opcion == '2':
        token = logica.login(nombre,password)
    listaserver = logica.obtenerListaServidores(token)
    opcionserver,listasserver = datos.listaServidores(listaserver)
    servidor = logica.conectarServidor(listasserver,opcionserver,nombre,token)
    listajuego = logica.obtenerJuego(listasserver,opcionserver)
    opcion,listasjuego = datos.listaJuego(listajuego)
    logica.conectarJuego(listasserver,opcion,opcionserver,listasjuego,token)
    #servidor = datos.conectarServidor(listasserver,opcion,nombre,token)
    estaacabado = False
    while(estaacabado == False):
        estadojuego = logica.obtenerEstado(servidor)
        logica.imprimir_estado(estadojuego,nombre)
        opcion = datos.mostraropciones()
        if opcion == '1':
            logica.imprimir_estado(estadojuego,nombre)
        elif opcion == '2':
            logica.realizarMoviento(token,servidor)
            estadomovimiento = logica.obtenerEstado(servidor)
            if logica.estaacabado(estadomovimiento):
                estaacabado = logica.estaacabado(estadomovimiento)
        else:
            print('Opcion incorrecta vuelva a intentarlo:')
        if logica.estaacabado(estadojuego):
            estaacabado = logica.estaacabado(estadomovimiento) 
            
