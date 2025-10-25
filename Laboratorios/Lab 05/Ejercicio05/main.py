import sys
import os
sys.path.append(os.path.abspath('..'))

import random, time
import matplotlib.pyplot as plt
from utils.graph import GraphLink
from utils.bellman_ford import bellman_ford
from utils.dijkstra import dijkstra

def generar_grafo(num_vertices):
    grafo = GraphLink()

    for i in range(num_vertices):
        grafo.insert_vertex(i)

    for u in range(1, num_vertices):
        v = random.randint(0, u - 1)
        peso = random.randint(1, 10)
        grafo.insert_edge(u, v, peso)

    aristas_extra = int(num_vertices * 0.5)
    aristas_extras = set()

    for _ in range(aristas_extra):
        u, v = random.sample(range(num_vertices), 2)
        if (u, v) in aristas_extras or (v, u) in aristas_extras:
            continue

        aristas_extras.add((u, v))
        peso = random.randint(1, 10)
        grafo.insert_edge(u, v, peso)

    return grafo

if __name__ == "__main__":
    sizes = range(100, 3001, 100)
    tiempos_dijkstra = []
    tiempos_bellman = []

    for n in sizes:
        grafo = generar_grafo(n)

        start = time.time()
        dijkstra(grafo, 0)
        end = time.time()

        tiempos_dijkstra.append(end - start)

        start = time.time()
        bellman_ford(grafo, 0)
        end = time.time()

        tiempos_bellman.append(end - start)

        print(f"{n} vértices -> Dijkstra: {tiempos_dijkstra[-1]:.6f}s | Bellman-Ford: {tiempos_bellman[-1]:.6f}s")

    # Graficar resultados
    plt.figure(figsize=(10, 6))
    plt.plot(list(sizes), tiempos_dijkstra, label="Dijkstra", marker='o')
    plt.plot(list(sizes), tiempos_bellman, label="Bellman-Ford", marker='s')
    plt.title("Comparación de tiempos de ejecución")
    plt.xlabel("Número de vértices")
    plt.ylabel("Tiempo (segundos)")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()