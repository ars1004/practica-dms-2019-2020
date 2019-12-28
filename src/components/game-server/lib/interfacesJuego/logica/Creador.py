# -*- coding: utf-8 -*-
"""
Clase encargada de llevar tablero y crear arbitro
"""
from lib.interfacesJuego.datos.TableroInterfaz import Tablero
from lib.interfacesJuego.logica.arbitro import Arbitro

class Creador(object):
    def __init__(self,tamaño,jugadores):
        self.adjudicarTamaño(tamaño)
        self.tablero = self.crearTablero(self.tamaño)
        self.jugadores = jugadores
        self.arbitro = Arbitro(self.tablero,self.jugadores)
    
    def adjudicarTamaño(self,size):
        self.tamaño = size
        
    def crearTablero(self,tamaño):
        self.board = Tablero(tamaño)
        return self.board.grid
   
    def obtenerEstado(self):
        return 1, [[0,0,0],[0,0,0],[0,0,0]], False # Debería usar el metodo de los hijos
