from graph import GraphLink, Vertex
import heapq

# Algoritmo Dijkstra - Programación voraz
def dijkstra(grafo: GraphLink, inicio):
    initial_vertex: Vertex = grafo.search_vertex(inicio)
    if not initial_vertex:
        return {}, {}

    dist = {v.data: float('inf') for v in grafo.vertices}
    prev = {v.data: None for v in grafo.vertices}
    dist[inicio] = 0

    pq = [(0, initial_vertex)]

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
                prev[vecino.data] = actual_vertex.data
                heapq.heappush(pq, (new_dist, vecino))

    return dist, prev


# Algoritmo para transformar resultado de Dijkstra
def grafo_dijkstra(grafo: GraphLink, dist, prev):
    nuevo_grafo = GraphLink()

    for v in grafo.vertices:
        nuevo_grafo.insert_vertex(v.data)

    for nodo, padre in prev.items():
        if padre is not None:
            peso = None
            v_padre = grafo.search_vertex(padre)
            for edge in v_padre.adj_list:
                if edge.dest.data == nodo:
                    peso = edge.weight
                    break
            if peso is not None:
                nuevo_grafo.insert_edge(padre, nodo, peso)

    return nuevo_grafo

# Algoritmo de la mochila - Programación Dinámica
def backpack(peso, valor, W):
    n = len(peso)
    
    dp = [[0] * (W + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for j in range(W + 1):
            if peso[i - 1] <= j:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - peso[i - 1]] + valor[i - 1])
            else:
                dp[i][j] = dp[i - 1][j]
    
    objetos = []
    j = W
    for i in range(n, 0, -1):
        if dp[i][j] != dp[i - 1][j]:
            objetos.append(i - 1)
            j -= peso[i - 1]
    
    objetos.reverse()
    return dp[n][W], objetos
