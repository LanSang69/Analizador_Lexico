import backend.analizador.AFNtoAFD.logic.LL1.Regla as R


class LR0:
    def __init__(self):
        self.gramatica = [] #type: [R.regla()]
        self.terminales = [] #type: [str]
        self.noTerminales = []

    def __eq__(self, other):
        if isinstance(other,LR0):
            return self.gramatica == other.gramatica and self.terminales == other.terminales and self.noTerminales == other.noTerminales
        return False
    
    def initWithString(self,string):
        lines = string.split("\n")
        for line in lines:
            izquierdo = line.split("->")[0]
            derecho = line.split("->")[1]