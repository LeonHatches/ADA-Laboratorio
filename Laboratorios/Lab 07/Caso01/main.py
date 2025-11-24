from ordenar_pacientes import merge_sort_pacientes
from asignacion import mochila_pacientes
from rutas_dijkstra import dijkstra, grafo_hospital

pacientes = [
    {"nombre": "Juan", "gravedad": 8, "tiempo": 3},
    {"nombre": "Jose", "gravedad": 4, "tiempo": 2},
    {"nombre": "Carl", "gravedad": 10, "tiempo": 4},
    {"nombre": "Aron", "gravedad": 2, "tiempo": 1},
    {"nombre": "Mark", "gravedad": 5, "tiempo": 5}
]

# Utilizar divide y venceras para ordenar pacientes
ordenados = merge_sort_pacientes(pacientes)
print("Pacientes en orden de gravedad: ", ordenados)

# tiempo maximo disponible (horas)
tiempo_max = 6

# Problema de la mochila 1/0
seleccion, gravedad_total = mochila_pacientes(ordenados, tiempo_max)
print("\nPacientes seleccionados:", seleccion)
print("Gravedad total:", gravedad_total)

# Dijkstra
ruta, costo = dijkstra(grafo_hospital, "Cama1", "Quirófano")
print("\nRuta óptima:", ruta, "Costo:", costo)