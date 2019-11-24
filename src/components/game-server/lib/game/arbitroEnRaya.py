# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 19:47:19 2019
Arbitro del juego
"""

from lib.game.modelo import Player
import random
import numpy as np
from lib.game.modelo import Board

class Arbitro:
   
    turnPlayer = 1
    tablero = None
    num = 0
    
    def __init__(self, size = 3):
        
        if size>0 and size<9:
            self.board = Board.BoardEnRaya(size)
        self.tablero = self.board.grid
        iteracion = 0
        numMayor = 0
        self.players = []
       
    def crearJugador (self):
        if self.num == 3:
            raise # si se intentan unir mas de dos personas
        self.num = self.num + 1
        self.players.append(self.num)
        
    
    def movePiece(self,row,column):
        if self.legalMove(row,column):
           self.board.colocar(row,column,self.turnPlayer)
           self.turnPlayer = 3 - self.turnPlayer
        
    def legalMove(self,row,column):
        if row >= 0 and row < len(self.tablero) and column >= 0 and column < len(self.tablero):
            if self.tablero[row][column] == 0:
                return True
        return False
        
    def isFinished(self):
        noZero = 0
        for i in range(len(self.tablero)):
            if self.enFila(i) == True:
                return True
            for j in range(len(self.tablero)):
                if self.enColumna(j) == True:
                   return True
                if self.tablero[i][j] != 0:
                    noZero += 1
                    
        if noZero ==  len(self.tablero)*len(self.tablero):
            return True
        else:
            return False
       
    def enFila(self,row):
        noZero = 0
        valor = 0
        for x in self.tablero[row]:
            if x != 0:
                valor += x
                noZero += 1
        if (noZero == valor or noZero == valor/2) and noZero == len(self.tablero):
            return True
        else:
            return False
    
    def enColumna(self,column):
        noZero = 0
        valor = 0
        for i in range(len(self.tablero)):
            for j in range(len(self.tablero)):
                if j == column:
                    if self.tablero[i][j] != 0:
                        valor += self.tablero[i][j]
                        noZero += 1
        if noZero == len(self.tablero) and (noZero == valor or noZero == valor/2):
            return True
        else:
            return False
                
        
    def obtenerEstado(self):
        player = self.turnPlayer
        tablero = self.tablero
        return player, tablero, self.isFinished()
    
        
    def check(self):
        return True

