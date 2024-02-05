import random
import math

def fitnessFunction(x):
    return x**2

def generate_neighbor(actual, change_factor):
    return actual + random.uniform(-change_factor, change_factor)

def simulatedAneanling():
    actual_temperature = 100.0
    min_temperature = 1.0
    cooling = 0.9
    iterat_for_temp = 10
    actual_solution = 5
    change_factor = 1
    
    while(actual_temperature > min_temperature):
        for _ in range(iterat_for_temp):
            neighbor = generate_neighbor(actual_solution, change_factor)
            
            actual_cost = fitnessFunction(actual_solution)
            neighbor_cost = fitnessFunction(neighbor)
            
            variation = neighbor_cost - actual_cost
            
            if variation < 0  or  random.random() < math.exp(-variation / actual_temperature ):
                actual_solution = neighbor
        
        actual_temperature *= cooling
    
    return actual_solution


if __name__ == '__main__':
    print('Algoritmo: Simulated aneanling :)')
    print(f"Solucion encontrada con valor: {simulatedAneanling()}")
    