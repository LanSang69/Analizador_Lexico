from . import AFN
from . import Analizador as Lexic
from . import AFD
from . import simbolosEspeciales as s

class Regex():
    def __init__(self):
        self.Lexic = Lexic.AnalizadorLexico()

    def initWithTable(self, sigma, AutFD):
        self.expresion = sigma
        self.Lexic = Lexic.AnalizadorLexico()
        self.Lexic.initWithTable(sigma, AutFD)

    def E(self, f):
        print("E")
        if self.T(f):
            if self.Ep(f):
                return True
        return False

    def Ep(self, f):
        print("Ep")
        f2 = AFN.AFN()
        Token = self.Lexic.yylex()
        if Token == s.Simbolos.OR:
            if self.T(f2):
                f.Unir(f2)
                if self.Ep(f):
                    return True
            return False
        self.Lexic.UndoToken()
        return True

    def T(self, f):
        print("T")
        if self.C(f):
            if self.Tp(f):
                return True
        return False

    def Tp(self, f):
        print("Tp")
        f2 = AFN.AFN()
        Token = self.Lexic.yylex()
        print("Token: ", Token)
        if Token == s.Simbolos.CONCATENACION:
            if self.C(f2):
                f.Concatenar(f2)
                if self.Tp(f):
                    return True
            return False
        self.Lexic.UndoToken()
        return True

    def C(self, f):
        print("C")
        if self.F(f):
            if self.Cp(f):
                print("Cp returneando true")
                return True
        return False

    def Cp(self, f):
        print("Cp")
        Token = self.Lexic.yylex()
        print("Token: ", Token)
        
        if Token == s.Simbolos.MAS:
            f.CerraduraPositiva()
        elif Token == s.Simbolos.POR:
            f.CerraduraKleene()
        elif Token == s.Simbolos.OPCIONAL:
            f.Opcional()
        else:
            print("UndoToken")
            self.Lexic.UndoToken()
            return True

        if self.Cp(f):
            return True
        return False

    def F(self, f):
        print("F")
        Token = self.Lexic.yylex()
        Lexema1 = None
        Lexema2 = None
        print("Token: ", Token)
        if Token == s.Simbolos.PARENTESISIZQ:
            if self.E(f):
                Token = self.Lexic.yylex()
                if Token == s.Simbolos.PARENTESISDER:
                    return True
            return False
        
        elif Token == s.Simbolos.SIMB:
            Lexema1 = self.Lexic.yytext()[1] if self.Lexic.yytext()[0] == '\\' else self.Lexic.yytext()[0]
            f.crearAFNBasicoChar(Lexema1)
            return True

        elif Token == s.Simbolos.CORCHEIZQ:
            Token = self.Lexic.yylex()
            if Token == s.Simbolos.SIMB:
                Lexema1 = self.Lexic.yytext()[1] if self.Lexic.yytext()[0] == '\\' else self.Lexic.yytext()[0]
                Token = self.Lexic.yylex()
                if Token == s.Simbolos.COMA:
                    Token = self.Lexic.yylex()
                    if Token == s.Simbolos.SIMB:
                        Lexema2 = self.Lexic.yytext()[1] if self.Lexic.yytext()[0] == '\\' else self.Lexic.yytext()[0]
                        Token = self.Lexic.yylex()
                        if Token == s.Simbolos.CORCHEDER:
                            f.crearAFNBasicoRange(Lexema1, Lexema2)
                            return True
            return False

        return False
