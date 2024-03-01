import random

class anticuerpo:
    def __init__(self, mejoras):
        self.mejoras = mejoras
        self.objetivo = 0

def iniciar_poblacion(tam_poblacion, feature_size):
    return [anticuerpo([random.uniform(0, 1) for _ in range(feature_size)]) for _ in range(tam_poblacion)]

def calcular_objetivo(anticuerpo, objetivo):
    return sum((a - b) ** 2 for a, b in zip(anticuerpo.mejoras, objetivo))

def elegir_clones(poblacion, objetivo, clone_factor):
    clones = []
    for anticuerpo in poblacion:
        num_clones = int(clone_factor / (1 + anticuerpo.objetivo))
        clones.extend([anticuerpo] * num_clones)
    return clones

def mutate(anticuerpo, mutation_rate):
    return anticuerpo([feature + random.uniform(-mutation_rate, mutation_rate) for feature in anticuerpo.mejoras])

def main():
    objetivo_anticuerpo = anticuerpo([0.5, 0.3, 0.8]) 
    tam_poblacion = 50
    clone_factor = 5
    mutation_rate = 0.1
    generacions = 100

    poblacion = iniciar_poblacion(tam_poblacion, len(objetivo_anticuerpo.mejoras))

    for generacion in range(generacions):
        for anticuerpo in poblacion:
            anticuerpo.objetivo = calcular_objetivo(anticuerpo, objetivo_anticuerpo)

        poblacion.sort(key=lambda x: x.objetivo)

        clones = elegir_clones(poblacion, objetivo_anticuerpo, clone_factor)

        clones_mutados = [mutate(clone, mutation_rate) for clone in clones]

        for i in range(len(clones_mutados)):
            poblacion[i] = clones_mutados[i]

        mejor_anticuerpo = min(poblacion, key=lambda x: x.objetivo)
        print(f"generacion {generacion + 1}, mejor objetivo: {mejor_anticuerpo.objetivo}")

    print("Poblacion final:")
    for anticuerpo in poblacion:
        print(f"mejoras: {anticuerpo.mejoras}, objetivo: {anticuerpo.objetivo}")

if __name__ == "__main__":
    main()
