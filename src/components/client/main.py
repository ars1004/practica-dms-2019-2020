from cliente import *
def main():
    jugador = cliente()
    token,nombre = cliente.registrarse()
    lista = cliente.obtenerListaServidores(token)
    servidor = cliente.seleccionarServidor(lista,nombre,token)
    estados = cliente.obtenerEstado(servidor)
    while( not estados[2]):
        print('Lista de cosas disponibles:')
        print('1.Obtener estado del juego')
        print('2.Realizar un movimiento')
        opcion = input('Indique que opcion desea realizar:')
        comprobacion = False
        while comprobacion == False:
            if opcion == '1':
                estados = cliente.obtenerEstado(servidor)
                cliente.imprimir_estado(estados)
                comprobacion = True
            elif opcion=='2':
                cliente.realizarMoviento(token,servidor)
                comprobacion = True
            else:
                print('Opcion no válida, vuelve a intentarlo')
                print('Lista de cosas disponibles:')
                print('1.Obtener estado del juego')
                print('2.Realizar un movimiento')
                opcion = input('Indique que opcion desea realizar:')
main()

            
