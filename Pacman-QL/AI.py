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
    def __init__(self, gameboard, pos_pacman, pos_ghost, tec=None, path=None) :
        self.tablero = gameboard
        self.pos_inical = pos_pacman
        self.teclas = tec
        self.path = path

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
                
    def recorrer_tablero(self) :
        row, col = self.pos_inical
        tecla = ""
        i = j = 0
        
        if self.teclas == None :
            while i < len(self.tablero) - 1:
                
                while j < len(self.tablero[0]) - 1:
                    if j == col and i == row:
                        if self.tablero[i][j+1] in [2, 6, 5]:
                            tecla = "d"
                            #print(tecla)
                        elif self.tablero[i][j-1] in [2, 6, 5]:
                            tecla = "a"
                            #print(tecla)
                        elif self.tablero[i-1][j] in [2, 6, 5]:
                            tecla = "w"
                            #print(tecla)
                        elif self.tablero[i+1][j] in [2, 6, 5]:
                            tecla = "s"
                            #print(tecla)
                            
                        if tecla != "" :
                            keyboard.press(tecla)
                            keyboard.release(tecla)
                    j += 1
                    
                i += 1
                j = 0
                if self.tablero[row][col-1] in [1, 3] and self.tablero[row][col+1] in [1, 3] and self.tablero[row-1][col] in [1, 3] and self.tablero[row+1][col] in [1, 3]:
                    ultimo_punto = []
                    for x in range(len(self.tablero)) :
                        for z in range(len(self.tablero[0])) :
                            if self.tablero[x][z] == 2 :
                                if x != self.pos_inical[0] and z != self.pos_inical[1]:
                                    ultimo_punto.append([x, z])
                                
                    self.path, self.teclas = self.a_star([row, col], ultimo_punto[len(ultimo_punto) - 1])
                    print(self.path, self.teclas)
                    return self.path, self.teclas                 
                    
            return None, None
        
        for i in range(2) :
            if self.path[i][0] == self.pos_inical[0] and self.path[i][1] == self.pos_inical[1] :
                keyboard.press(self.teclas[i])
                keyboard.release(self.teclas[i])
                r = i
                while r >= 0 :
                    del self.path[r]
                    del self.teclas[r]
                    r -= 1
                break
                    
        if self.path == [] or self.teclas == [] :
            return None, None
        
        return self.path, self.teclas
        