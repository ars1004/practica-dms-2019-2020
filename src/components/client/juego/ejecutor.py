# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 21:07:32 2019

@author: usuario
"""
import pygame
from modelo import board
from modelo import color

def main():
    """
    Main function
    """
    pygame.init()
    
    # Establecemos el LARGO y ALTO de la pantalla
    DIMENSION_VENTANA = [255, 255]
    pantalla = pygame.display.set_mode(DIMENSION_VENTANA)
    
    # Iteramos hasta que el usuario pulse el botón de salir.
    hecho = False
    
    # Lo usamos para establecer cuán rápido de refresca la pantalla.
    reloj = pygame.time.Clock()
    
    while not hecho:
        for evento in pygame.event.get(): 
            if evento.type == pygame.QUIT: 
                hecho = True
            elif evento.type == pygame.MOUSEBUTTONDOWN:
            # El usuario presiona el ratón. Obtiene su posición.
                pos = pygame.mouse.get_pos()
            # Cambia las coordenadas x/y de la pantalla por coordenadas reticulares
                columna = pos[0] // (board.LARGO + board.MARGEN)
                fila = pos[1] // (board.ALTO + board.MARGEN)
            # Establece esa ubicación a cero
                board.grid[fila][columna] = 1
                print("Click ", pos, "Coordenadas de la retícula: ", fila, columna)
                
    # Establecemos el fondo de pantalla.
    pantalla.fill(color.NEGRO)
    
    board.dibujarTablero()
    
    # Limitamos a 60 fotogramas por segundo.
    reloj.tick(60)
    
     # Avanzamos y actualizamos la pantalla con lo que hemos dibujado.
    pygame.display.flip()
    
    pygame.quit()
    
    
                
                
                
                