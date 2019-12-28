# -*- coding: utf-8 -*-
"""
Clase encargada de llevar tablero y crear arbitro
"""
from datos import TableroInterfaz
import arbitro

class Creador(object):
    def __init__(self,tamaño,jugadores):
        self.adjudicarTamaño(tamaño)
        self.tablero = self.crearTablero(self.tamaño)
        self.jugadores = jugadores
        self.arbitro = arbitro.Arbitro(self.tablero,self.jugadores)
    
    def adjudicarTamaño(self,size):
        self.tamaño = size
        
    def crearTablero(self,tamaño):
        self.board = TableroInterfaz.Tablero(tamaño)
        return self.board.grid
   
    def obtenerEstado(self):
        pass
