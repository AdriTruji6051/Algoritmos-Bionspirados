from antColony import AntColony, Graph_Configuration
import networkx as nx
        
def createGraph():
    G = nx.Graph()
    G.add_weighted_edges_from([
        ["A","B", 0.5], 
        ["B","C", 0.18],
        ["C","D", 0.67],
        ["D","F", 0.4],
        ["A","F", 0.7],
        ["F","H", 0.21],
        ["H","J", 0.023],
        ["H","K", 0.94],
        ["K","L", 0.025],
        ["D","J", 0.09]
    ])

    return G
        
if __name__ == "__main__":
    max_it_num = 500
    iteration = 1
    num_of_ants = 10
    
    graph = createGraph() 
    graph_configuration = Graph_Configuration()
    ant_colony = AntColony(num_of_ants, graph, graph_configuration)
    while(max_it_num >= iteration and ant_colony.graph_configuration.food_in_objective > 0):
        ant_colony.move_Ants()
        if iteration % 10 == 0:
            ant_colony.showStadisctics(iteration)
        iteration += 1
        
    ant_colony.showStadisctics(iteration)
    ant_colony.showAntsPaths()