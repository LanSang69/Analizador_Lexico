import AFD
import simbolosEspeciales as s

class AnalizadorLexico:
    def __init__(self) -> None:
        self.token = -1
        self.EdoActual = None
        self.EdoTransicion = None
        self.CadenaSigma = ""
        self.Lexema = ""
        self.PasoPorEdoAcept = False
        self.InitLexema = -1
        self.FinLexema = -1
        self.IndiceCracterActual = -1
        self.CaracterActual = ""
        self.Pila = []
        self.AutomataFD = None

    def init(self, sigma, fileAFD, idAFD) -> None :
        self.AutomataFD = AFD.AFD()
        self.CadenaSigma = sigma
        self.PasoPorEdoAcept = False
        self.InitLexema = 0
        self.FinLexema = -1
        self.IndiceCaracterActual = 0
        self.Pila.clear()
        self.AutomataFD.LeerAFDArchivo(fileAFD, idAFD)

    def initNoId(self, sigma, fileAFD) -> None :
        self.AutomataFD = AFD.AFD()
        self.CadenaSigma = sigma
        self.PasoPorEdoAcept = False
        self.InitLexema = 0
        self.FinLexema = -1
        self.IndiceCaracterActual = 0
        self.Pila.clear()
        self.AutomataFD.LeerAFDArchivo(fileAFD, -1)
    
    def initNoSigma(self, fileAFD, idAFD) -> None:
        self.AutomataFD = AFD.AFD()
        self.CadenaSigma = ""
        self.PasoPorEdoAcept = False
        self.InitLexema = 0
        self.FinLexema = -1
        self.IndiceCaracterActual = 0
        self.Pila.clear()
        self.AutomataFD.LeerAFDArchivo(fileAFD, idAFD)

    def initWithTable(self, sigma, AutFD) -> None :
        self.AutomataFD = AFD.AFD()
        self.CadenaSigma = sigma
        self.PasoPorEdoAcept = False
        self.InitLexema = 0
        self.FinLexema = -1
        self.IndiceCaracterActual = 0
        self.Pila.clear()
        self.AutomataFD = AutFD

    class estadoAnalizis:
        def __init__(self) -> None:
            self.token = -1
            self.EdoActual = None
            self.EdoTransicion = None
            self.Lexema = ""
            self.PasoPorEdoAcept = False
            self.InitLexema = -1
            self.FinLexema = -1
            self.IndiceCracterActual = -1
            self.CaracterActual = ""
            self.Pila = []
        
    def getEstatus(self) -> None:
        EdoActual = AnalizadorLexico.estadoAnalizis()
        EdoActual.token = self.token
        EdoActual.EdoActual = self.EdoActual
        EdoActual.EdoTransicion = self.EdoTransicion
        EdoActual.Lexema = self.Lexema
        EdoActual.PasoPorEdoAcept = self.PasoPorEdoAcept
        EdoActual.InitLexema = self.InitLexema
        EdoActual.FinLexema = self.FinLexema
        EdoActual.IndiceCracterActual = self.IndiceCracterActual
        EdoActual.CaracterActual = self.CaracterActual
        EdoActual.Pila = list(self.Pila)
        return EdoActual
        
    def setEstatus(self, e) -> bool: #receives an estadoAnalisis instance
        self.token = e.token
        self.EdoActual = e.EdoActual
        self.EdoTransicion = e.EdoTransicion
        self.Lexema = e.Lexema
        self.PasoPorEdoAcept = e.PasoPorEdoAcept
        self.InitLexema = e.InitLexema
        self.FinLexema = e.FinLexema
        self.IndiceCracterActual = e.IndiceCracterActual
        self.CaracterActual = e.CaracterActual
        self.Pila = list(e.Pila)
        return True

    def setSigma(self, sigma) -> None:
        self.CadenaSigma = sigma
        self.PasoPorEdoAcept = False
        self.InitLexema = 0
        self.FinLexema = -1
        self.IndiceCaracterActual = 0
        self.token = -1
        self.Pila.clear()

    # def cadenaXanalizar

    def yylex(self) -> int: 
        while True:
            self.Pila.append(self.IndiceCracterActual)

            if self.IndiceCaracterActual >= len(self.CadenaSigma):
                self.Lexema = ""
                return s.Simbolos.FIN
            
            self.InitLexema = self.IndiceCaracterActual
            self.EdoActual = 1
            self.PasoPorEdoAcept = False
            self.FinLexema = -1
            self.token = -1

            while self.IndiceCaracterActual < len(self.CadenaSigma):
                self.CaracterActual = self.CadenaSigma[self.IndiceCaracterActual]
                # print(self.CadenaSigma[self.IndiceCaracterActual])
                self.EdoTransicion = self.AutomataFD.tablaAFD[self.EdoActual][ord(self.CaracterActual)]
                # print("transicion: ",self.EdoActual, self.EdoTransicion)
                if self.EdoTransicion != -1:
                    if self.AutomataFD.tablaAFD[self.EdoTransicion][257] != -1:
                        self.PasoPorEdoAcept = True
                        self.token = self.AutomataFD.tablaAFD[self.EdoTransicion][257]
                        # print("token: ", self.token)
                        self.FinLexema = self.IndiceCaracterActual
                    self.IndiceCaracterActual+=1
                    # print("indice: ", self.IndiceCaracterActual)
                    self.EdoActual = self.EdoTransicion
                    continue
                break

            if not self.PasoPorEdoAcept:
                self.IndiceCaracterActual = self.InitLexema + 1
                self.Lexema = self.CadenaSigma[self.InitLexema]
                self.token = s.Simbolos.ERROR #Manejar el simbolo especial de error
                return self.token
            
            self.Lexema = self.CadenaSigma[self.InitLexema:self.FinLexema + 1]
            self.IndiceCaracterActual = self.FinLexema + 1

            if self.token == s.Simbolos.OMITIR: #Handle the number for Omitir
                continue
            else:
                return self.token
    
    def UndoToken(self) -> None:
        if len(self.Pila) == 0:
            return False
        self.IndiceCaracterActual = self.Pila.pop()
        return True