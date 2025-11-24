import heapq

grafo_hospital = {
    "Ambulancia": [("Pasillo A", 10)],

    "Pasillo A": [
        ("Ambulancia", 10),
        ("Cama1", 5),
        ("Pasillo B", 7),
        ("Pasillo C", 6),
    ],

    "Pasillo B": [
        ("Pasillo A", 7),
        ("Cama2", 6),
        ("Cama4", 4),
        ("Pasillo D", 8),
    ],

    "Pasillo C": [
        ("Pasillo A", 6),
        ("Cama3", 5),
        ("Pasillo D", 7),
    ],

    "Pasillo D": [
        ("Pasillo B", 8),
        ("Pasillo C", 7),
        ("Quirófano", 6),
        ("Cama5", 5),
        ("Cama6", 7),
    ],

    "Cama1": [("Pasillo A", 5)],
    "Cama2": [("Pasillo B", 6)],
    "Cama3": [("Pasillo C", 5)],
    "Cama4": [("Pasillo B", 4)],
    "Cama5": [("Pasillo D", 5)],
    "Cama6": [("Pasillo D", 7)],

    "Quirófano": [("Pasillo D", 6)],
}


def dijkstra(grafo, inicio, fin):

    if inicio not in grafo or fin not in grafo:
        return [], float("inf")

    dist = {nodo: float("inf") for nodo in grafo}
    dist[inicio] = 0
    prev = {nodo: None for nodo in grafo}

    pq = [(0, inicio)]

    while pq:
        costo, nodo = heapq.heappop(pq)

        if nodo == fin:
            break

        if costo > dist[nodo]:
            continue

        for vecino, peso in grafo[nodo]:
            nuevo = costo + peso
            if nuevo < dist[vecino]:
                dist[vecino] = nuevo
                prev[vecino] = nodo
                heapq.heappush(pq, (nuevo, vecino))

    if dist[fin] == float("inf"):
        return [], float("inf")

    ruta = []
    actual = fin
    while actual is not None:
        ruta.append(actual)
        actual = prev[actual]

    ruta.reverse()
    return ruta, dist[fin]

