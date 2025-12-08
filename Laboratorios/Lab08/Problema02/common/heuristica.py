"""
Heurística Constructiva - Greedy/NEH
"""
from .problema import FlowShop


def construir_solucion_greedy(flowshop : FlowShop):
    tiempos_totales = []    # Se calculan la suma de tiempos totales por pan 
    for index, tiempos in enumerate(flowshop.tiempos):
        suma_tiempos = sum(tiempos)
        tiempos_totales.append((index, suma_tiempos))

    tiempos_totales.sort(key=lambda x: x[1], reverse=True)
    
    secuencia = []

    # Utiliza método goloso para obtener la mejor secuencia en base a lo que primero encuentre
    for job, _ in tiempos_totales:
        mejor_makespan = float("inf")
        mejor_pos = 0

        for pos in range(len(secuencia) + 1):
            nueva = secuencia[:pos] + [job] + secuencia[pos:]
            valor = flowshop.calcular_makespan(nueva)

            if valor < mejor_makespan:
                mejor_makespan = valor
                mejor_pos = pos

        secuencia.insert(mejor_pos, job)

    return secuencia

def reconstruir_goloso(flowshop : FlowShop, secuencia_parcial, elementos_destruidos):
    n_secuencia = secuencia_parcial.copy()

    for e in elementos_destruidos: # Se itera sobre los elementos destruidos
        mejor_makespan = float("inf")
        mejor_pos = 0

        for pos in range(len(n_secuencia) + 1):     # Se prueba para encontrar el mejor lugar para poner el elemento
            candidata = n_secuencia[:pos] + [e] + n_secuencia[pos:]
            makespan = flowshop.calcular_makespan(candidata)

            if makespan < mejor_makespan:
                mejor_makespan = makespan
                mejor_pos = pos

        n_secuencia.insert(mejor_pos, e)

    return n_secuencia

