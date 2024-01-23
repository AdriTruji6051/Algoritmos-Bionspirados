import random

class Poblacion:
    poblacion = []
    new_poblacion = []
    genMinRange = 0
    genMaxRange = 500
    factual = 1
    dnaSlots = 7
    mutation_rate = 20

def createDNA(poblacion):
    DNA = []
    for i in range(poblacion.dnaSlots):
        DNA.append(random.randint(poblacion.genMinRange, poblacion.genMaxRange))
    
    poblacion.poblacion.append(DNA)

def fitnessFunction(factual, gen):
    div = abs(sum(gen) - factual)
    if div != 0:
        calculated_factual = (1.0 / div) - 0.001
        return calculated_factual
    return 1

def mutation(gens, poblacion):
    if random.randint(0,100) < poblacion.mutation_rate:
        gens[random.randint(0, poblacion.dnaSlots - 1)] = random.randint(poblacion.genMinRange, poblacion.genMaxRange)
        return gens
    return gens

def genetichalAlgorithm(numOfPopulation, limite):

    muestra = Poblacion()
    halfPopulationCount = numOfPopulation // 2
    halfDNACount = muestra.dnaSlots // 2

    #Creamos nuestros DNA's
    for i in range(numOfPopulation):
        createDNA(muestra)

    print('Poblacion inicial: \n', muestra.poblacion, "\n")

    #Iteramos hasta encontrar nuestro mejor resultado
    for generation in range(limite):
        
        #Calculamos nuestras funciones objetivo
        for gens in muestra.poblacion:
            dnaAndFx = fitnessFunction(muestra.factual, gens), gens
            muestra.new_poblacion.append(dnaAndFx)

        muestra.new_poblacion = sorted(muestra.new_poblacion, key=lambda x: x[0], reverse=True)

        #Datos y condicionales de finalizacion
        if generation % 10 == 0:
            print(f'Generacion {generation}:    Mejor objetivo: %.3f' %muestra.new_poblacion[0][0] ,f'    DNA: {muestra.new_poblacion[0][1]}')
        
        if muestra.new_poblacion[0][0] >= 1:
            print(f"\nObjetivo encontrado en la generacion {generation}")
            break

        #Resetamos valores para trabajar con los hijos :)
        muestra.poblacion = []

        #Creamos a los hijos de los mejores padres :)
        for a in range(halfPopulationCount):
            father = muestra.new_poblacion[a][1]
            if(halfPopulationCount > 2):
                mother = muestra.new_poblacion[random.choice([i for i in range(0, halfPopulationCount) if i not in [a]])][1]
            else: mother = muestra.new_poblacion[a+1][1]

            #Primer hijo
            muestra.poblacion.append(mutation(father[:halfDNACount] + mother[halfDNACount:], muestra))

            #Segundo hijo            
            muestra.poblacion.append(mutation(mother[:halfDNACount] + father[halfDNACount:], muestra))

        #Evitando errores de index al imprimir :)
        if limite <= generation: muestra.new_poblacion = []
        limite += 1
        
    print('\n\nMejor resultado: ', muestra.new_poblacion[0])

if __name__ == '__main__':
    print('Algoritmo genetico :)')
    genetichalAlgorithm(13,1000)