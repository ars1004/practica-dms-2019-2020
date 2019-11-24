# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 15:48:59 2019
Clase enumerada color
"""
import random

class Color:
    
    def __init__(self):
        num1 = random.randint((0,255))
        num2 = random.randint((0,255))
        num3 = random.randint((0,255))
        self.color = (num1,num2,num3)

