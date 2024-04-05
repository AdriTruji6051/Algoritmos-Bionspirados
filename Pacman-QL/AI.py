import keyboard
import time

class IA:
    def __init__(self, gameboard, pos_pacman, pos_ghost) :
        self.tablero = self.cuadro_alrededor_pacman(gameboard, pos_pacman)
        self.pos_inical = [2, 2]

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
            print(i)
        print('\n')
    
    def sigue_camino(self) :   
        row = self.pos_inical[0]
        col = self.pos_inical[1]
        vecino = 1
        while True :
            if self.tablero[row][col-vecino] == 2:
                time.sleep(0)
                keyboard.press('A')
                print('A')
                break
            elif self.tablero[row][col+vecino] == 2:
                time.sleep(0)
                keyboard.press('D')
                print('D')
                break
            elif self.tablero[row-vecino][col] == 2:
                time.sleep(0)
                keyboard.press('S')
                print('S')
                break
            elif self.tablero[row+vecino][col] == 2:
                time.sleep(0)
                keyboard.press('W')
                print('W')
                vecino = 1
                break
            else :
                vecino += 1
            if vecino == 2 :
                break