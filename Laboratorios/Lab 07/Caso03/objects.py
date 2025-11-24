class Pedido():
    def __init__(self, nombre, destino, peso, valor):
        self.nombre = nombre
        self.destino = destino
        self.peso = peso
        self.valor = valor

    def __str__(self):
        return f"Pedido(nombre={self.nombre}, destino={self.destino}, peso={self.peso}, valor={self.valor})"

def get_pedidos():
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
