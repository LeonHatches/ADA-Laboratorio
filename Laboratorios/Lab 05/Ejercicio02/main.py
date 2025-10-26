import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils.graph import GraphLink
from utils.floyd_warshall import floyd_warshall
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

    graph.insert_edge_directed("A", "B", random.randint(1, 10))
    graph.insert_edge_directed("A", "C", random.randint(1, 10))
    graph.insert_edge_directed("A", "D", random.randint(1, 10))
    graph.insert_edge_directed("B", "E", random.randint(1, 10))
    graph.insert_edge_directed("B", "F", random.randint(1, 10))
    graph.insert_edge_directed("C", "G", random.randint(1, 10))
    graph.insert_edge_directed("C", "H", random.randint(1, 10))
    graph.insert_edge_directed("D", "E", random.randint(1, 10))
    graph.insert_edge_directed("D", "G", random.randint(1, 10))
    graph.insert_edge_directed("E", "F", random.randint(1, 10))
    graph.insert_edge_directed("E", "H", random.randint(1, 10))
    graph.insert_edge_directed("F", "G", random.randint(1, 10))
    graph.insert_edge_directed("F", "A", random.randint(1, 10))
    graph.insert_edge_directed("G", "H", random.randint(1, 10))
    graph.insert_edge_directed("H", "B", random.randint(1, 10))

    return graph

if __name__ == "__main__":
    graph = getGraph()
    print("\nGrafo original")
    graph.print_graph()

    print("\n\tTABLA DE PESOS EN PARES DE VÉRTICES (FLOYD-WARSHALL)")
    floyd_warshall(graph)