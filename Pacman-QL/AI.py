import keyboard
import time

class IA:
    def __init__(self, gameboard, pos_pacman, pos_ghost) :
        self.tablero = gameboard
        self.pos_inical = pos_pacman

    def cuadro_alrededor_pacman(self, tablero_completo, posicio_pacman) :
        cuadro = []
        fila = []
        row, col = posicio_pacman
        for i in range(row-2, row+3) :
            for j in range(col-2, col+3) :
                fila.append(tablero_completo[i][j])
            cuadro.append(fila)
            fila = []
        return cuadro

    def imprimir_tablero(self) :
        for i in self.tablero :
            print(str(i) + ',')
        print('\n')
    
    def sigue_camino(self) :   
        row = self.pos_inical[0]
        col = self.pos_inical[1]
        vecinoAB = 0
        vecinoID = 0
        while True :
            print(vecinoID)
            #self.imprimir_tablero()
            if self.tablero[row][col-vecinoID] == 2:
                keyboard.press('a')
                time.sleep(0.1)
                keyboard.release('a')
                break
            elif self.tablero[row][col+vecinoID] == 2:
                keyboard.press('d')
                time.sleep(0.1)
                keyboard.release('d')
                break
            elif self.tablero[row-vecinoAB][col] == 2:
                keyboard.press('w')
                time.sleep(0.1)
                keyboard.release('w')
                break
            elif self.tablero[row+vecinoAB][col] == 2:
                keyboard.press('s')
                time.sleep(0.1)
                keyboard.release('s')
                break
            else :
                if row > 3 and row < len(self.tablero): 
                    vecinoAB += 1
                if col > 0 and col < len(self.tablero[0]) - 2:
                    vecinoID += 1
