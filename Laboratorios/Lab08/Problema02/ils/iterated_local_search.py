"""
Algoritmo Iterated Local Search (ILS)
PERSONA 6: Implementa el algoritmo ILS completo
"""

import random
from common.heuristica import construir_solucion_greedy
from common.busqueda_local import busqueda_local


class IteratedLocalSearch:
    """
    Implementación del algoritmo Iterated Local Search para flow shop
    """
    
    def __init__(self, flowshop, max_iter=100, perturbacion_size=3):

        self.flowshop          = flowshop
        self.max_iter          = max_iter
        self.perturbacion_size = perturbacion_size
    
    def perturbar(self, secuencia):
        """
        Aplica perturbación a la solución actual
        (movimientos más fuertes que búsqueda local)
        """

        nueva = secuencia.copy()
        n     = len(nueva)

        for _ in range(self.perturbacion_size):
            i, j = random.sample(range(n), 2)
            nueva[i], nueva[j] = nueva[j], nueva[i]

        return nueva
    
    def criterio_aceptacion(self, makespan_nuevo, makespan_mejor):
        """
        Decide si acepta la nueva solución
        """
        return makespan_nuevo <= makespan_mejor
    
    def ejecutar(self):
        """
        Ejecuta el algoritmo ILS completo
        """

        # Construcción inicial (Cambiar si se realiza construcción greedy)

        # secuencia = construir_solucion_greedy(self.flowshop)
        secuencia = random.sample(range(self.flowshop.n_jobs), self.flowshop.n_jobs)

        # Óptimo local
        secuencia, mk = busqueda_local(self.flowshop, secuencia)

        mejor_secuencia = secuencia.copy()
        mejor_makespan  = mk

        # Bucle principal
        for it in range(self.max_iter):

            # Perturbar la solución
            nueva = self.perturbar(secuencia)

            # Nueva búsqueda local
            nueva, mk_nueva = busqueda_local(self.flowshop, nueva)

            # Criterio de aceptación
            if self.criterio_aceptacion(mk_nueva, mk):
                secuencia = nueva
                mk        = mk_nueva
            
            # Actualizar mejor global
            if mk_nueva < mejor_makespan:
                mejor_secuencia = nueva
                mejor_makespan  = mk_nueva
        
        return mejor_secuencia, mejor_makespan, self.max_iter