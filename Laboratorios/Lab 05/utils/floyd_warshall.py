from graph import GraphLink

def floyd_warshall (g: GraphLink):
    n = len(g.vertices)
    
    if n == 0:
        return []
    
    # INICIALIZAR PESOS Y DICCIONARIO
    index = {v.data: i for i, v in enumerate(g.vertices)}
    dist  = [[float('inf')] * n for _ in range(n)]

    # ESTABLECE DISTANCIAS DIRECTAS
    for i, v in enumerate(g.vertices):
        dist[i][i] = 0
        for edge in v.adj_list:
            j = index[edge.dest.data]
            dist[i][j] = edge.weight

    # FLOYD WARSHALL
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist [i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    
    return dist, index