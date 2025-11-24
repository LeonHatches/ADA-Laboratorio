from mapa import get_graph, get_posiciones
from graph import GraphLinkDirected, GraphLink
from algorithms import dijkstra, grafo_dijkstra, backpack, reconstruir_camino, ruta_completa, nearest_neighbor, reconstruir_grafo_recorrido
from objects import Pedido, get_pedidos_1, get_pedidos_2, get_pedidos_3
from graficador import draw_graph


print("-----------------------------")
print("- Eligiendo carga de camión -")
print("-----------------------------")

camion_capacidad = 400
punto_inicial = "Fabrica_ParqueIndustrial"
grafo = get_graph()
posiciones = get_posiciones()

draw_graph(grafo, posiciones)

# pedidos : list[Pedido] = get_pedidos_1()
# pedidos : list[Pedido] = get_pedidos_2()
pedidos : list[Pedido] = get_pedidos_3()

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
draw_graph(grafo_final, posiciones)