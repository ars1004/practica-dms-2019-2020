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
   
    turnPlayer = None
    tablero = None
    num = 0
    
    def __init__(self, size = 3):
        
        if size>0 and size<9:
            self.board = Board.BoardEnRaya(size)
        self.tablero = self.board.grid
        iteracion = 0
        numMayor = 0
        self.players = []
        self.crearJugador
        for i in range(len(self.players)):
            numer = random.randint(0,10)
            play = Player.Player(self.num)
            if iteracion ==0:
                 numer = numMayor
                 iteracion += 1
                 self.turnPlayer = play.name
            elif numer > numMayor:
                 self.turnPlayer = play.name
                 iteracion += 1
       
    def crearJugador (self):
        self.num = self.num + 1
        self.players.append(self.num)
    
    def movePiece(self,row,column):
           self.board.colocar(row,column,self.turnPlayer)
           if (self.turnPlayer+1) < len(self.players):
               self.turnPlayer = self.players(self.turnPlayer+1)
           else:
               self.turnPlayer = self.players[0]
                
        
    def legalMove(self,row,column):
        if row >= 0 and row < len(self.tablero) and column >= 0 and column < len(self.tablero):
            if self.tablero[row][column] == 0:
                self.movePiece(row,column)
        
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
        player = self.arbitro.turnPlayer
        tablero = self.tablero
        return player, tablero, self.isFinished()
    
        
    def check(self):
        return True

