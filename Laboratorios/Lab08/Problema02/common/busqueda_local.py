import random
import copy

"""
Búsqueda Local y Vecindario
"""


def generar_vecino(secuencia, tipo='swap'):
    """
    Genera un vecino de la secuencia actual
    """

    # Generación de vecinos

    n      = len(secuencia)
    vecino = secuencia.copy()

    if tipo == 'swap':
        i, j = random.sample(range(n), 2)
        vecino[i], vecino[j] = vecino[j], vecino[i]

    elif tipo == 'insert':
        i, j = random.sample(range(n), 2)
        elem = vecino.pop(i)
        vecino.insert(j, elem)

    else:
        raise ValueError("Tipo de vecindario no soportado")


def busqueda_local(flowshop, secuencia_inicial):
    """
    Realiza búsqueda local para mejorar una solución
    Explora el vecindario hasta encontrar un óptimo local
    """

    mejor_secuencia = secuencia_inicial.copy()
    mejor_makespan  = flowshop.calcular_makespan(mejor_secuencia)
    mejora          = True

    while mejora:
        mejora          = False
        mejor_vecino    = None
        mejor_vecino_mk = mejor_makespan

        # Explora todo el vecindario
        for i in range(len(mejor_secuencia)):
            
            for j in range(i + 1, len(mejor_secuencia)):
                # Generar vecino con swap fijo
                vecino = mejor_secuencia.copy()
                vecino[i], vecino[j] = vecino[j], vecino[i]

                mk = flowshop.calcular_makespan(vecino)

                if mk < mejor_vecino_mk:
                    mejor_vecino = vecino
                    mejor_vecino_mk = mk
                    mejora = True
            
        if mejora:
            mejor_secuencia = mejor_vecino
            mejor_makespan  = mejor_vecino_mk
    
    return mejor_secuencia, mejor_makespan

