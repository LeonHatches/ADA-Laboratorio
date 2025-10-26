import networkx as nx
import matplotlib.pyplot as plt
import random, sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.graph import GraphLink
from utils.mapa import get_graph, get_posiciones


def graficar_grafo(grafo : GraphLink, posiciones=None, mapa=True):
    
    G = nx.Graph()

    # GRAFO RECIBIDO
    for vertex in grafo.vertices:
        G.add_node(vertex.data)
    
    for vertex in grafo.vertices:
        for edge in vertex.adj_list:
            if not G.has_edge(vertex.data, edge.dest.data):
                G.add_edge(vertex.data, edge.dest.data, weight=edge.weight)
    
    if posiciones == None:
        posiciones = nx.spring_layout(G)

    plt.figure(figsize=(8, 12))
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True)
    plt.xlim(-82, -68)
    plt.ylim(-19, 0)
    plt.axis("equal")

    # MAPA BASE
    if mapa:
        mapa_grafo = get_graph()

        for vertices in mapa_grafo.vertices:
            G.add_node(vertices.data)

        for vertex in mapa_grafo.vertices:
            for edge in vertex.adj_list:
                if not G.has_edge(vertex.data, edge.dest.data):
                    G.add_edge(vertex.data, edge.dest.data, weight=edge.weight)
        
        mapa_pos = get_posiciones()
        nx.draw_networkx_edges(G, mapa_pos, edge_color='black', width=1.5)

    plt.axis('off')
    plt.show()


if __name__ == "__main__":
    g = GraphLink()

    graficar_grafo(g)

