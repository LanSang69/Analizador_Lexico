from . import Analizador
from . import AFD
from . import simbolosEspeciales as s

class EvaluadorExpr:
    def __init__(self):
        self.expresion = ""
        self.result = 0.0
        self.ExprPost = ""
        self.Analizador = None
    
    def __eq__(self, other):
        if isinstance(other, EvaluadorExpr):
            return (self.expresion == other.expresion and
                    self.result == other.result and
                    self.postfix == other.postfix and
                    self.Analizador == other.Analizador)
        return False
    
    def __hash__(self):
        return hash((self.expresion, self.result, self.postfix, self.Analizador))
    
    def initWithTable(self, sigma, AutFD):
        self.expresion = sigma
        self.Analizador = Analizador.AnalizadorLexico()
        self.Analizador.initWithTable(sigma, AutFD)

    def initWithStringAFD(self, sigma, stringAFD, idAFD):
        self.expresion = sigma
        aux = AFD.AFD()
        aux.leerString(stringAFD)
        self.Analizador = Analizador.AnalizadorLexico()
        self.Analizador.init(sigma, aux, idAFD)

    def initNoSigma(self, stringAFD, idAFD):
        aux = AFD.AFD()
        aux.leerString(stringAFD)
        self.Analizador = Analizador.AnalizadorLexico()
        self.Analizador.initNoSigma(aux, idAFD)

    def setExpresion(self, sigma):
        self.expresion = sigma
    
    def iniEval(self) -> bool:
        print("Iniciando evaluacion")
        token = None
        v = [0.0]
        postfijo = [""]

        if self.E(v, postfijo):
            token = int(self.Analizador.yylex())
            print("Token: ", token)
            print("Fin: ", s.Simbolos.FIN)
            if int(token) == s.Simbolos.FIN:
                print("Fin de la expresion")
                self.result = v[0]
                print("Resultado: ", self.result)
                self.ExprPost = postfijo[0]
                print("Postfijo: ", self.ExprPost)
                return True
        return False

    def E(self, v, postfijo) -> bool:
        print("Evaluando E")
        if self.T(v, postfijo):
            if self.Ep(v, postfijo):
                print("e returneando true")
                return True
        return False
    
    def Ep(self, v, postfijo) -> bool:
        print("Evaluando Ep")
        token = int(self.Analizador.yylex())
        print("Token: ", token)
        v2 = [0.0]
        postfijo2 = [""]
        if int(token) == 10 or int(token) == 20:
            print("operation + or -")
            if self.T(v2, postfijo2):
                v[0] = v[0] + v2[0] if int(token) == 10 else v[0] - v2[0]
                postfijo[0] = postfijo[0] + postfijo2[0] + ("+" if int(token) == 10 else "-")
                if self.Ep(v, postfijo):
                    return True
            return False
        self.Analizador.UndoToken()
        return True
    
    def T(self, v, postfijo) -> bool:
        print("Evaluando T")
        if self.F(v, postfijo):
            if self.Tp(v, postfijo):
                print("t returneando true")
                return True
        return False
    
    def Tp(self, v, postfijo) -> bool:
        print("Evaluando Tp")
        v2 = [0.0]
        postfijo2 = [""]
        token = self.Analizador.yylex()
        print("Token: ", token)
        if int(token) == 30 or int(token) == 40:
            if self.F(v2, postfijo2):
                v[0] = v[0] * v2[0] if int(token) == 30 else v[0] / v2[0]
                postfijo[0] = postfijo[0] + postfijo2[0] + ("*" if int(token) == 30 else "/")
                if self.Tp(v, postfijo):
                    return True
            return False
        self.Analizador.UndoToken()
        return True

    def F(self, v, postfijo) -> bool:
        token = int(self.Analizador.yylex())
        if int(token) == 50: #parentesis izquierdo
            if self.E(v, postfijo):
                token = self.Analizador.yylex()
                if int(token) == 60: #parentesis derecho
                    return True
            return False
        elif int(token) == 70 or int(token) == 80: #Numero
            v[0] = float(self.Analizador.Lexema)
            postfijo[0] = postfijo[0] + self.Analizador.Lexema
            return True
        return False