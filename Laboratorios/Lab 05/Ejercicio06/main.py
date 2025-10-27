from graficador import graficar_grafo
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.dijkstra import dijkstra, grafo_dijkstra
from utils.mapa import get_graph_airports_and_edges, get_pos_airports

grafo_inicial   = get_graph_airports_and_edges()
pos_aeropuertos = get_pos_airports()
graficar_grafo(grafo_inicial, pos_aeropuertos, True)

# PROGRAMA DE INGRESAR CIUDADd
ciudades = [v.data for v in grafo_inicial.vertices]

print("\nRUTA DE CIUDADES A TODO EL PERÚ\nCiudades disponibles:")
for i, ciudad in enumerate(ciudades, start=1):
    print(f"{i}. {ciudad}")

while True:
    try:
        opcion = int(input("\nSelecciona una ciudad de origen (número): "))
        if 1 <= opcion <= len(ciudades):
            CIUDAD = ciudades[opcion - 1]
            break
        else:
            print("Opción fuera de rango. Intenta de nuevo.")
    
    except ValueError:
        print("Ingresa un número válido.")


# Ejecutar Dijkstra y graficar rutas
dist, prev = dijkstra(grafo_inicial, CIUDAD)
grafo_rutas = grafo_dijkstra(grafo_inicial, dist, prev)
graficar_grafo(grafo_rutas, pos_aeropuertos, True, CIUDAD)