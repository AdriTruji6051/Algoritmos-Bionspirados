import random

class Graph_Configuration:
    def __init__(self):
        self.start_node = "A"
        self.objective_node = "L"
        self.food_in_objective = 100000000
        self.pheromones = 10
        self.evaporation_rate = 1
        self.pheromonesEdgesMap = {}
        self.imp_Pheromones = 0.5
        self.imp_Node_Vis = 0.2
        
class Ant:
    def __init__(self, startGraph, id):
        self.path = [startGraph]
        self.visited_path = {startGraph}
        self.id = id
    
class AntColony:
    def __init__(self, num_of_ants, graph, graph_configuration):
        self.global_best = 0
        self.best_path = []
        self.ants = []
        self.graph = graph
        self.graph_configuration = graph_configuration

        #Creando nuestras hormigas
        for h in range(num_of_ants):
            self.ants.append(Ant(graph_configuration.start_node, h))
            
#HELP FUNCTIONS TO WORK WITH NETWORKX LIB
    def getPossibleNodes(self, node):
        nexts_nodes = list(self.graph.edges(node, data=True))
        possible_nodes = []

        for n in range(len(nexts_nodes)):
                possible_nodes.append(nexts_nodes[n][1])
        return possible_nodes
    
    def getPossibleNodesExclPrev(self, node, prev_node):
        nexts_nodes = list(self.graph.edges(node, data=True))
        possible_nodes = []

        for n in range(len(nexts_nodes)):
            if nexts_nodes[n][1] != prev_node:
                possible_nodes.append(nexts_nodes[n][1])
        return possible_nodes   
    
    def getEdgePheromones(self, ori_node, dest_node):
        key = ori_node, dest_node
        if key in self.graph_configuration.pheromonesEdgesMap: return self.graph_configuration.pheromonesEdgesMap.get(key)
        else: return self.graph_configuration.pheromones * 0.10
    
    def setEdgePheromones(self, ori_node, dest_node, new_Pherom):
        key = ori_node, dest_node
        if key in self.graph_configuration.pheromonesEdgesMap: self.graph_configuration.pheromonesEdgesMap[key] = new_Pherom
        else:  self.graph_configuration.pheromonesEdgesMap.update({key: new_Pherom})
    
    def addEdgePheromones(self, ori_node, dest_node, new_Pherom):
        key = ori_node, dest_node
        if key in self.graph_configuration.pheromonesEdgesMap: self.graph_configuration.pheromonesEdgesMap[key] += new_Pherom
        else:  self.graph_configuration.pheromonesEdgesMap.update({key: new_Pherom})

            
#MATH FUCNTIONS TO OUR COLONY    
    def selectNode(self,nodes_probability):
        totalSum = 0
        probabilitys = []
        actualProb = 0
        
        for nodeDistance in nodes_probability:
            totalSum += nodeDistance[1]

        for node in nodes_probability:
            try:
                actualProb += ( (node[1] * 100) / totalSum) / 100
            except:
                actualProb += 0
            nodeProb = node[0], actualProb
            probabilitys.append(nodeProb)
            
        spinNode = random.random()
        
        for prob in probabilitys:
            if(prob[1] >= spinNode):
                return prob[0]
    
    def calcProbNode(self, ant):
        if len(ant.path) > 1:
            possible_nodes = self.getPossibleNodesExclPrev(ant.path[-1], ant.path[-2])
        else: possible_nodes = self.getPossibleNodes(ant.path[-1])
        
        nodes_probability = []
        
        for node in possible_nodes:
            Tij = self.getEdgePheromones(ant.path[-1], node) / self.graph.edges[ant.path[-1],node]['weight']
            Nij = 1 / self.graph.edges[ant.path[-1],node]['weight']
            ij = ( (Tij ** self.graph_configuration.imp_Pheromones) * (Nij ** self.graph_configuration.imp_Node_Vis) )
            ik = 1
            
            for knode in possible_nodes:   
                if knode != node: 
                    Nik = (1 / self.graph.edges[ant.path[-1],knode]['weight']) * self.graph_configuration.pheromones
                    Tik = (self.getEdgePheromones(ant.path[-1], knode) / self.graph.edges[ant.path[-1],knode]['weight']) * self.graph_configuration.pheromones
                    Ni = len(possible_nodes)
                    ik +=  ( Ni * ( Tik ** self.graph_configuration.imp_Pheromones) * (Nik ** self.graph_configuration.imp_Node_Vis))

            #Bajamos la probabilidad de ir al nodo si ya lo visito
            visited = ant.path.count(node)
            if visited == 0: visited = 1
            nodes_probability.append([node, ((ij / ik) * 10) / visited])    
            
        return self.selectNode(nodes_probability)
    
    def calcPheromones(self, ant):
        distance = 0
        for n in range(len(ant.path) - 1):
            distance += self.graph.edges[ant.path[n],ant.path[n+1]]['weight']

        pherom = (1/distance) * self.graph_configuration.pheromones
        
        #Guardamos el mejor resultado
        if pherom > self.global_best:
            self.best_path = ant.path
            self.global_best = pherom
        
        return pherom

#MAIN HELP FUNCTIONS  
    def goToFitnessNode(self, ant):
        next_node = self.calcProbNode(ant)
        if next_node != None:
            ant.path.append(next_node)
    
    def putPheromonesInEdges(self, ant):
        pherom = self.calcPheromones(ant)
        self.graph_configuration.food_in_objective -= 1
        visited_edges = {}
        
        for n in range(len(ant.path) - 1):
            infoEdge = ant.path[n], ant.path[n+1]
            if infoEdge in visited_edges != True:
                self.addEdgePheromones(ant.path[n], ant.path[n+1], pherom)

        ant.path = []
        ant.path.append(self.graph_configuration.start_node)
        
    def evaporatePheromones(self):
        for data in self.graph_configuration.pheromonesEdgesMap.items():
            evaporate_pherom = (1 * self.graph_configuration.evaporation_rate) * data[1]
            self.setEdgePheromones(data[0][0], data[0][1], evaporate_pherom)
           
#OFICIAL MAIN FUNCTIONS   
    def goToNextNode(self, ant):
        if(ant.path[-1] == self.graph_configuration.objective_node):
            self.putPheromonesInEdges(ant)
        else:
            self.goToFitnessNode(ant)
    
    def move_Ants(self):   
        for ant in self.ants:
            if self.graph_configuration.food_in_objective <= 0: break
            self.goToNextNode(ant)
            self.evaporatePheromones()
            
    def showStadisctics(self, iteration):
        distance = 0
        for n in range(len(self.best_path) - 1):
            distance += self.graph.edges[self.best_path[n], self.best_path[n+1]]['weight']
        print(f"\n---Estadiscticas de la ITERACION '{iteration}'\nMejor recorrido: {self.best_path} \nDistancia a objetivo: {distance}\nComida restante: {self.graph_configuration.food_in_objective}\n----------------------------------------------------------------------------------------------------------\n")

    def showAntsPaths(self):
        for ant in self.ants:
            print(f"Ant {ant.id}: {ant.path}")