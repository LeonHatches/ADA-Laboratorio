import networkx as nx
import matplotlib.pyplot as plt
import random, sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.graph import GraphLink

def graficar_grafo(grafo : GraphLink, posiciones=None):
    G = nx.Graph()

    for vertices in grafo.vertices:
        G.add_node(vertices.data)

    for vertex in grafo.vertices:
        for edge in vertex.adj_list:
            if not G.has_edge(vertex.data, edge.dest.data):
                G.add_edge(vertex.data, edge.dest.data, weight=edge.weight)

    if posiciones == None:
        posiciones = nx.spring_layout(G)

    node_colors = ['red' if node == 1 else 'lightblue' for node in G.nodes()]

    edge_colors = []
    for u, v in G.edges():
        w = G[u][v]['weight']
        if w == 0:
            edge_colors.append('red')
        else:
            edge_colors.append('black')



    plt.figure(figsize=(12, 12), dpi=2092//12)


    nx.draw_networkx_nodes(G, posiciones, node_color=node_colors, node_size=0)
    nx.draw_networkx_edges(G, posiciones, edge_color=edge_colors, width=2)
    nx.draw_networkx_labels(G, posiciones, font_size=12, font_color='black')

    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, posiciones, font_size=6, edge_labels=edge_labels)

    plt.axis('off')
    plt.show()


if __name__ == "__main__":
    g = GraphLink()

    for i in range(15):
        g.insert_vertex(chr(65 + i))

    for i in range(len(g.vertices)):
        for j in range(i + 1, len(g.vertices)):
            peso = random.randint(1, 10)
            g.insert_edge(g.vertices[i].data, g.vertices[j].data, peso)

    g.print_graph()

    graficar_grafo(g)
