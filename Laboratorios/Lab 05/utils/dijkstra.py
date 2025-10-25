from .graph import GraphLink, Vertex, Edge
import heapq

def dijkstra(grafo : GraphLink, inicio):
    initial_vertex : Vertex = grafo.search_vertex(inicio)

    if not initial_vertex:
        return {}

    dist = {v.data : float('inf') for v in grafo.vertices}
    dist[inicio] = 0

    pq = [(0, initial_vertex)]

    actual_dist : float
    actual_vertex : Vertex

    while pq:
        actual_dist, actual_vertex = heapq.heappop(pq)

        if actual_dist > dist[actual_vertex.data]:
            continue

        for edge in actual_vertex.adj_list:
            vecino = edge.dest
            peso = edge.weight
            new_dist = actual_dist + peso

            if new_dist < dist[vecino.data]:
                dist[vecino.data] = new_dist
                heapq.heappush(pq, (new_dist, vecino))

    return dist

if __name__ == "__main__":
    grafo = GraphLink()
    grafo.insert_vertex("A")
    grafo.insert_vertex("B")
    grafo.insert_vertex("C")
    grafo.insert_vertex("D")
    grafo.insert_vertex("E")

    grafo.insert_edge("A", "B", 4)
    grafo.insert_edge("A", "C", 2)
    grafo.insert_edge("B", "C", 1)
    grafo.insert_edge("B", "D", 5)
    grafo.insert_edge("C", "D", 8)
    grafo.insert_edge("C", "E", 10)
    grafo.insert_edge("D", "E", 2)

    print("Grafo:")
    grafo.print_graph()

    distancias = dijkstra(grafo, "B")

    print("\nPesos más cortos utilizando Dijkstra")
    for nodo, dist in distancias.items():
        print(f"{nodo}: {dist}")

    print("\nNuevo grafo creado con con caminos más cortos desde B")