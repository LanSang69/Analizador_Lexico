from ..lexico import Analizador
from . import Simbolos
from . import Nodo
from . import Regla

#Descenso recursivo
class GramaticaGramaticas:
    def __init__(self):
        self.Gramatica = ""
        self.ReglasG = []
        self.A = Analizador.AnalizadorLexico()
        self.S = Simbolos.Simbolos()
        self.Vn = []
        self.Vt = []
        self.counter = 0
        self.NumReglas = 0
    
    def __eq__(self, value):
        return self.Gramatica == value.Gramatica and self.A == value.A and self.S == value.S and self.Vn == value.Vn and self.Vt == value.Vt and self.counter == value.counter

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
            if int(Token) == self.S.PC:
                if self.ListaReglasP():
                    return True
        return False

    def ListaReglasP(self) -> bool:
        EdoAnalizador = self.A.getEstatus()
        if self.Reglas():
            Token = self.A.yylex()
            if int(Token) == self.S.PC:
                if self.ListaReglasP():
                    return True
                return False
        self.A.setEstatus(EdoAnalizador)
        return True
        
    def Reglas(self) -> bool:
        izquierdo:list = [""]
        if self.LadoIzquierdo(izquierdo):
            Token = self.A.yylex()
            if int(Token) == self.S.FLECHA:
                if self.LadosDerechos(izquierdo):
                    return True
        return False

    def LadoIzquierdo(self, izquierdo:list) -> bool:
        Token = self.A.yylex()
        if int(Token) == self.S.SIMBOLO:
            izquierdo[0] = self.A.yytext()
            izquierdo[0] = izquierdo[0][1:-1]
            return True
        return False
        
    def LadosDerechos(self, izquierdo:list) -> bool:
        l = []
        if self.LadoDerecho(l):
            self.ReglasG.append(Regla.Regla())
            self.ReglasG[self.counter].simbolo=izquierdo[0]
            self.ReglasG[self.counter].nodos=l
            self.ReglasG[self.counter].terminal=False
            self.counter+=1
            if self.LadosDerechosP(izquierdo):
                return True
        return False

    def LadosDerechosP(self,izquierdo:list) -> bool:
        l = []
        Token = self.A.yylex()
        if int(Token) == self.S.OR:
            if self.LadoDerecho(l):
                self.ReglasG.append(Regla.Regla())
                self.ReglasG[self.counter].simbolo=izquierdo[0]
                self.ReglasG[self.counter].nodos=l
                self.ReglasG[self.counter].terminal=False
                self.counter+=1
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
        if int(Token) == self.S.SIMBOLO:
            simbolo = self.A.yytext()
            simbolo = simbolo[1:-1]
            nodo = Nodo.Nodo(simbolo,False)
            lista.append(nodo)
            if self.SecSimbolosP(lista):
                return True
        return False

    def SecSimbolosP(self,lista):
        Token = self.A.yylex()
        if int(Token) == self.S.SIMBOLO:
            simbolo = self.A.yytext()
            simbolo = simbolo[1:-1]
            nodo = Nodo.Nodo(simbolo,False)
            lista.append(nodo)
            if self.SecSimbolosP(lista):
                return True
            return False
        self.A.UndoToken()
        return True
    
    def AnalizarGramatica(self):
        for item in self.ReglasG:
            if item.simbolo not in self.Vn:
                self.Vn.append(item.simbolo)
        
        for item in self.ReglasG:
            for ld in item.nodos:
                if ld.simbolo not in self.Vn:
                    ld.terminal = True
                    self.Vt.append(ld.simbolo)
        
        self.NumReglas = len(self.ReglasG)

    
