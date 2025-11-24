from graph import GraphLinkDirected, GraphLink
from algorithms import dijkstra, grafo_dijkstra, backpack

grafo = GraphLink()


print("----------------------")
print("- Hallar ruta mínima -")
print("----------------------")

puntos = ["Matarani", "Mollendo", "La Joya", "El Pedregal", "Arequipa (PI)", "Via P. Sur"]
for p in puntos:
    grafo.insert_vertex(p)

# Matarani -> Mollendo: 15 min
grafo.insert_edge("Matarani", "Mollendo", 15)
# Mollendo -> La Joya: 80 min
grafo.insert_edge("Mollendo", "La Joya", 80)
# La Joya -> Arequipa (Parque Industrial): 60 min (Ruta principal, tráfico moderado)
grafo.insert_edge("La Joya", "Arequipa (PI)", 60)
# La Joya -> El Pedregal: 45 min (Ruta alternativa, mayor distancia pero menos tráfico)
grafo.insert_edge("La Joya", "El Pedregal", 45) 
# El Pedregal -> Vía P. Sur: 30 min
grafo.insert_edge("El Pedregal", "Via P. Sur", 30)
# Vía P. Sur -> Arequipa (PI): 20 min
grafo.insert_edge("Via P. Sur", "Arequipa (PI)", 20)

inicio = "Matarani"
final = "Arequipa (PI)"

distancias, predecesores = dijkstra(grafo, inicio)

nuevo_grafo = grafo_dijkstra(grafo, distancias, predecesores)
nuevo_grafo.print_graph()

print("\n-----------------------------")
print("- Eligiendo carga de camión -")
print("-----------------------------")

pesos_contenedores = [4, 6, 2, 5, 8, 3]
valores_contenedores = [20, 30, 10, 25, 40, 15]
nombres_contenedores = ["Alimentos", "Electronicos", "Maquinaria", "Textiles", "Minerales", "Quimicos"]
capacidad_camion = 15

valor_maximo, objetos_indices = backpack(pesos_contenedores, valores_contenedores, 15)

print(f"Valor máximo = {valor_maximo}")

for i in objetos_indices:
    print(f"{nombres_contenedores[i]} = {valores_contenedores[i]}")