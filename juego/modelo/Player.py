# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 15:14:23 2019

@author: usuario
"""
from lib.game.modelo import Color

class Player(object):
    
    name = None
    col = None
    num = 0
    def __init__(self,num):
        self.name = num
        
    def returnName (self):
        return self.name
    
    def returnColor (self):
        return self.col
        