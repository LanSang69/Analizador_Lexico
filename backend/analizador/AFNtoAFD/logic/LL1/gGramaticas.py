from ..lexico import Analizador
import Simbolos

#Descenso recursivo
class GramaticaGramaticas:
    def __init__(self):
        self.Gramatica = ""
        self.A = Analizador.AnalizadorLexico()
        self.S = Simbolos.Simbolos()
        self.Vn = None
        self.Vt = None

    def initWithAnalizer(self, gramatica, A):
        self.Gramatica = gramatica
        self.A = A

    def initWithAFD(self, gramatica, AFD):
        self.Gramatica = gramatica
        self.A.initWithTable(gramatica, AFD)

    def Gramatica(self) -> bool:
        if self.ListaReglas():
            return True;
        return False;

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
        if self.LadoIzquierdo():
            Token = self.A.yylex()
            if Token == self.S.FLECHA:
                if self.LadosDerechos():
                    return True
        return False

    def LadoIzquierdo(self) -> bool:
        Token = self.A.yylex()
        if Token == self.S.SIMBOLO:
            return True
        
    def LadosDerechos(self):
        if self.LadoDerecho():
            if self.LadosDerechosP():
                return True
        return False

    def LadosDerechosP(self) -> bool:
        Token = self.A.yylex()
        if Token == self.S.OR:
            if self.LadoDerecho():
                if self.LadosDerechosP():
                    return True
            return False
        self.A.UndoToken()
        return True

    def LadoDerecho(self) -> bool:
        if self.SecSimbolos():
            return True
        return False

    def SecSimbolos(self):
        Token = self.A.yylex();
        if Token == self.S.SIMBOLO:
            if self.SecSimbolosP():
                return True
        return False

    def SecSimbolosP(self):
        Token = self.A.yylex()
        if Token == self.S.SIMBOLO:
            if self.SecSimbolosP():
                return True
        self.A.UndoToken()
        return True