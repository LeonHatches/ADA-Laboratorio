class Pedido():
    def __init__(self, nombre, destino, peso, valor):
        self.nombre = nombre
        self.destino = destino
        self.peso = peso
        self.valor = valor

    def __str__(self):
        return f"Pedido(nombre={self.nombre}, destino={self.destino}, peso={self.peso}, valor={self.valor})"

def get_pedidos_1():
    pedidos = [
        Pedido("Paquete_A", "Arequipa_Centro", 120, 9),
        Pedido("Paquete_B", "Miraflores", 80, 6),
        Pedido("Paquete_C", "Cayma_Plaza", 200, 10),
        Pedido("Paquete_D", "Cayma_Chilina", 150, 8),
        Pedido("Paquete_E", "AltoSelvaAlegre", 90, 5),
        Pedido("Paquete_F", "Yanahuara", 60, 7),
        Pedido("Paquete_G", "Paucarpata", 140, 6),
        Pedido("Paquete_H", "Sabandia", 180, 5),
        Pedido("Paquete_I", "Characato", 250, 9),
        Pedido("Paquete_J", "Chiguata", 300, 10),
        Pedido("Paquete_K", "Uchumayo", 110, 4),
        Pedido("Paquete_L", "Tiabaya", 130, 5),
        Pedido("Paquete_M", "Sachaca", 70, 3),
        Pedido("Paquete_N", "Hunter", 50, 6),
        Pedido("Paquete_O", "CerroColorado", 160, 7)
    ]
    return pedidos

def get_pedidos_2():
    pedidos = [
        Pedido("Paquete_A", "Miraflores", 100, 7),
        Pedido("Paquete_B", "Paucarpata", 140, 9),
        Pedido("Paquete_C", "Zamacola", 180, 8),
        Pedido("Paquete_D", "Cayma_Plaza", 120, 6),
        Pedido("Paquete_E", "Yanahuara", 90, 5),
        Pedido("Paquete_F", "Sachaca", 110, 7),
        Pedido("Paquete_G", "Cerro_Colorado", 200, 10),
        Pedido("Paquete_H", "Hunter", 80, 4),
        Pedido("Paquete_I", "Chiguata", 250, 10),
        Pedido("Paquete_J", "Characato", 220, 9),
        Pedido("Paquete_K", "Tiabaya", 130, 6),
        Pedido("Paquete_L", "Alto_Selva_Alegre", 150, 8),
        Pedido("Paquete_M", "Arequipa_Centro", 170, 9),
        Pedido("Paquete_N", "Socabaya", 100, 5),
        Pedido("Paquete_O", "Av_Independencia", 160, 7)
    ]
    return pedidos

def get_pedidos_3():
    pedidos = [
        Pedido("Paquete_A", "Cayma_Chilina", 120, 8),
        Pedido("Paquete_B", "Arequipa_Centro", 90, 6),
        Pedido("Paquete_C", "Sabandia", 200, 10),
        Pedido("Paquete_D", "Miraflores", 150, 7),
        Pedido("Paquete_E", "Paucarpata", 110, 5),
        Pedido("Paquete_F", "Yanahuara", 80, 6),
        Pedido("Paquete_G", "Cerro_Colorado", 180, 9),
        Pedido("Paquete_H", "Tiabaya", 130, 6),
        Pedido("Paquete_I", "Characato", 250, 10),
        Pedido("Paquete_J", "Chiguata", 300, 10),
        Pedido("Paquete_K", "Uchumayo", 100, 4),
        Pedido("Paquete_L", "Alto_Selva_Alegre", 140, 7),
        Pedido("Paquete_M", "Cayma_Plaza", 160, 8),
        Pedido("Paquete_N", "Sachaca", 70, 3),
        Pedido("Paquete_O", "Hunter", 150, 7)
    ]
    return pedidos
