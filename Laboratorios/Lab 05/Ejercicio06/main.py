from graficador import graficar_grafo

import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.dijkstra import dijkstra, grafo_dijkstra
from utils.mapa import get_graph_airports_and_edges, get_pos_airports

grafo_inicial   = get_graph_airports_and_edges()
pos_aeropuertos = get_pos_airports()
graficar_grafo(grafo_inicial, pos_aeropuertos, True)

CIUDAD = "Arequipa"

dist, prev = dijkstra(grafo_inicial, CIUDAD)
grafo_rutas = grafo_dijkstra(grafo_inicial, dist, prev)
graficar_grafo(grafo_rutas, pos_aeropuertos, True, CIUDAD)