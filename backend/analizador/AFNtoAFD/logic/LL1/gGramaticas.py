from ..lexico import Analizador
from . import Simbolos
from . import Nodo

#Descenso recursivo
class GramaticaGramaticas:
    def __init__(self):
        self.Gramatica = ""
        self.Reglas = []
        self.A = Analizador.AnalizadorLexico()
        self.S = Simbolos.Simbolos()
        self.Vn = None
        self.Vt = None
        self.counter = 0

    def initWithAnalizer(self, gramatica, A):
        self.Gramatica = gramatica
        self.A = A

    def initWithAFD(self, gramatica, AFD):
        self.Gramatica = gramatica
        self.A.initWithTable(gramatica, AFD)

    def G(self) -> bool:
        if self.ListaReglas():
            return True
        return False

    def ListaReglas(self) -> bool:
        if self.Reglas():
            Token = self.A.yylex()
            if Token == self.S.PC:
                if self.ListaReglasP():
                    return True
        return False

    def ListaReglasP(self) -> bool:
        EdoAnalizador = self.A.getEstatus()
        if self.Reglas():
            Token = self.A.yylex()
            if Token == self.S.PC:
                if self.ListaReglasP():
                    return True
                return False
        self.A.setEstatus(EdoAnalizador)
        return True
        
    def Reglas(self) -> bool:
        izquierdo:list = [""]
        if self.LadoIzquierdo(izquierdo):
            Token = self.A.yylex()
            if Token == self.S.FLECHA:
                if self.LadosDerechos(izquierdo):
                    return True
        return False

    def LadoIzquierdo(self, izquierdo:list) -> bool:
        Token = self.A.yylex()
        if Token == self.S.SIMBOLO:
            izquierdo[0] = self.A.yytext()
            izquierdo[0] = izquierdo[0][1:-1]
            return True
        return False
        
    def LadosDerechos(self, izquierdo:list) -> bool:
        l = []
        if self.LadoDerecho(l):
            self.Reglas[self.counter].simbolo=izquierdo[0]
            self.Reglas[self.counter].nodos=l
            self.Reglas[self.counter].terminal=False
            self.counter+=1
            if self.LadosDerechosP(izquierdo):
                return True
        return False

    def LadosDerechosP(self,izquierdo:list) -> bool:
        l = []
        Token = self.A.yylex()
        if Token == self.S.OR:
            if self.LadoDerecho(l):
                self.Reglas[self.counter].simbolo=izquierdo[0]
                self.Reglas[self.counter].nodos=l
                self.Reglas[self.counter].terminal=False
                if self.LadosDerechosP(izquierdo):
                    return True
            return False
        self.A.UndoToken()
        return True

    def LadoDerecho(self, lista) -> bool:
        if self.SecSimbolos(lista):
            return True
        return False

    def SecSimbolos(self,lista):
        Token = self.A.yylex()
        if Token == self.S.SIMBOLO:
            simbolo = self.A.yytext()
            simbolo = simbolo[1:-1]
            nodo = Nodo.Nodo(simbolo,False)
            if self.SecSimbolosP(lista):
                lista.append(nodo)
                return True
        return False

    def SecSimbolosP(self,lista):
        Token = self.A.yylex()
        if Token == self.S.SIMBOLO:
            simbolo = self.A.yytext()
            simbolo = simbolo[1:-1]
            nodo = Nodo.Nodo(simbolo,False)
            if self.SecSimbolosP(lista):
                lista.append(nodo)
                return True
            return False
        self.A.UndoToken()
        return True