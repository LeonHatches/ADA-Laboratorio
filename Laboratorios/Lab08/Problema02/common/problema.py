
class FlowShop:
    """
    Clase que representa el problema de flow shop de la panadería
    con tres máquinas: amasar, hornear y empaquetar
    """
    
    def __init__(self, tiempos_procesamiento):
        # Inicializa el problema de flow shop
        
        # Se guardan los datos
        self.tiempos    = tiempos_procesamiento
        self.n_jobs     = len(tiempos_procesamiento)
        self.n_machines = len(tiempos_procesamiento[0])
    
    def calcular_makespan(self, secuencia):
        
        # Calcula el makespan (tiempo total) para una secuencia dada
        
        # Matriz de tiempos de finalización
        C = [[0] * self.n_machines for _ in range(self.n_jobs)]

        for j, job in enumerate(secuencia):
            for m in range(self.n_machines):

                # Tiempo de procesamiento del pan 'job' en máquina 'm'
                p = self.tiempos[job][m]

                if j == 0 and m == 0:
                    # Primer pan en primera máquina
                    C[j][m] = p

                elif j == 0:
                    # Primer pan, pero máquina siguiente
                    C[j][m] = C[j][m - 1] + p

                elif m == 0:
                    # Primera máquina, pero pan siguiente
                    C[j][m] = C[j - 1][m] + p

                else:
                    # Caso general
                    C[j][m] = max(C[j - 1][m], C[j][m - 1]) + p

        # Makespan = fin del último pan en la última máquina
        return C[self.n_jobs - 1][self.n_machines - 1]