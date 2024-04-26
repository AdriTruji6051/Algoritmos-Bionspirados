import time
class Node:
    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position
        self.g = 0  # Costo acumulado desde el nodo inicial
        self.h = 0  # Heurística (distancia Manhattan al nodo objetivo)
        self.f = 0  # Costo total: g + h

class Astar:
    def __init__(self, start, goal, tablero) :
        self.tablero = tablero
        self.inicio = start
        self.fin = goal
        
        
    def a_star(self) :
        lista_abierta = []
        lista_cerrada = []
        nodo_inicio = Node(None, self.inicio)
        nodo_final = Node(None, self.fin)
        
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
                
                if self.tablero[nueva_dir[0]][nueva_dir[1]] not in [2, 1]:
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
    
grid = [
    [3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3],
    [3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3],
    [3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3],
    [3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3],  
    [3,2,2,2,2,2,2,2,2,2,2,2,2,3,3,2,2,2,2,2,2,2,2,2,2,2,2,3],
    [3,2,3,3,3,3,2,3,3,3,3,3,2,3,3,2,3,3,3,3,3,2,3,3,3,3,2,3],
    [3,6,3,3,3,3,2,3,3,3,3,3,2,3,3,2,3,3,3,3,3,2,3,3,3,3,6,3],
    [3,2,3,3,3,3,2,3,3,3,3,3,2,3,3,2,3,3,3,3,3,2,3,3,3,3,2,3],
    [3,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,3],
    [3,2,3,3,3,3,2,3,3,2,3,3,3,3,3,3,3,3,2,3,3,2,3,3,3,3,2,3],
    [3,2,3,3,3,3,2,3,3,2,3,3,3,3,3,3,3,3,2,3,3,2,3,3,3,3,2,3],
    [3,2,2,2,2,2,2,3,3,2,2,2,2,3,3,2,2,2,2,3,3,2,2,2,2,2,2,3],
    [3,3,3,3,3,3,2,3,3,3,3,3,1,3,3,1,3,3,3,3,3,2,3,3,3,3,3,3],
    [3,3,3,3,3,3,2,3,3,3,3,3,1,3,3,1,3,3,3,3,3,2,3,3,3,3,3,3],
    [3,3,3,3,3,3,2,3,3,1,1,1,1,1,1,1,1,1,1,3,3,2,3,3,3,3,3,3],
    [3,3,3,3,3,3,2,3,3,1,3,3,3,3,3,3,3,3,1,3,3,2,3,3,3,3,3,3],
    [3,3,3,3,3,3,2,3,3,1,3,4,4,4,4,4,4,3,1,3,3,2,3,3,3,3,3,3],
    [1,1,1,1,1,1,2,1,1,1,3,4,4,4,4,4,4,3,1,1,1,2,1,1,1,1,1,1], # Middle Lane Row: 14
    [3,3,3,3,3,3,2,3,3,1,3,4,4,4,4,4,4,3,1,3,3,2,3,3,3,3,3,3],
    [3,3,3,3,3,3,2,3,3,1,3,3,3,3,3,3,3,3,1,3,3,2,3,3,3,3,3,3],
    [3,3,3,3,3,3,2,3,3,1,1,1,1,1,1,1,1,1,1,3,3,2,3,3,3,3,3,3],
    [3,3,3,3,3,3,2,3,3,1,3,3,3,3,3,3,3,3,1,3,3,2,3,3,3,3,3,3],
    [3,3,3,3,3,3,2,3,3,1,3,3,3,3,3,3,3,3,1,3,3,2,3,3,3,3,3,3],
    [3,2,2,2,2,2,2,2,2,2,2,2,2,3,3,2,2,2,2,2,2,2,2,2,2,2,2,3],
    [3,2,3,3,3,3,2,3,3,3,3,3,2,3,3,2,3,3,3,3,3,2,3,3,3,3,2,3],
    [3,2,3,3,3,3,2,3,3,3,3,3,2,3,3,2,3,3,3,3,3,2,3,3,3,3,2,3],
    [3,6,2,2,3,3,2,2,2,2,2,2,2,2,1,2,2,2,2,2,2,2,3,3,2,2,6,3],
    [3,3,3,2,3,3,2,3,3,2,3,3,3,3,3,3,3,3,2,3,3,2,3,3,2,3,3,3],
    [3,3,3,2,3,3,2,3,3,2,3,3,3,3,3,3,3,3,2,3,3,2,3,3,2,3,3,3],
    [3,2,2,2,2,2,2,3,3,2,2,2,2,3,3,2,2,2,2,3,3,2,2,2,2,2,2,3],
    [3,2,3,3,3,3,3,3,3,3,3,3,2,3,3,2,3,3,3,3,3,3,3,3,3,3,2,3],
    [3,2,3,3,3,3,3,3,3,3,3,3,2,3,3,2,3,3,3,3,3,3,3,3,3,3,2,3],
    [3,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,3],
    [3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3],
    [3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3],
    [3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3]
]

start = (26, 14)
goal = (5, 26)

uno = Astar(start, goal, grid)
path, dirs = uno.a_star()
print(path)
print(dirs)
