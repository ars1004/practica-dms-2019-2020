"""
Arbitro del juego Damas
"""

import arbitro

class ArbitroEnRaya(arbitro.Arbitro):
    num = 0
    grid = []
    jugadores = []
    jugadorTurno = 0
    def __init__(self,tablero,jugadores):
        arbitro.Arbitro.__init__(tablero,jugadores)
        
    def colocarPeonesIniciales (self):
        self.grid = [[0, 'n', 0, 'n', 0, 'n', 0, 'n'],
           ['n', 0, 'n', 0, 'n', 0, 'n', 0],
           [0, 'n', 0, 'n', 0, 'n', 0, 'n'],
           [0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0],
           ['b', 0, 'b', 0, 'b', 0, 'b', 0],
           [0, 'b', 0, 'b', 0, 'b', 0, 'b'],
           ['b', 0, 'b', 0, 'b', 0, 'b', 0]]
        
    def moverPieza(self,filaI,columnaI,filaF,columnaF,jugador):
        if self.jugadorTurno == jugador and self.movimientoLegal(filaI,columnaI,filaF,columnaF):
            if self.jugadorTurno == 1 and not(self.cambiarDamas(filaF)):
                self.grid[filaI][columnaI] = 0
                self.grid[filaF][columnaF] = 'b'
            else:
                self.grid[filaI][columnaI] = 0
                self.grid[filaF][columnaF] = 'B'
            if self.jugadorTurno == 2 and not(self.cambiarDamas(filaF)):
                self.grid[filaI][columnaI] = 0
                self.grid[filaF][columnaF] = 'n'
            else:
                self.grid[filaI][columnaI] = 0
                self.grid[filaF][columnaF] = 'N'
            self.jugadorTurno = self.obtenerJugadorConTurno
        else:
            raise
    
    def cambiarDamas(self,fila):
        if self.jugadorTurno == 1 and fila == 0:
            return True
        else:
            return False
        if self.jugadorTurno == 2 and fila == 7:
            return True
        else:
            return False
   
    def movimientoLegal(self,fila1,columna1,fila2,columna2):
        if self.grid[fila1][columna1] is not 0:
            if self.grid[fila1][columna1] == 'n' or self.grid[fila1][columna1] == 'b':
                if fila1 == 2 or fila1 == 5:
                    self.devolver = self.esValidoPeonPrimero(self,fila1,columna1,fila2,columna2)
                else:
                    self.devolver = self.esValidoPeonSegundo(self,fila1,columna1,fila2,columna2)
            elif self.grid[fila1][columna1] == 'N' or self.grid[fila1][columna1] == 'B':
                self.devolver = self.esValidoDamas(self,fila1,columna1,fila2,columna2)
        return self.devolver
    
    def esValidoPeonPrimero(self,fila1,columna1,fila2,columna2):
        if self.grid[fila1][columna1] is not 0:
            if self.grid[fila2][columna2] == 0:
                if self.esMovimientoDiagonalPrimero(self,fila1,columna1,fila2,columna2) == True:
                    return True
        else:
            return False
    
    def esMovimientoDiagonalPrimero(self,fila1,columna1,fila2,columna2):
        if (fila1 >= 0) and (fila1 <= 7) and (fila2 >= 0) and (fila2 <= 7) and (columna1 >= 0) and (columna1 <= 7) and (columna2 >= 0) and (columna2 <= 7):
            resta = (fila1+columna1)-(fila2+columna2)
            if self.grid[fila1][columna1] == 'n':
                if resta == 0 or resta==2 or resta == 4:
                    if resta == 4:
                        if self.grid[fila1+1][columna1+1] == 'b':
                            self.grid[fila1+1][columna1+1] = 0
                        elif self.grid[fila1+1][columna1-1] == 'b':
                            self.grid[fila1+1][columna1-1] = 0
                    return True
            elif self.grid[fila1][columna1] == 'b':
                if resta == 0 or resta == -2 or resta == -4:
                    if resta == 4:
                        if self.grid[fila1-1][columna1+1] == 'n':
                            self.grid[fila1-1][columna1+1] = 0
                        elif self.grid[fila1-1][columna1-1] == 'n':
                            self.grid[fila1-1][columna1-1] = 0
                    return True
            else:
                return False
        else:
            return False
				
    def esValidoPeonSegundo(self,fila1,columna1,fila2,columna2):
        if self.grid[fila1][columna1] is not 0:
            if self.grid[fila2][columna2] == 0:
                if self.esMovimientoDiagonalSegundo(self,fila1,columna1,fila2,columna2) == True:
                    return True
        else:
            return False
    
    def esMovimientoDiagonalSegundo(self,fila1,columna1,fila2,columna2):
        if (fila1 >= 0) and (fila1 <= 7) and (fila2 >= 0) and (fila2 <= 7) and (columna1 >= 0) and (columna1 <= 7) and (columna2 >= 0) and (columna2 <= 7):
            resta = (fila1+columna1)-(fila2+columna2)
            if self.grid[fila1][columna1] == 'n':
                if self.grid[fila1+1][columna1+1]==0 or self.grid[fila1+1][columna1+1]=='b' or self.grid[fila1+1][columna1+1]=='B':
                    self.grid[fila1+1][columna1+1]=0
                    if resta == 0 or resta==4:
                        return True
                elif self.grid[fila1+1][columna1-1]==0 or self.grid[fila1+1][columna1-1]=='b' or self.grid[fila1+1][columna1-1]=='B':
                    self.grid[fila1+1][columna1-1]=0
                    if resta == 0 or resta==4:
                        return True
            elif self.grid[fila1][columna1] == 'b':
                if self.grid[fila1-1][columna1+1]==0 or self.grid[fila1-1][columna1+1]=='n' or  self.grid[fila1-1][columna1+1]=='N':
                    self.grid[fila1-1][columna1+1]=0
                    if resta == 0 or resta == -4:
                        return True
                elif self.grid[fila1-1][columna1-1]==0 or self.grid[fila1-1][columna1-1]=='n' or self.grid[fila1-1][columna1-1]=='N':
                    self.grid[fila1-1][columna1-1]=0
                    if resta == 0 or resta == -4:
                        return True
            else:
                return False
        else:
            return False
				
    def esValidoDamas(self,fila1,columna1,fila2,columna2):
        if self.grid[fila1][columna1] is not 0:
            if self.grid[fila2][columna2] == 0:
                if self.esMovimientoDiagonalDama(self,fila1,columna1,fila2,columna2) == True:
                    return True
        else:
            return False					

    def esMovimientoDiagonalDama(self,fila1,columna1,fila2,columna2):
        if (fila1 >= 0) and (fila1 <= 7) and (fila2 >= 0) and (fila2 <= 7) and (columna1 >= 0) and (columna1 <= 7) and (columna2 >= 0) and (columna2 <= 7):
            resta = (fila1+columna1)-(fila2+columna2)
            if self.grid[fila1][columna1] == 'B':
                if resta == 0 or resta==2 or resta==4 or resta==6 or resta==8 or resta==10 or resta==12:
                    if resta > 2:
                        if (fila1+1 <= fila2) and self.grid[fila1+1][columna1] == 'n' or self.grid[fila1+1][columna1] == 'N':
                            self.grid[fila1+1][columna1] = 0
                        elif (fila1+3 <= fila2) and self.grid[fila1+3][columna1] == 'n' or self.grid[fila1+3][columna1] == 'N':
                            self.grid[fila1+3][columna1] = 0
                        elif (fila1+5 <= fila2) and self.grid[fila1+5][columna1] == 'n' or self.grid[fila1+5][columna1] == 'N':
                            self.grid[fila1+5][columna1] = 0
                        elif (fila1+7 <= fila2) and self.grid[fila1+7][columna1] == 'n' or self.grid[fila1+7][columna1] == 'N':
                            self.grid[fila1+7][columna1] = 0
                    return True
            elif self.grid[fila1][columna1] == 'N':
                if resta == 0 or resta == -2 or resta==-4 or resta==-6 or resta==-8 or resta==-10 or resta==-12:
                    if resta < -2:
                        if (fila1-1 <= fila2) and self.grid[fila1-1][columna1] == 'n' or self.grid[fila1-1][columna1] == 'N':
                            self.grid[fila1-1][columna1] = 0
                        elif (fila1-3 <= fila2) and self.grid[fila1-3][columna1] == 'n' or self.grid[fila1-3][columna1] == 'N':
                            self.grid[fila1-3][columna1] = 0
                        elif (fila1-5 <= fila2) and self.grid[fila1-5][columna1] == 'n' or self.grid[fila1-5][columna1] == 'N':
                            self.grid[fila1-5][columna1] = 0
                        elif (fila1-7 <= fila2) and self.grid[fila1-7][columna1] == 'n' or self.grid[fila1-7][columna1] == 'N':
                            self.grid[fila1-7][columna1] = 0
                    return True
            else:
                return False
        else:
            return False
    
    def obtenerJugadorConTurno(self):
        self.jugadorTurno = arbitro.Arbitro.obtenerJugadorConTurno
        return self.jugadorTurno
    
    def estaAcabado(self):
        contadorB = 0
        contadorN = 0
        for i in range(len(self.grid)):
            for j in i:
                if j=='n' or j=='N':
                    contadorN+=1
                elif j=='b' or j=='B':
                    contadorB+=1
        if contadorN==0 or contadorB==0:
            return True
        else:
            return False
        
             
    def check(self):
        return True

