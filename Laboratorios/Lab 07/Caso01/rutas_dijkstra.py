import heapq

grafo_hospital = {
    "Ambulancia": [("Pasillo A", 6)],
    "Pasillo A": [("Ambulancia", 6), ("Cama1", 3), ("Cama2", 4), ("Quirófano", 5)],
    "Cama1": [("Pasillo A", 3)],
    "Cama2": [("Pasillo A", 4)],
    "Quirófano": [("Pasillo A", 5)]
}

def dijkstra(grafo, inicio, fin):
    dist = {nodo: float("inf") for nodo in grafo}
    dist[inicio] = 0
    prev = {nodo: None for nodo in grafo}

    pq = [(0, inicio)]

    while pq:
        costo, nodo = heapq.heappop(pq)

        if nodo == fin:
            break

        for vecino, peso in grafo[nodo]:
            nuevo = costo + peso
            if nuevo < dist[vecino]:
                dist[vecino] = nuevo
                prev[vecino] = nodo
                heapq.heappush(pq, (nuevo, vecino))

    ruta = []
    actual = fin

    while actual is not None:
        ruta.append(actual)
        actual = prev[actual]

    ruta.reverse()
    return ruta, dist[fin]

