"""
Programa Principal - Comparación IG vs ILS
PERSONA 7: Implementa este archivo con la ejecución y comparación de ambos algoritmos
"""

import time
from common.problema import FlowShop
from ig.iterative_greedy import IterativeGreedy
from ils.iterated_local_search import IteratedLocalSearch
from common.busqueda_local import busqueda_local

def get_tiempos():
    tiempos = [
        [4, 7, 3],
        [2, 5, 1],
        [6, 3, 8],
        [5, 4, 5],
        [3, 6, 2],
        [7, 2, 6],
        [4, 8, 3],
        [9, 1, 4],
        [3, 7, 5],
        [6, 4, 2],
        [5, 9, 3],
        [8, 2, 7],
        [7, 6, 4],
        [4, 5, 6],
        [3, 8, 1],
        [6, 7, 3],
        [2, 9, 4],
        [8, 3, 5],
        [5, 6, 2],
        [7, 4, 8],
        [3, 5, 7],
        [9, 2, 6],
        [4, 7, 5],
        [6, 3, 1],
        [5, 8, 4],
        [7, 6, 3],
        [3, 9, 2],
        [8, 4, 7],
        [6, 5, 3],
        [4, 2, 6]
    ]
    return tiempos


def main():
    """
    Función principal que ejecuta IG e ILS sobre la misma instancia
    y compara los resultados obtenidos
    """
    tiempos = get_tiempos()
    
    flowshop = FlowShop(tiempos)

    print("=" * 60)
    print("METAHEURÍSTICAS ITERATIVAS: IG vs ILS")
    print("Problema: Flow Shop - Panadería")
    print("=" * 60)
    
    # Ejecutar Iterative Greedy
    print("\n[1] Ejecutando Iterative Greedy (IG)...")
    t0 = time.time()
    ig = IterativeGreedy(flowshop, 100, 15)
    mejor_solucion_ig, makespan_ig, iter_ig = ig.ejecutar()
    tiempo_ig = time.time() - t0

    # Ejecutar Iterated Local Search
    print("\n[2] Ejecutando Iterated Local Search (ILS)...")
    t0 = time.time()
    ils = IteratedLocalSearch(flowshop, 100, 100)
    mejor_solucion_ils, makespan_ils, iter_ils = ils.ejecutar()
    tiempo_ils = time.time() - t0
    
    # Mostrar comparación de resultados
    print("\n" + "=" * 60)
    print("COMPARACIÓN DE RESULTADOS")
    print("=" * 60)

    # Imprimir: makespan, secuencia, iteraciones, tiempo
    print("[1] IG: ", mejor_solucion_ig)
    print("Makespan: ", makespan_ig, ", Iteraciones: ", iter_ig, ", Tiempo: ", tiempo_ig)

    print()

    print("[2] ILS: ", mejor_solucion_ils)
    print("Makespan: ", makespan_ils, ", Iteraciones: ", iter_ils, ", Tiempo: ", tiempo_ils)
    

if __name__ == "__main__":
    main()
