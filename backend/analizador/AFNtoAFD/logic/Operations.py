import renglon as r
import Si as s
import AFN as a
import regexToPost as regex
operators = ['|', '*', '+', '&']
eps = 'ε'

def print_afn_details(afn):
    count = 0
    for e in afn.edosAFN:
        count += 1
        e.idEdo = count

    print("inicial: ", afn.edoInicial.idEdo)
    for e in afn.edosAcept:
        print("Aceptacion: ", e.idEdo)
    for element in afn.edosAFN:
        for t in element.transiciones:
            print(element.idEdo, "(", t.simboloInf, "-" , t.simboloSup, ")","-->",t.edoDestino.idEdo)
    Sj, queue = afn.EstadoSi()
    return Sj, queue

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

        for e in pila:
            print("_______________________________")
            print(postfix[i])
            print_afn_details(e)
            print("_______________________________")
        i += 1

    if len(pila) == 1:
        return pila.pop()
    else:
        raise ValueError("Error: The stack does not contain exactly one element.")
            


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


def IndexOfSj(C, Sk):

    for index, si in enumerate(C):

        if si.S == Sk.S:

            return index

    return -1
