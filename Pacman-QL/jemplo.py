class Node:
    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position
        self.g = 0  # Costo acumulado desde el nodo inicial
        self.h = 0  # Heurística (distancia Manhattan al nodo objetivo)
        self.f = 0  # Costo total: g + h


# Ejemplo de mapa
def astar(grid, start, goal):
    # Inicializar nodos inicial y objetivo
    start_node = Node(None, start)
    start_node.g = start_node.h = start_node.f = 0
    goal_node = Node(None, goal)
    goal_node.g = goal_node.h = goal_node.f = 0

    # Inicializar listas abierta y cerrada
    open_list = []
    closed_list = []

    # Agregar nodo inicial a la lista abierta
    open_list.append(start_node)

    # Iterar hasta encontrar el objetivo
    while len(open_list) > 0:
        # Obtener el nodo actual
        current_node = open_list[0]
        current_index = 0
        for index, item in enumerate(open_list):
            if item.f < current_node.f:
                current_node = item
                current_index = index

        # Sacar el nodo actual de la lista abierta y agregarlo a la lista cerrada
        open_list.pop(current_index)
        closed_list.append(current_node)

        # Verificar si se llegó al objetivo
        if current_node.position == goal_node.position:
            path = []
            current = current_node
            while current is not None:
                path.append(current.position)
                current = current.parent
            return path[::-1]  # Devolver el camino invertido

        # Generar nodos vecinos
        neighbors = []
        for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0)]:  # Movimientos arriba, abajo, izquierda, derecha
            node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])

            # Verificar que el nodo esté dentro de los límites del mapa
            if node_position[0] > (len(grid) - 1) or node_position[0] < 0 or node_position[1] > (len(grid[len(grid) - 1]) - 1) or node_position[1] < 0:
                continue

            # Verificar que el nodo no sea un obstáculo
            if grid[node_position[0]][node_position[1]] == 1:
                continue

            # Crear un nuevo nodo
            new_node = Node(current_node, node_position)

            # Agregar el nuevo nodo a la lista de vecinos
            neighbors.append(new_node)

        # Procesar vecinos
        for neighbor in neighbors:
            # Verificar que el vecino no esté en la lista cerrada
            if neighbor in closed_list:
                continue

            # Calcular los costos g, h, y f
            neighbor.g = current_node.g + 1  # Costo de movimiento a un vecino adyacente
            neighbor.h = abs(neighbor.position[0] - goal_node.position[0]) + abs(neighbor.position[1] - goal_node.position[1])
            neighbor.f = neighbor.g + neighbor.h

            # Verificar si el vecino ya está en la lista abierta
            if neighbor in open_list:
                # Verificar si este nuevo camino es mejor que el anterior
                if neighbor.g > current_node.g:
                    continue

            # Agregar el vecino a la lista abierta
            open_list.append(neighbor)

    # Si no se encuentra un camino
    return None


grid = [[0, 0, 0, 0, 0],
        [0, 1, 1, 1, 1],
        [0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 0, 0]]

start = (0, 4)
goal = (4, 0)

path = astar(grid, start, goal)
print(path)