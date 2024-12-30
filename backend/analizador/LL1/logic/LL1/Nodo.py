class Nodo:
    def __init__(self,simbolo,terminal):
        self.simbolo = simbolo
        self.terminal = terminal 
    def __eq__(self, value):
        return self.simbolo == value.simbolo and self.terminal == value.terminal
    def __hash__(self):
        return hash((self.simbolo, self.terminal))
