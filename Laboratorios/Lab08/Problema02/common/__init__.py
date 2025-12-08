"""
Módulo Común - Funciones compartidas por IG e ILS
"""

from .problema import FlowShop
from .heuristica import construir_solucion_greedy, reconstruir_goloso
from .busqueda_local import busqueda_local, generar_vecino

__all__ = [
    'FlowShop',
    'construir_solucion_greedy',
    'reconstruir_goloso',
    'busqueda_local',
    'generar_vecino'
]
