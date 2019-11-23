# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 16:13:57 2019

@author: usuario
"""
import platform
import os
import Fade

class Menu:
    
    def display_menu(self):
        """
        Displays a menu with all the available options to solve the Flow Shop problem
        """
        
        option = None

        while option != "3":
            self.print_menu()
            option = input('Selecciona una opción: ')
            if option == "1":
                ejecutor = Fade.Fade()
                ejecutor.enRaya()
            elif option== "2":
                print('Juego en construcción')
            elif option != "3":
                print('ERROR, esa opción no existe!')

            if option != "3":
                input('\nPulsa cualquier tecla para volver al menú...')


    def print_menu(self):
        """
        Prints the menu
        """
        self.clear()
        print('\t\t MENU')
        print('******************************************')
        print('\t1 - EnRaya')
        print('\t2 - Futuro Juego')
        print('\t3 - Salir del programa')
        

    
    def clear(self):
        """
        Cleans the terminal
        """
        system = platform.system()
        if system == 'Windows':
            os.system('cls')
        elif system == 'Linux':
            os.system('clear')