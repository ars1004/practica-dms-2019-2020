# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 16:40:43 2019

@author: usuario
"""

import arbitroEnRaya



class Fade:   

    def __init__(self):
        self.arbitro = arbitroEnRaya.Arbitro()
    
    def enRaya(self):
        flag = False
        while flag != True:
            self.mostrarEstado()
            row = int(input('introduce fila '))
            column = int(input('introduce columna '))
            self.arbitro.legalMove(row,column)
            flag = self.arbitro.isFinished()
            for i in self.arbitro.board.grid:
                print(i)
       
        
    def mostrarEstado(self):
        print('El jugador con turno es: ')
        player = self.arbitro.turnPlayer
        print(player)
        