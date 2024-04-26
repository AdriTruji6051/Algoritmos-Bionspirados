import keyboard
import time
class Node:
    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position
        self.g = 0  # Costo acumulado desde el nodo inicial
        self.h = 0  # Heurística (distancia Manhattan al nodo objetivo)
        self.f = 0  # Costo total: g + h
        

class IA:
    def __init__(self, gameboard, pos_pacman, pos_ghost) :
        self.tablero = gameboard
        self.pos_inical = pos_pacman

    def imprimir_tablero(self) :
        for i in self.tablero :
            print(str(i) + ',')
        print('\n')
    
    def a_star(self, inicio, fin) :
        lista_abierta = []
        lista_cerrada = []
        nodo_inicio = Node(None, inicio)
        nodo_final = Node(None, fin)
        
        lista_abierta.append(nodo_inicio)
        
        while lista_abierta != [] :
            nodo_actual = lista_abierta[0]
            indice = 0
            for numero, nodo, in enumerate(lista_abierta) :
                if nodo.f < nodo_actual.f :
                    print(nodo.position)
                    nodo_actual = nodo
                    indice = numero
        
            lista_abierta.pop(indice)
            lista_cerrada.append(nodo_actual)
            
            if nodo_actual.position[0] == nodo_final.position[0] and nodo_actual.position[1] == nodo_final.position[1]:
                path = []
                actual = nodo_actual
                while actual is not None:
                    path.append(actual.position)
                    actual = actual.parent
                path = path[::-1]
                dirs = []
                for i in range(len(path) - 1) :
                    dir = ""
                    if path[i][0] == path[i+1][0] and path[i][1] < path[i + 1][1] :
                        dir = "d"
                    elif path[i][0] == path[i+1][0] :
                        dir = "a"
                    elif path[i][1] == path[i + 1][1] and path[i][0] < path[i+1][0]:
                        dir = "s"
                    elif path[i][1] == path[i + 1][1]:
                        dir = "w"
                    dirs.append(dir)
                return path, dirs
                
            vecinos = []
            for dir in [(-1, 0), (1, 0), (0, -1), (0, 1)] :
                nueva_dir = [nodo_actual.position[0] + dir[0], nodo_actual.position[1] + dir[1]]
                
                if nueva_dir[0] > len(self.tablero) - 1 or nueva_dir[0] < 0 or nueva_dir[1] > len(self.tablero[0]) - 1 or nueva_dir[1] < 0 :
                    continue
                
                if self.tablero[nueva_dir[0]][nueva_dir[1]] not in [2, 1, 5, 6]:
                    continue
                
                nodo_nuevo = Node(nodo_actual, nueva_dir)
                
                vecinos.append(nodo_nuevo)
                
            for vecino in vecinos :
                if vecino in lista_cerrada :
                    continue
                
                vecino.g = nodo_actual.g + 1
                vecino.h = abs(vecino.position[0] - nodo_final.position[0]) + abs(vecino.position[1] - nodo_final.position[1])
                vecino.f = vecino.g + vecino.h
                
                if vecino in lista_abierta :
                    if vecino.g > nodo_actual.g :
                        continue
                    
                lista_abierta.append(vecino)
                            
        return None

    def sigue_camino(self) :
        row = self.pos_inical[0]
        col = self.pos_inical[1]
        vecinoID = 0
        vecinoAB = 0
        while True :
            
            vecinoAB += 1
            if not row - vecinoAB > 4 and row + vecinoAB < len(self.tablero) - 4: 
                vecinoAB -= 1
                continue
            vecinoID += 1
            if not col - vecinoID > 0 and col + vecinoID < len(self.tablero[0]) - 1:
                vecinoID -= 1
                continue 

            if self.tablero[row][col-vecinoID] in [2, 5, 6]:
                index, teclas = self.a_star( [row, col], [row, col-vecinoID] )
                print(teclas)
                break
            elif self.tablero[row][col+vecinoID] in [2, 5, 6]:
                index, teclas = self.a_star( [row, col], [row, col+vecinoID] )
                print(teclas)
                break
            elif self.tablero[row-vecinoAB][col] in [2, 5, 6]:
                index, teclas = self.a_star( [row, col], [row - vecinoAB, col] )
                print(teclas)
                break
            elif self.tablero[row+vecinoAB][col] in [2, 5, 6]:
                index, teclas = self.a_star( [row, col], [row + vecinoAB, col] )
                print(teclas)
                break
            else :
                vecinoAB += 1
                if not row - vecinoAB > 4 and row + vecinoAB < len(self.tablero) - 4: 
                    vecinoAB -= 1
                    continue
                vecinoID += 1
                if not col - vecinoID > 0 and col + vecinoID < len(self.tablero[0]) - 1:
                    vecinoID -= 1
                    continue 
        


