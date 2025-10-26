from .graph import GraphLink

MOSTRAR_TABLA = True

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
    
    if (MOSTRAR_TABLA):
        mostrar_tabla(dist, index)
    
    return dist, index

def mostrar_tabla(dist, index):
    vertices = [''] * len(index)
    for vertice, i in index.items():
        vertices[i] = vertice

    ancho = 6

    print("      ", end="")
    for v in vertices:
        print(f"{v:>{ancho}}", end="")
    print()

    print("     " + "-" * ((ancho + 1) * len(vertices)))

    for i, origen in enumerate(vertices):
        print(f"{origen:>4} |", end="")
        for j in range(len(vertices)):
            valor = dist[i][j]
            if valor == float('inf'):
                print(f"{'∞':>{ancho}}", end="")
            else:
                print(f"{valor:>{ancho}}", end="")
        print()

if __name__ == "__main__":
    grafo = GraphLink()

    for name in ["A", "B", "C", "D"]:
        grafo.insert_vertex(name)

    grafo.insert_edge("A", "B", 4)
    grafo.insert_edge("A", "C", 2)
    grafo.insert_edge("C", "B", 1)
    grafo.insert_edge("B", "D", 2)
    grafo.insert_edge("C", "D", 3)

    floyd_warshall(grafo)