import matplotlib.pyplot as plt
import networkx as nx
from rutas_dijkstra import dijkstra, grafo_hospital
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

pos = {
    "Ambulancia": (0, 6),
    "Pasillo A": (0, 4),
    "Cama1": (-2, 2),
    "Pasillo C": (0, 2),
    "Cama3": (-1, 0),
    "Pasillo B": (2, 3),
    "Cama2": (4, 4),
    "Cama4": (4, 2),
    "Pasillo D": (3, 1),
    "Cama5": (5, 0),
    "Cama6": (4, -1),
    "Quirófano": (2, -1),
}

def mapa_hospital(asignacion_pacientes=None):
    G = nx.Graph()

    nodos = [
        "Ambulancia",
        "Pasillo A", "Pasillo B", "Pasillo C", "Pasillo D",
        "Cama1", "Cama2", "Cama3", "Cama4", "Cama5", "Cama6",
        "Quirófano"
    ]
    for n in nodos:
        G.add_node(n)

    conexiones = [
        ("Ambulancia", "Pasillo A", 10),
        ("Pasillo A", "Cama1", 5),
        ("Pasillo A", "Pasillo B", 7),
        ("Pasillo A", "Pasillo C", 6),
        ("Pasillo B", "Cama2", 6),
        ("Pasillo B", "Cama4", 4),
        ("Pasillo B", "Pasillo D", 8),
        ("Pasillo C", "Cama3", 5),
        ("Pasillo C", "Pasillo D", 7),
        ("Pasillo D", "Quirófano", 6),
        ("Pasillo D", "Cama5", 5),
        ("Pasillo D", "Cama6", 7),
    ]
    for a, b, w in conexiones:
        G.add_edge(a, b, weight=w)

    node_colors = []
    labels = {}

    for nodo in G.nodes():
        if "Cama" in nodo:
            paciente = asignacion_pacientes.get(nodo) if asignacion_pacientes else None
            if paciente:
                node_colors.append("red")
                labels[nodo] = f"{nodo}\n({paciente})"
            else:
                node_colors.append("green")
                labels[nodo] = f"{nodo}\n(libre)"
        elif nodo == "Quirófano":
            node_colors.append("orange")
            labels[nodo] = nodo
        elif nodo == "Ambulancia":
            node_colors.append("cyan")
            labels[nodo] = nodo
        else:
            node_colors.append("skyblue")
            labels[nodo] = nodo

    fig = plt.Figure(figsize=(10, 8))
    ax = fig.add_subplot(111)

    nx.draw_networkx_nodes(G, pos, node_color=node_colors, node_size=1500, ax=ax)
    nx.draw_networkx_labels(G, pos, labels=labels, font_size=9, ax=ax)
    nx.draw_networkx_edges(G, pos, width=2, ax=ax)
    nx.draw_networkx_edge_labels(
        G, pos,
        edge_labels=nx.get_edge_attributes(G, "weight"),
        ax=ax
    )

    ax.set_title("Mapa del Centro Médico")
    ax.axis("off")
    return fig


def mostrar_ruta(cama_destino):
    """Ruta desde Ambulancia hacia la cama seleccionada."""

    ruta, costo = dijkstra(grafo_hospital, "Ambulancia", cama_destino)

    G = nx.Graph()
    for nodo in grafo_hospital:
        for vecino, peso in grafo_hospital[nodo]:
            G.add_edge(nodo, vecino, weight=peso)

    pos = {
        "Ambulancia": (0, 6),
        "Pasillo A": (0, 4),
        "Cama1": (-2, 2),
        "Pasillo C": (0, 2),
        "Cama3": (-1, 0),
        "Pasillo B": (2, 3),
        "Cama2": (4, 4),
        "Cama4": (4, 2),
        "Pasillo D": (3, 1),
        "Cama5": (5, 0),
        "Cama6": (4, -1),
        "Quirófano": (2, -1),
    }

    ruta_edges = list(zip(ruta, ruta[1:]))

    fig = plt.Figure(figsize=(6, 5))
    ax = fig.add_subplot(111)

    nx.draw_networkx_nodes(G, pos, node_color="skyblue", node_size=1400, ax=ax)
    nx.draw_networkx_labels(G, pos, ax=ax)
    nx.draw_networkx_edges(G, pos, width=1.5, alpha=0.3, ax=ax)

    if ruta_edges:
        nx.draw_networkx_edges(
            G, pos,
            edgelist=ruta_edges,
            width=4,
            edge_color="red",
            ax=ax
        )

    nx.draw_networkx_edge_labels(
        G, pos,
        edge_labels=nx.get_edge_attributes(G, "weight"),
        ax=ax
    )

    ax.set_title(f"Ruta de Ambulancia → {cama_destino} (Costo {costo})")
    ax.axis("off")

    return fig


def embed_figure_in_window(fig, parent_window):

    for widget in parent_window.winfo_children():
        widget.destroy()

    canvas = FigureCanvasTkAgg(fig, master=parent_window)
    widget = canvas.get_tk_widget()

    widget.config(width=600, height=720)
    widget.pack_propagate(False)

    widget.pack(fill="none", expand=False)

    canvas.draw()

