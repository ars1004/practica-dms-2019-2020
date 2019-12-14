# -*- coding: utf-8 -*-
"""
Clase encargada de manejar los Jugadores
"""


class Jugador(object):
    id = None
    """
    Constructor del jugador
    """
    def __init__(self,num):
        self.id = num
    
    """
    Devuelve el Id del jugador 
    """
    def returnId (self):
        return self.id
  