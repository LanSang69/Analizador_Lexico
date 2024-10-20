from . import AFN
from .import simbolosEspeciales as s

class AFD:
    def __init__(self) -> None:
        self.IdAFD = 0
        self.NumEstados = 0
        self.tablaAFD = None
        self.archivo = None
    
    def initTabla(self, queue) -> None:
        table = [["irrelevant"]]
        # -----------------------------------------
        # | id Edo | elementos ascii[256] | token |
        # -----------------------------------------
        while len(queue) > 0:
            renglon = []
            top = queue.pop(0)
            for m in top.movimientos:
                renglon.append(m)
            table.append(renglon)
        
        self.tablaAFD = table

    def setIdAFD(self, IdAFD):
        self.IdAFD = IdAFD

    def setConjAFDs(self, ConjAFDs):
        self.ConjAFDs = ConjAFDs

    def setAlfabeto(self, alfabeto):
        self.alfabeto = alfabeto

    def setNumEstados(self, NumEstados):
        self.NumEstados = NumEstados
    
    def setTablaAFD(self, tabla):
        self.tablaAFD = tabla

    def getIdAFD(self):
        return self.IdAFD

    def getConjAFDs(self):
        return self.ConjAFDs

    def getAlfabeto(self):
        return self.alfabeto

    def getNumEstados(self):
        return self.NumEstados

    def getTablaAFD(self):
        return self.tablaAFD
    
    #Metodos para crear archivo y para leer archivo
    def guardarEnString(self):
        resultado = f"{self.NumEstados}\n"
        
        for e in self.getTablaAFD():
            resultado += "\t".join(str(m) for m in e)
            if e != self.getTablaAFD()[-1]:
                resultado += "\n"
        
        self.archivo = resultado

    def leerString(self, archivo):
        self.setTablaAFD([])
        lines = archivo.strip().split("\n")

        self.setNumEstados(int(lines[0].strip()))
        self.tablaAFD = []

        for line in lines[1:]:
            elementos = line.strip().split("\t")
            self.tablaAFD.append(elementos)