import estado

class Transicion:
    def __init__(self):
        self.simboloInf = ''
        self.simboloSup = ''
        self.edoDestino = estado.Estado()

    def init_data(self, simboloInf, simboloSup, edoDestino):
        self.simboloInf = simboloInf
        self.simboloSup = simboloSup
        self.edoDestino = edoDestino 

    def init_self(self, auxTrans):
        self.simboloInf = auxTrans.simboloInf
        self.simboloSup = auxTrans.simboloSup
        self.edoDestino = auxTrans.edoDestino