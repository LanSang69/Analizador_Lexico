import estado

class Transicion:
    def __init__(self):
        self.simboloInf = ''
        self.simboloSup = ''
        self.edoDestino = estado.Estado()

    @classmethod
    def init_data(cls, simboloInf, simboloSup, edoDestino):
        transicion = cls()
        transicion.simboloInf = simboloInf
        transicion.simboloSup = simboloSup
        transicion.edoDestino = edoDestino 
        return transicion

    @classmethod
    def init_transicion(cls, auxTrans):
        transicion = cls()
        transicion.simboloInf = auxTrans.simboloInf
        transicion.simboloSup = auxTrans.simboloSup
        transicion.edoDestino = auxTrans.edoDestino
        return transicion
    
    # simboloInf
    @property
    def simboloInf(self):
        return self._simboloInf

    @simboloInf.setter
    def simboloInf(self, simboloInf):
        self._simboloInf = simboloInf

    # simboloSup
    @property
    def simboloSup(self):
        return self._simboloSup

    @simboloSup.setter
    def simboloSup(self, simboloSup):
        self._simboloSup = simboloSup

    # edoDestino
    @property
    def edoDestino(self):
        return self._edoDestino

    @edoDestino.setter
    def edoDestino(self, edoDestino):
        self._edoDestino = edoDestino