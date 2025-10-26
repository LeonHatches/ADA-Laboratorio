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

    