# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 16:40:43 2019

@author: usuario
"""

import arbitroEnRaya
import pygame



class Fade:   

    def __init__(self):
        self.arbitro = arbitroEnRaya.Arbitro()
    
    def enRaya(self):
        pygame.init()
        flag = False
        while flag != True:
            self.mostrarEstado()
            row = int(input('introduce fila '))
            column = int(input('introduce columna '))
            self.arbitro.legalMove(row,column)
            flag = self.arbitro.isFinished()
            for i in self.arbitro.board.grid:
                print(i)
            pygame.quit()
        self.mostrarResultadoFinal()
        pygame.quit()
        
    def mostrarEstado(self):
        print('El jugador con turno es: ')
        player = self.arbitro.turnPlayer
        print(player)
        