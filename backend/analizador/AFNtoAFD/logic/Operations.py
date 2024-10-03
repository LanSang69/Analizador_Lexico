import renglon as r
import Si as s
eps = 'ε'

def CerraduraES(state):
    P = []
    C = []
    
    P.append(state)
    while len(P) > 0:
        aux = P.pop()
        if aux not in C:
            C.append(aux)
            for t in aux.transiciones:
                if t.simboloInf == eps:
                    P.append(t.edoDestino)
        
    return C

def CerraduraEC(conjunto):
    R = []
    for e in conjunto:
        for estado in CerraduraES(e):
            if estado not in R:
                R.append(estado)

    return R

def MoverS(estado, simbolo):
    R = []
    for t in estado.transiciones:
        if ord(t.simboloInf) <= ord(simbolo) <= ord(t.simboloSup):
            R.append(t.edoDestino)
    return R

def MoverC(conjunto, simbolo):
    R = []
    for e in conjunto:
        for estado in MoverS(e, simbolo):
            if estado not in R:
                R.append(estado)
    return R

def Ir_AS(estado, simbolo):
    return CerraduraES(MoverS(estado,simbolo))

def Ir_AC(conjunto, simbolo):
    R = []
    R = CerraduraEC(MoverC(conjunto, simbolo))
    return R 

def ContieneSj(C, Sj):
    for element in C:
        if element == Sj:
            return True
    return False


def EsAceptacion(Sj):
    for e in Sj.S:
        if e.EdoAcept:
            return True
    return False