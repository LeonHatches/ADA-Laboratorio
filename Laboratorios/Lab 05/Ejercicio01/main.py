import sys
import os
sys.path.append(os.path.abspath('..'))

from utils.graph import GraphLink, Vertex, Edge
from utils.dijkstra import dijkstra
import random

def getGraph():
    graph = GraphLink()

    graph.insert_vertex("A")
    graph.insert_vertex("B")
    graph.insert_vertex("C")
    graph.insert_vertex("D")
    graph.insert_vertex("E")
    graph.insert_vertex("F")
    graph.insert_vertex("G")
    graph.insert_vertex("H")

    graph.insert_edge("A", "B", random.randint(1, 10))
    graph.insert_edge("A", "C", random.randint(1, 10))
    graph.insert_edge("A", "D", random.randint(1, 10))
    graph.insert_edge("B", "E", random.randint(1, 10))
    graph.insert_edge("B", "F", random.randint(1, 10))
    graph.insert_edge("C", "G", random.randint(1, 10))
    graph.insert_edge("C", "H", random.randint(1, 10))
    graph.insert_edge("D", "E", random.randint(1, 10))
    graph.insert_edge("D", "G", random.randint(1, 10))
    graph.insert_edge("E", "F", random.randint(1, 10))
    graph.insert_edge("E", "H", random.randint(1, 10))
    graph.insert_edge("F", "G", random.randint(1, 10))
    graph.insert_edge("F", "A", random.randint(1, 10))
    graph.insert_edge("G", "H", random.randint(1, 10))
    graph.insert_edge("H", "B", random.randint(1, 10))

    return graph

if __name__ == "__main__":
    graph = getGraph()
    print("Grafo original")
    graph.print_graph()

    distancias = dijkstra(graph, "A")

    print("\nCaminos más cortos con Dijkstra:")
    for nodo, dist in distancias.items():
        print(f"{nodo}: {dist}")
