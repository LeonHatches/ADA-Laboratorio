from mapa import get_graph, get_posiciones
from graph import GraphLinkDirected, GraphLink
from algorithms import dijkstra, grafo_dijkstra, backpack
from objects import Pedido, get_pedidos
from graficador import draw_graph

def nearest_neighbor(grafo, start, zonas : list[str]):
    recorrido = [start]
    actual = start

    while zonas:
        dist, prev = dijkstra(grafo, actual)
        min_zona = zonas[0]
        min_dist = dist[min_zona]

        for zona in zonas:
            if dist[zona] < min_dist:
                min_dist = dist[zona]
                min_zona = zona

        recorrido.append(min_zona)
        actual = min_zona
        zonas.remove(min_zona)

    return recorrido

def reconstruir_camino(prev, destino):
    camino = []
    actual = destino
    while actual is not None:
        camino.append(actual)
        actual = prev[actual]
    camino.reverse()
    return camino

def ruta_completa(grafo, recorrido):
    ruta_final = []

    for i in range(len(recorrido) - 1):
        origen = recorrido[i]
        destino = recorrido[i+1]

        dist, prev = dijkstra(grafo, origen)
        camino = reconstruir_camino(prev, destino)

        # Evitar repetir el nodo inicial
        if ruta_final and camino[0] == ruta_final[-1]:
            ruta_final.extend(camino[1:])
        else:
            ruta_final.extend(camino)

    return ruta_final

def reconstruir_grafo_recorrido(grafo : GraphLink, ruta):
    for i in range(len(ruta) - 1):
        grafo.insert_edge(ruta[i], ruta[i+1], 0)

    return grafo


print("-----------------------------")
print("- Eligiendo carga de camión -")
print("-----------------------------")

pedidos : list[Pedido] = get_pedidos()
camion_capacidad = 300
punto_inicial = "Fabrica_ParqueIndustrial"
grafo = get_graph()

valor_max, seleccion = backpack(pedidos, camion_capacidad)

print(f"Máximo Valor: {valor_max}")
print("Pedidos seleccionados")

for i in seleccion:
    print(pedidos[i])

print("\nZonas a las que hay que ir")

zonas = []

for i in seleccion:
    zonas.append(pedidos[i].destino)

print(zonas)

print("\nRecorrido con Nearest Neighbor")
recorrido = nearest_neighbor(grafo, punto_inicial, zonas)
print(recorrido)
ruta = ruta_completa(grafo, recorrido)
print(ruta)

grafo_final = get_graph()
for v in grafo_final.vertices:
    v.adj_list = []

grafo_final = reconstruir_grafo_recorrido(grafo_final, ruta)
draw_graph(grafo_final, get_posiciones())