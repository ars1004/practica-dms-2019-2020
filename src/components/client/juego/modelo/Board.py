# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 19:39:45 2019

@class Tablero
"""

class Board(object):
    
    def __init__(self,size):
        self.grid = []
        for fila in range(size):
            self.grid.append([])
            for columna in range(size):
                self.grid[fila].append(0)

                
    def colocar(self,row, column,player):
        pass
    
    def dibujarTablero(self):
        pass
    
    
    
    
class BoardEnRaya(Board):
    
    
    def __init__(self,size):
        Board.__init__(self,size)
        
    def colocar(self,row, column,jugador):
        self.grid[row][column] = jugador
        
    
    
   
        
    
    
    
	
	
    
    
    

 

 
    
        
        

