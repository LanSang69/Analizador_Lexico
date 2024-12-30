class Regla:
    def __init__(self):
        self.simbolo:str = ""
        self.terminal:bool = False
        self.nodos = []

    def __str__(self):
        return f'{self.id} -> {self.produccion}'

    def __eq__(self, other):
        if isinstance(other, Regla):
            return self.simbolo == other.simbolo and self.terminal == other.terminal and self.nodos == other.nodos
        return False