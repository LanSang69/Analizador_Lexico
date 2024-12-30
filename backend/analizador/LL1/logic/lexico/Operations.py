from . import renglon as r
from . import Si as s
from . import AFN as a
from . import regexToPost as regex
import random
operators = ['|', '*', '+', '&']
eps = 'ε'

def print_afn_details(afn):
    details = []
    count = 0
    for e in afn.edosAFN:
        count += 1
        e.idEdo = count

    details.append(f"Edo inicial: ({afn.edoInicial.idEdo})")
    for element in afn.edosAFN:
        for t in element.transiciones:
            left, right = ' ', ' '
            if t.edoDestino.EdoAcept:
                right = ')'
                left = '('
            details.append(f"({element.idEdo}) -- [{t.simboloInf}-{t.simboloSup}] --> {left}({t.edoDestino.idEdo}){right}")
    Sj, queue = afn.EstadoSi()
    return "\n".join(details)

def expToAFN(exp):
    pila = []
    postfix, dictionary = regex.regex_to_postfix(exp)
    i = 0
    while i < len(postfix):
        if postfix[i] == "|":
            e1: a.AFN = pila.pop()
            e2: a.AFN = pila.pop()
            e1.Unir(e2)
            pila.append(e1)
        elif postfix[i] == "*":
            e1: a.AFN = pila.pop()
            e1.CerraduraKleene()
            pila.append(e1)
        elif postfix[i] == "+" and len(pila) > 0 and postfix[i-1] not in operators:
            e1: a.AFN = pila.pop()
            e1.CerraduraPositiva()
            pila.append(e1)
        elif postfix[i] == "&":
            e2: a.AFN = pila.pop()
            e1: a.AFN = pila.pop()
            e1.Concatenar(e2)
            pila.append(e1)
        elif postfix[i] == "?":
            e1: a.AFN = pila.pop()
            e1.Opcional()
            pila.append(e1)
        else:
            if postfix[i] in dictionary:
                aux = a.AFN()
                left, right = dictionary[postfix[i]].split("-")
                aux.crearAFNBasicoRange(left,right)
                pila.append(aux)
            else:
                aux = a.AFN()
                aux.crearAFNBasicoChar(postfix[i])
                pila.append(aux)

        i += 1

    if len(pila) == 1:
        return pila.pop()
    else:
        raise ValueError("Error: La pila quedó con elementos sobrantes.")
            


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
        if element.S == Sj.S:
            return True
    return False


def EsAceptacion(Sj):
    for e in Sj.S:
        if e.EdoAcept:
            return True
    return False

def getIdEdoAcept(Sj):
    for e in Sj.S:
        if e.EdoAcept:
            return hex(id(e))
    return -1


def IndexOfSj(C, Sk):

    for index, si in enumerate(C):

        if si == Sk:

            return index

    return -1

def generate_random_id():
    return random.randint(1000000000, 9999999999)