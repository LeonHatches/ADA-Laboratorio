import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import random, time
from utils.graph import GraphLink
from utils.bellman_ford import bellman_ford
from utils.dijkstra import dijkstra
from utils.floyd_warshall import floyd_warshall

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
    sizes = range(50, 501, 50)

    for i in range(len(sizes)):
        grafo = generar_grafo(sizes[i])

        print(f"--- Grafo con {sizes[i]} vertices ---")

        start = time.time()
        dijkstra(grafo, 0)
        end = time.time()
        print(f"Dijkstra       - Tiempo de ejecución = {end - start}")

        start = time.time()
        bellman_ford(grafo, 0)
        end = time.time()
        print(f"Bellman-Ford   - Tiempo de ejecución = {end - start}")

        start = time.time()
        floyd_warshall(grafo, False)
        end = time.time()
        print(f"Floyd-Warshall - Tiempo de ejecución = {end - start}")

        print()

