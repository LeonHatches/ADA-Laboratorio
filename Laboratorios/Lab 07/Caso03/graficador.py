import networkx as nx
import matplotlib.pyplot as plt
from graph import GraphLink
from mapa import get_graph, get_posiciones


def graficar_grafo(grafo : GraphLink, posiciones=None, mapa=True, ruta=None):
    
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
    plt.xlim(-82, -68)
    plt.ylim(-19, 0)
    plt.axis("equal")

    # MAPA BASE
    if mapa:
        mapa_grafo = get_graph()
        G_mapa = nx.Graph()

        for v in mapa_grafo.vertices:
            for e in v.adj_list:
                if not G_mapa.has_edge(v.data, e.dest.data):
                    G_mapa.add_edge(v.data, e.dest.data)

        mapa_pos = get_posiciones()
        nx.draw_networkx_edges(G_mapa, mapa_pos, edge_color='black', width=1)

    # VÉRTICES DEL GRAFO
    nx.draw_networkx_nodes(
        G,
        posiciones,
        node_color='red',
        node_size=100
    )

    # ARISTAS DEL GRAFO
    nx.draw_networkx_edges(
        G,
        posiciones,
        edge_color='blue',
        style='dashed',
        width=2
    )

    # ETIQUETAS DEL GRAFO
    etiquetas = {n: n for n in G.nodes()}
    nx.draw_networkx_labels(
        G,
        posiciones,
        labels=etiquetas,
        font_size=8,
        font_color='black',
        verticalalignment='bottom'
    )
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(
        G,
        posiciones,
        edge_labels=edge_labels,
        font_color='blue',
        font_size=7
    )

    plt.title(f"Rutas aéreas del Perú {'desde ' + ruta if ruta else ''} (en KM)",
              fontsize=14, fontweight='bold', color='darkblue', pad=20)
    plt.axis('off')
    plt.show()

if __name__ == "__main__":
    g = GraphLink()

    graficar_grafo(g)

