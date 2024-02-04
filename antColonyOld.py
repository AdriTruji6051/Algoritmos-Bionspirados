import networkx as nx
import random

class Ant:
    def __init__(self, startGraph, id):
        self.path = [startGraph]
        self.id = id
    
class Graph_Configuration:
    def __init__(self, start_node, objective_node, food_in_objective, pheromones, evaporation_rate, imp_Pheromones, imp_Node_Vis):
        self.start_node = start_node
        self.objective_node = objective_node
        self.food_in_objective = food_in_objective
        self.pheromones = pheromones
        self.evaporation_rate = evaporation_rate
        self.pheromonesEdgesMap = {}
        self.imp_Pheromones = imp_Pheromones
        self.imp_Node_Vis = imp_Node_Vis

class AntColony:
    def __init__(self, num_of_ants, graph, graph_configuration):
        self.global_best = 0
        self.ants = []
        self.graph = graph
        self.graph_configuration = graph_configuration

        #Creando nuestras hormigas
        for h in range(num_of_ants):
            self.ants.append(Ant(graph_configuration.start_node, h))

#Calculate the best next node 
    def fitnessNode(self, possible_nodes, ant):
        #return random.choice([n for n in possible_nodes if n not in ant.path])
        edgeCoord = []
        next_Node = None
        bestProbablity = []
        for n in range(len(possible_nodes)):
            keys = ant.path[-1], possible_nodes[n]
            edgeCoord.append(keys)
        
        for keys in edgeCoord:
            edgePheromones = self.graph_configuration.pheromonesEdgesMap.get(keys)
            if(edgePheromones != None):
                next_Node = edgePheromones

        return random.choice([n for n in possible_nodes if n not in ant.path])

            

    def fitnessPath(self, ant):
        self.graph_configuration.food_in_objective -= 1
        evaporation_rate = self.graph_configuration.evaporation_rate
        distance = 0

        for f in range(len(ant.path) - 1):
            key = ant.path[f], ant.path[f+1]
            try:
                graph_edges = self.graph.edges(ant.path[f], data=True)

                #Total de distancia
                for edge in graph_edges:
                    distance += edge[2]['weight']

                for edge in graph_edges:
                    if(edge[1] == key[1]):
                        #Calculamos cuantas pheromonas vamos a depositar en cada arco 
                        pheromonesInEdge = self.graph_configuration.pheromonesEdgesMap.get(key)
                        newPheromonesInEdge = (
                            (1-evaporation_rate) * (pheromonesInEdge + (1/distance))
                        )
                        
                        self.graph_configuration.pheromonesEdgesMap[key] = newPheromonesInEdge
                        break
                    #Hasta aqui llega
            except:
                pheromonesInEdge = (
                    (1-evaporation_rate) * (1/distance)
                )
                self.graph_configuration.pheromonesEdgesMap[key] = pheromonesInEdge

        #Devolvemos la hormiga al hormiguero
          
        ant.path = []
        ant.path.append(graph_configuration.start_node)
        
def createGraph():
    G = nx.Graph()
    G.add_weighted_edges_from([
        ["A","B", 0.5], 
        ["B","C", 0.18],
        ["C","D", 0.67],
        ["D","F", 0.4],
        ["A","F", 0.7]
    ])

    return G
        
if __name__ == "__main__":
    start_node = "A"
    objective_node = "F"
    food_in_objective = 5 #Numero de veces que las hormigas deben llegar a este nodo
    pheromones = 17
    imp_Pheromones = 0.5
    imp_Node_Vis = 0.5
    evaporation_rate = 0.1
    max_it_num = 100
    iteration = 1
    num_of_ants = 1
    graph = createGraph()
    graph_configuration = Graph_Configuration(start_node, objective_node, food_in_objective, 
                                              pheromones, evaporation_rate, imp_Pheromones, imp_Node_Vis)

    #Nuestro hormiguero y su grafo
    ant_colony = AntColony(num_of_ants, graph, graph_configuration)

    while(max_it_num >= iteration and ant_colony.graph_configuration.food_in_objective >= 1):
        print("Chambeando.....")
        for ant in ant_colony.ants:
            actual_node = ant.path[-1]
            nexts_nodes = list(ant_colony.graph.edges(actual_node, data=True))
            possible_nodes = []

            for n in range(len(nexts_nodes)):
                possible_nodes.append(nexts_nodes[n][1])

            ant.path.append(ant_colony.fitnessNode(possible_nodes, ant))

            if(ant.path[-1] == ant_colony.graph_configuration.objective_node):
                print('Food finded')
                ant_colony.fitnessPath(ant)
        
        iteration += 1

    print(ant_colony.graph_configuration.pheromonesEdgesMap)
        # print(graph_edges[1][2]['weight']) ---------- Pa sacar el peso
    