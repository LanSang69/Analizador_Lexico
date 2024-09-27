import estado, transicion
eps = 'ε'
class AFN:
    def __init__(self):
        self.idAFN = 'a'
        self.edoInicial = estado.Estado()
        self.edosAFN = []
        self.alphabet = []
        self.edosAcept = []
        self.countIdAFN = 0
        self.automatas = []
        self.unido = False

    @classmethod
    def init_data(cls, idAFN, edoInicial, edosAFN, alphabet, edosAcept, countIdAFN, automatas, unido):
        afn = cls()
        afn.idAFN = idAFN
        afn.edoInicial = edoInicial
        afn.edosAFN = edosAFN
        afn.alphabet = alphabet
        afn.edosAcept = edosAcept
        afn.countIdAFN = countIdAFN
        afn.automatas = automatas
        afn.unido = unido
        return afn
    
    @classmethod
    def init_AFN(cls, auxAFN):
        afn = cls()
        afn.idAFN = auxAFN.idAFN
        afn.edoInicial = auxAFN.edoInicial
        afn.edosAFN = auxAFN.edosAFN
        afn.alphabet = auxAFN.alphabet
        afn.edosAcept = auxAFN.edosAcept
        afn.countIdAFN = auxAFN.countIdAFN
        afn.automatas = auxAFN.automatas
        afn.unido = auxAFN.unido
        return afn
    
    # idAFN
    @property
    def idAFN(self):
        return self._idAFN

    @idAFN.setter
    def idAFN(self, value):
        self._idAFN = value

    # edoInicial
    @property
    def edoInicial(self):
        return self._edoInicial

    @edoInicial.setter
    def edoInicial(self, value):
        self._edoInicial = value

    # edosAFN
    @property
    def edosAFN(self):
        return self._edosAFN

    @edosAFN.setter
    def edosAFN(self, value):
        self._edosAFN = value

    # alphabet
    @property
    def alphabet(self):
        return self._alphabet

    @alphabet.setter
    def alphabet(self, value):
        self._alphabet = value

    # edosAcept
    @property
    def edosAcept(self):
        return self._edosAcept

    @edosAcept.setter
    def edosAcept(self, value):
        self._edosAcept = value

    # countIdAFN
    @property
    def countIdAFN(self):
        return self._countIdAFN

    @countIdAFN.setter
    def countIdAFN(self, value):
        self._countIdAFN = value

    # automatas
    @property
    def automatas(self):
        return self._automatas

    @automatas.setter
    def automatas(self, value):
        self._automatas = value

    # unido
    @property
    def unido(self):
        return self._unido

    @unido.setter
    def unido(self, value):
        self._unido = value

    #metodos para trabajar
    @classmethod
    def crearAFNBasicoChar(cls, simbolo, count):
        count += 1
        automata = cls()
        e1, e2 = estado.Estado(), estado.Estado()

        t = transicion.Transicion.init_data(simbolo, simbolo, e2)
        e1.transiciones.append(t)
        e2.edo_acept = True

        automata.edoInicial = e1
        automata.edoInicial.id_edo = count
        count += 1
        automata.edosAFN.append(e1)
        automata.edosAFN.append(e2)
        automata.alphabet.append(simbolo)
        automata.edosAcept.append(e2)
        automata.edosAcept[0].id_edo = count
        automata.unido = False

        return automata, count
    
    @classmethod
    def crearAFNBasicoRange(cls, simbolo1, simbolo2):
        automata = cls()
        e1, e2 = estado.Estado(), estado.Estado()

        t = transicion.Transicion.init_data(simbolo1, simbolo2, e2)
        e1.transiciones.append(t)
        e2.edo_acept = True

        automata.edoInicial = e1
        automata.edosAFN.append(e1)
        automata.edosAFN.append(e2)

        for i in range(ord(simbolo1), ord(simbolo2) + 1):
            automata.alphabet.append(chr(i))

        automata.edosAcept.append(e2)
        automata.unido = False

        return automata
    
    @classmethod
    def Unir(_,current, afn):
        e1, e2 = estado.Estado(), estado.Estado()
        t1 = transicion.Transicion.init_data(eps, eps, current.edoInicial)
        t2 = transicion.Transicion.init_data(eps, eps, afn.edoInicial)

        e1.transiciones.append(t1)
        e1.transiciones.append(t2)
        t1 = transicion.Transicion.init_data(eps, eps, e2)

        for e in current.edosAcept:
            e.transiciones.append(t1)
            e.edo_acept = False
        for e in afn.edosAcept:
            e.transiciones.append(t1)
            e.edo_acept = False

        e2.edo_acept = True
        current.edoInicial = e1

        for e in afn.edosAFN:
            current.edosAFN.append(e)
        

        current.edosAFN.append(e1)
        current.edosAFN.append(e2)
        current.edosAcept.clear()
        current.edosAcept.append(e2)
        for a in afn.alphabet:
            if a not in current.alphabet:
                current.alphabet.append(a)
        return current