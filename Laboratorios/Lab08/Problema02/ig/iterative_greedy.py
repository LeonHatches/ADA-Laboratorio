"""
Algoritmo Iterative Greedy (IG)
"""
import random

import random
from common.heuristica import construir_solucion_greedy, reconstruir_goloso
from common.busqueda_local import busqueda_local


class IterativeGreedy:
    """
    Implementación del algoritmo Iterative Greedy para flow shop
    """
    
    def __init__(self, flowshop, max_iter=100, d=2):
        """
        Inicializa el algoritmo IG
        
        Args:
            flowshop: instancia del problema
            max_iter: número máximo de iteraciones
            d: número de elementos a destruir en cada iteración
        """

        self.flowshop = flowshop
        self.max_iter = max_iter
        self.d = d
    
    def destruir(self, secuencia):
        n_secuencia = secuencia.copy() # Se crea copia de secuencia
        eliminar = []

        for _ in range(self.d):  # Se eliminan d elementos aleatorios de la secuencia
            x = random.randrange(len(n_secuencia))
            eliminar.append(n_secuencia.pop(x))

        return n_secuencia, eliminar    # Se regresa la secuencia parcial y elementos eliminados

    

    def criterio_aceptacion(self, makespan_nuevo, makespan_mejor):
        return makespan_nuevo < makespan_mejor
    
    def ejecutar(self):
        # Se genera solucion inicial greedy
        sol_actual = construir_solucion_greedy(self.flowshop)
        makespan_actual = self.flowshop.calcular_makespan(sol_actual)

        sol_mejor = sol_actual.copy()
        makespan_mejor = makespan_actual

        for _ in range(self.max_iter):
            # Destruir parte de solucion
            sol_parcial, eliminados = self.destruir(sol_actual)

            # Reconstruir solucion parcial
            sol_reconstruida = reconstruir_goloso(self.flowshop, sol_parcial, eliminados)

            # Se calcula nuevo makespan con la nueva solucion
            makespan_reconstruida = self.flowshop.calcular_makespan(sol_reconstruida)

            # Se analiza si se elegira con el criterio de aceptacion
            if self.criterio_aceptacion(makespan_actual, makespan_reconstruida):
                sol_actual = sol_reconstruida
                makespan_actual = makespan_reconstruida

            # Se actualiza solucion global
            if makespan_reconstruida < makespan_mejor:
                sol_mejor = sol_reconstruida
                makespan_mejor = makespan_reconstruida

        return sol_mejor, makespan_mejor, self.max_iter
        