from .graph import GraphLink, Vertex, Edge

def bellman_ford(grafo : GraphLink, inicio):
    initial_vertex : Vertex = grafo.search_vertex(inicio)

    if not initial_vertex:
        return {}

    dist = {v.data : float('inf') for v in grafo.vertices}
    dist[inicio] = 0

    for i in range(len(grafo.vertices) - 1):
        for vertex in grafo.vertices:
            for edge in vertex.adj_list:
                dest = edge.dest
                peso = edge.weight

                if dist[vertex.data] + peso < dist[dest.data]:
                    dist[dest.data] = dist[vertex.data] + peso

    for vertex in grafo.vertices:
        for edge in vertex.adj_list:
            dest = edge.dest
            peso = edge.weight

            if dist[vertex.data] + peso < dist[dest.data]:
                print("El grafo contiene un ciclo negativo")
                return None

    return dist


if __name__ == "__main__":
    grafo = GraphLink()

    for name in ["A", "B", "C", "D"]:
        grafo.insert_vertex(name)

    grafo.insert_edge("A", "B", 4)
    grafo.insert_edge("A", "C", 2)
    grafo.insert_edge("C", "B", 1)
    grafo.insert_edge("B", "D", 2)
    grafo.insert_edge("C", "D", 3)

    distancias = bellman_ford(grafo, "A")

    if distancias:
        print("\nDistancias más cortas desde A:")
        for vertice, distancia in distancias.items():
            print(f"{vertice}: {distancia}")

