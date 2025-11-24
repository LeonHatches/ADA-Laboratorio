class Pedido():
    def __init__(self, destino, peso, valor):
        self.destino = destino
        self.peso = peso
        self.valor = valor

    def __str__(self):
        return f"Pedido(destino={self.destino}, peso={self.peso}, valor={self.valor})"