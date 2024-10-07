import estado, transicion
import renglon as r
import Si as s
import Operations as op

eps = 'ε'
class AFN:
    def __init__(self):
        self.idAFN = 'a'
        self.edoInicial = None
        self.edosAFN = []
        self.alphabet = []
        self.edosAcept = []
        self.countIdAFN = 0
        self.automatas = []
        self.unido = False

    # Getters and Setters
    def get_idAFN(self):
        return self.idAFN

    def set_idAFN(self, idAFN):
        self.idAFN = idAFN

    def get_edoInicial(self):
        return self.edoInicial

    def set_edoInicial(self, edoInicial):
        self.edoInicial = edoInicial

    def get_edosAFN(self):
        return self.edosAFN

    def set_edosAFN(self, edosAFN):
        self.edosAFN = edosAFN

    def get_alphabet(self):
        return self.alphabet

    def set_alphabet(self, alphabet):
        self.alphabet = alphabet

    def get_edosAcept(self):
        return self.edosAcept

    def set_edosAcept(self, edosAcept):
        self.edosAcept = edosAcept

    def get_countIdAFN(self):
        return self.countIdAFN

    def set_countIdAFN(self, countIdAFN):
        self.countIdAFN = countIdAFN

    def get_automatas(self):
        return self.automatas

    def set_automatas(self, automatas):
        self.automatas = automatas

    def get_unido(self):
        return self.unido

    def set_unido(self, unido):
        self.unido = unido

    def init_data(self, idAFN, edoInicial, edosAFN, alphabet, edosAcept, countIdAFN, automatas, unido):
        self.set_idAFN(idAFN)
        self.set_edoInicial(edoInicial)
        self.set_edosAFN(edosAFN)
        self.set_alphabet(alphabet)
        self.set_edosAcept(edosAcept)
        self.set_countIdAFN(countIdAFN)
        self.set_automatas(automatas)
        self.set_unido(unido)
    
    def init_AFN(self, auxAFN):
        self.set_idAFN(auxAFN.get_idAFN())
        self.set_edoInicial(auxAFN.get_edoInicial())
        self.set_edosAFN(auxAFN.get_edosAFN())
        self.set_alphabet(auxAFN.get_alphabet())
        self.set_edosAcept(auxAFN.get_edosAcept())
        self.set_countIdAFN(auxAFN.get_countIdAFN())
        self.set_automatas(auxAFN.get_automatas())
        self.set_unido(auxAFN.get_unido())
    
    #metodos para trabajar con el automata
    def crearAFNBasicoChar(self, simbolo):
        e1, e2 = estado.Estado(), estado.Estado()
        t = transicion.Transicion()
        t.init_data(simbolo, simbolo, e2)
        e1.transiciones.append(t)
        e2.set_EdoAcept(True)

        self.set_edoInicial(e1)
        self.edosAFN.append(e1)
        self.edosAFN.append(e2)
        self.alphabet.append(simbolo)
        self.edosAcept.append(e2)
        self.set_unido(False)
    
    def crearAFNBasicoRange(self, simbolo1, simbolo2):
        e1, e2 = estado.Estado(), estado.Estado()
        t = transicion.Transicion()
        t.init_data(simbolo1, simbolo2, e2)
        e1.transiciones.append(t)
        e2.set_EdoAcept(True)

        self.set_edoInicial(e1)
        self.edosAFN.append(e1)
        self.edosAFN.append(e2)

        for i in range(ord(simbolo1), ord(simbolo2) + 1):
            self.alphabet.append(chr(i))

        self.edosAcept.append(e2)
        self.set_unido(False)
    
    def Unir(self,afn):
        e1, e2 = estado.Estado(), estado.Estado()
        t1, t2 = transicion.Transicion(), transicion.Transicion()

        t1.init_data(eps, eps, self.edoInicial)
        t2.init_data(eps, eps, afn.edoInicial)

        e1.transiciones.append(t1)
        e1.transiciones.append(t2)

        t3 = transicion.Transicion()
        t3.init_data(eps, eps, e2)

        for e in self.edosAcept:
            e.transiciones.append(t3)
            e.set_EdoAcept(False)
        for e in afn.edosAcept:
            e.transiciones.append(t3)
            e.set_EdoAcept(False)

        e2.set_EdoAcept(True)
        self.set_edoInicial(e1)

        for e in afn.edosAFN:
            self.edosAFN.append(e)

        self.edosAFN.append(e1)
        self.edosAFN.append(e2)
        self.edosAcept.clear()
        self.edosAcept.append(e2)
        for a in afn.alphabet:
            if a not in self.alphabet:
                self.alphabet.append(a)

    def Concatenar(self, afn):
        for t in afn.edoInicial.transiciones:
            for e in self.edosAcept:
                e.transiciones.append(t)
                e.set_EdoAcept(False)

        for e in afn.edosAFN:
            if e != afn.edoInicial:
                self.edosAFN.append(e)
        
        for a in afn.alphabet:
            if a not in self.alphabet:
                self.alphabet.append(a)
                
        self.edosAcept.clear()
        for e in afn.edosAcept:
            self.edosAcept.append(e)

    def CerraduraPositiva(self):
        e1, e2 = estado.Estado(), estado.Estado()
        t1 = transicion.Transicion()

        t1.init_data(eps, eps, self.edoInicial)
        e1.transiciones.append(t1)
        for e in self.edosAcept:
            taux1,taux2 = transicion.Transicion(), transicion.Transicion()
            taux1.init_data(eps, eps, e2)
            taux2.init_data(eps, eps, self.edoInicial)

            e.transiciones.append(taux1)
            e.transiciones.append(taux2)
            e.set_EdoAcept(False)
        
        self.edosAcept.clear()
        self.edosAcept.append(e2)
        e2.set_EdoAcept(True)
        self.set_edoInicial(e1)
        self.edosAFN.append(e1)
        self.edosAFN.append(e2)

    def CerraduraKleene(self):
        t = transicion.Transicion()

        self.CerraduraPositiva()
        t.init_data(eps,eps,self.edosAcept[0])
        self.edoInicial.transiciones.append(t)

    def Opcional(self):
        e1, e2 = estado.Estado(), estado.Estado()
        t1, t2 = transicion.Transicion(), transicion.Transicion()

        t1.init_data(eps, eps, self.edoInicial)
        t2.init_data(eps, eps, e2)
        e1.transiciones.append(t1)

        for e in self.edosAcept:
            e.transiciones.append(t2);
            e.set_EdoAcept(False)

        self.set_edoInicial(e1)
        self.edoInicial.transiciones.append(t2)
        e2.set_EdoAcept(True)
        self.edosAcept.clear()
        self.edosAcept.append(e2)
        self.edosAFN.append(e1)
        self.edosAFN.append(e2)
        return self
    
    def EstadoSi(self):
        token = 0
        C = []  # Conjunto of Si's
        Q = []  # Queue
        EdosAFN = []  # Queue of states
        counter = 0
        Saux = s.Si()

        counter += 1
        Saux.init_data(counter, op.CerraduraES(self.edoInicial))
        Saux.accept = op.EsAceptacion(Saux)

        Q.append(Saux)
        C.append(Saux)

        while len(Q) > 0:
            Saux = Q.pop(0)
            previous = Saux.get_id()
            i = 0  # Ensure `i` starts from 0 for each new state
            while i < len(self.alphabet):
                j = i
                Raux = r.Renglon()
                repetidos = []
                Sk = s.Si()  
                Sk.S = op.Ir_AC(Saux.S, self.alphabet[i])
                repetidos.append(self.alphabet[i])
                j += 1
                # Add a boundary check for `j` to prevent index out of range
                while j < len(self.alphabet) and Sk.S == op.Ir_AC(Saux.S, self.alphabet[j]):
                    repetidos.append(self.alphabet[j])
                    j += 1
                i = j  # Update `i` to avoid processing the same range again
                Sk.set_accept(op.EsAceptacion(Sk))

                if Sk.S:
                    if not op.ContieneSj(C, Sk):
                        counter += 1
                        Sk.set_id(counter)
                        Q.append(Sk)
                        C.append(Sk)
                        for element in repetidos:
                            Raux.Assign(element, Sk.get_id())
                        Raux.SetOrigin(previous)
                        if Sk.get_accept():
                            token += 10
                            Raux.setToken(token)
                        EdosAFN.append(Raux)
        return C, EdosAFN
