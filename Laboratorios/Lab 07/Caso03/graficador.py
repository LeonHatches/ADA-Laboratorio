from mapa import get_graph, get_posiciones
from graph import GraphLink
import networkx as nx
import matplotlib.pyplot as plt

def draw_graph(grafo, pos): 
    G = nx.Graph()

    for v in grafo.vertices:
        G.add_node(v.data)

    for v in grafo.vertices:
        for e in v.adj_list:
            G.add_edge(v.data, e.dest.data, weight=e.weight)

    nx.draw_networkx_nodes(
        G, pos,
        node_size=650,
        node_color="#4285F4",
        edgecolors="white",
        linewidths=2
    )

    nx.draw_networkx_edges(
        G, pos,
        width=2,
        edge_color="#70757a"
    )

    nx.draw_networkx_labels(
        G, pos,
        font_size=9,
        font_color="black",
        font_family="sans-serif",
        verticalalignment="center",
        horizontalalignment="left" 
    )

    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(
        G, pos,
        edge_labels=labels,
        font_size=8,
        font_color="#5f6368"
    )

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    grafo = get_graph()
    posiciones = get_posiciones()

    draw_graph(grafo, posiciones)