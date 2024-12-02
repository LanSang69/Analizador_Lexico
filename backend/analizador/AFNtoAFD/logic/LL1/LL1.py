from .lexico import Analizador as A
from .lexico import AFD

class LL1:
    def __init__(self):
        self.Gramatica = ""
        self.Analisis = None
        self.ArrReglas = []
        self.numReglas = 0
        self.Vn = set()
        self.Vt = set()
    def initialize(self, sigma, fileAFD, idAFD):
        self.Gramatica = sigma
        auxAFD = AFD.AFD()
        auxAFD.leerString(fileAFD)
        analisis = A.AnalizadorLexico()
        analisis.initWithTable(sigma, auxAFD)
    #Haccer First
    #Hacer Follow
    #Hacer gramatica de gramaticas