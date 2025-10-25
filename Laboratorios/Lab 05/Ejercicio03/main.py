import sys
import os
sys.path.append(os.path.abspath('..'))

from utils.graph import GraphLinkDirected
from utils.bellman_ford import bellman_ford

def getGraph(): 
    graph = GraphLinkDirected()

    graph.insert_vertex("A")
    graph.insert_vertex("B")
    graph.insert_vertex("C")
    graph.insert_vertex("D")
    graph.insert_vertex("E")

    graph.insert_edge("A", "B", 4)
    graph.insert_edge("A", "C", 2)
    graph.insert_edge("B", "C", -1)
    graph.insert_edge("B", "D", 2)
    graph.insert_edge("C", "E", -3)
    graph.insert_edge("E", "D", -2)
    graph.insert_edge("D", "B", 3)
    
    return graph

if __name__ == "__main__":
    grafo = getGraph()

    print("Grafo Original")
    grafo.print_graph()

    print("\nCalculando ruta más corta desde A")
    distances = bellman_ford(grafo, "A")

    if (distances):
        for vertex, dist in distances.items():
            print(f"{vertex}: {dist}")


