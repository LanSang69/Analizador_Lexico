from ..lexico import Analizador as A
from ..lexico import AFN
from ..lexico import AFD
from ..lexico import Operations as op
from ..lexico import simbolosEspeciales as s
from . import gGramaticas as G
from . import ItemLR0
from . import LR0_Conj_Sj 
from . import Inf_IrA
from . import Nodo
from . import Operations as Op
import os

class LR0:
    def __init__(self):
        self.ResultIrA:Inf_IrA = []  
        self.idAutGram: int = 0
        self.DescRecG = G.GramaticaGramaticas()  
        self.NumRenglonesIrA: int = 0
        self.NumRenglonesTabla: int = 0
        self.LexGram = A.AnalizadorLexico()
        self.Gram: str = ""
        self.Sigma: str = ""
        self.TablaLR0 = [{}]
        self.Vt  = [] 
        self.Vn = []
        self.V = []
        self.ArchAFDLexiGramGram: str = ""
    
    def init(self, DescRecG):
        self.DescRecG = DescRecG

    def crearTablaLR0(self):
        #All Sj's
        C = set()
        
        #Sets Sj
        ConjSJ: LR0_Conj_Sj = LR0_Conj_Sj.LR0ConjSj()
        ConjSJAux: LR0_Conj_Sj = LR0_Conj_Sj.LR0ConjSj()

        #Temporal set of items
        ConjItems = set()

        #Temporarily save IrA result
        SjAux = set()

        #Left im queue
        Q = []

        V = []
        
        for simb in self.DescRecG.Vn:
            self.Vn.append(simb)
            V.append(simb)
        for simb in self.DescRecG.Vt:
            self.Vt.append(simb)
            V.append(simb)

        self.Vt.append("$")
        self.V = V

        ResultIrA = []
        itemAux = ItemLR0.ItemLR0()
        itemAux.init(0,0)
        ConjItems.add(itemAux)
        j = 0
        ConjSJ.Sj = self.Cerradura(ConjItems) #cerradura S0
        ConjSJ.j = j
        C.add(ConjSJ)
        Q.append(ConjSJ)

        self.NumRenglonesIrA = 0
        self.ResultIrA.append(Inf_IrA.InfoIrA())
        self.ResultIrA[self.NumRenglonesIrA].Si = 0
        self.ResultIrA[self.NumRenglonesIrA].IrA_Sj = -1
        self.ResultIrA[self.NumRenglonesIrA].IrA_Simbolo = ""
        self.ResultIrA[self.NumRenglonesIrA].ConjuntoItems = self.ObtenerCadenaItems(ConjSJ.Sj)
        self.NumRenglonesIrA += 1

        j+=1

        while(len(Q) > 0):
            ConjSJ = Q.pop(0)
            for simb in V:
                SjAux = self.IrA(ConjSJ.Sj, simb)
                if len(SjAux) == 0:
                    continue
                existe = False

                for ElemSj in C:
                    if len(ElemSj.Sj) == len(SjAux):
                        if ElemSj.Sj == SjAux:
                            existe = True
                            self.ResultIrA.append(Inf_IrA.InfoIrA())
                            self.ResultIrA[self.NumRenglonesIrA].Si = ElemSj.j
                            self.ResultIrA[self.NumRenglonesIrA].IrA_Sj = ConjSJ.j
                            self.ResultIrA[self.NumRenglonesIrA].IrA_Simbolo = simb
                            self.ResultIrA[self.NumRenglonesIrA].ConjuntoItems = self.ObtenerCadenaItems(ConjSJ.Sj)
                            self.ResultIrA[self.NumRenglonesIrA].existe = True
                            self.NumRenglonesIrA += 1
                            break
                
                if existe == False:
                    self.NumRenglonesTabla +=1
                    nuevoConjSJ = LR0_Conj_Sj.LR0ConjSj()
                    nuevoConjSJ.Sj = SjAux
                    nuevoConjSJ.j = j

                    self.ResultIrA.append(Inf_IrA.InfoIrA())
                    self.ResultIrA[self.NumRenglonesIrA].Si = j
                    self.ResultIrA[self.NumRenglonesIrA].IrA_Sj = ConjSJ.j
                    self.ResultIrA[self.NumRenglonesIrA].IrA_Simbolo = simb
                    self.ResultIrA[self.NumRenglonesIrA].ConjuntoItems = self.ObtenerCadenaItems(SjAux)
                    self.NumRenglonesIrA += 1
                    j += 1

                    C.add(nuevoConjSJ)
                    Q.append(nuevoConjSJ)

        
    def Mover(self, C, Simbolo):
        R = set()
        Aux = ItemLR0.ItemLR0()
        N = Nodo.Nodo("",False)

        Lista = list()
        for I in C:
            Lista = self.DescRecG.ReglasG[I.NumRegla].nodos
            if I.PosPunto < len(Lista):
                N = Lista[I.PosPunto]
                if N.simbolo == Simbolo:
                    Aux = ItemLR0.ItemLR0()
                    Aux.init(I.NumRegla, I.PosPunto+1)
                    R.add(Aux)
        return R
    
    def Cerradura(self, C):
        R = set()
        Temporal = set()
        Aux = ItemLR0.ItemLR0()
        Lista = list()
        N = Nodo.Nodo("",False)

        if len(C) == 0:
            return R

        R = R.union(C) #union d R y C

        for I in C:
            Lista = self.DescRecG.ReglasG[I.NumRegla].nodos
            if I.PosPunto < len(Lista):
                N = Lista[I.PosPunto]
                if N.terminal == False:
                    for i in range(self.DescRecG.NumReglas):
                        if self.DescRecG.ReglasG[i].simbolo == N.simbolo:
                            Aux = ItemLR0.ItemLR0()
                            Aux.init(i,0)
                            if self.C_Contiene(R, Aux) == False:
                                Temporal.add(Aux)
        R = R.union(self.Cerradura(Temporal))
        return R

    def C_Contiene(self, C, Aux):
        for I in C:
            if I.NumRegla == Aux.NumRegla and I.PosPunto == Aux.PosPunto:
                return True
        return False

    def IrA(self, C, Simbolo):
        return self.Cerradura(self.Mover(C, Simbolo))
    
    def ObtenerCadenaItems(self, C):
        R = ""
        Item_string = ""
        Lista = list()

        if len(C) == 0:
            return R
        
        for I in C:
            Item_string = self.DescRecG.ReglasG[I.NumRegla].simbolo + " -> "
            Lista = self.DescRecG.ReglasG[I.NumRegla].nodos

            for i in range(len(Lista)):
                if i == I.PosPunto:
                    Item_string += "."
                Item_string += Lista[i].simbolo
            
            if I.PosPunto == len(Lista):
                Item_string += "."

            R = R + Item_string + " , "
        R = R[:-2]
        
        return R

    def imprimirAnalisis(self):
        result = []
        for e in self.ResultIrA:
            if e.IrA_Sj < 0:
                aux = f"S{e.Si} = {e.ConjuntoItems}"
            else:
                if not e.existe:
                    aux = f"IrA( S{e.IrA_Sj}, \"{e.IrA_Simbolo}\" ) = {e.ConjuntoItems} = S{e.Si}"
                else:
                    aux = f"IrA( S{e.IrA_Sj}, \"{e.IrA_Simbolo}\" ) = S{e.Si}"
            result.append(aux)
        return result

    
    def setEmpty(self):
        for i in range(self.NumRenglonesTabla):
            self.TablaLR0.append({})
            for e in self.V:
                self.TablaLR0[i][e] = ""
    
    def generarTabla(self):
        self.setEmpty()
        self.setRules()
        for e in self.ResultIrA:
            if e.IrA_Sj >= 0:
                if e.IrA_Simbolo in self.Vn:
                    self.TablaLR0[e.IrA_Sj][e.IrA_Simbolo] = e.Si
                else:
                    self.TablaLR0[e.IrA_Sj][e.IrA_Simbolo] = "d" + str(e.Si)
    
    def setRules(self):
        print("in setting rules")
        for e in self.ResultIrA:
            if not e.existe:
                aux = e.ConjuntoItems.replace(" ", "").split(",")
                print("aux: ", aux)
                for item in aux:
                    if item.endswith('.'):
                        print("item: ", item)
                        icon = item.split('->')[0]
                        right = item.split('->')[1].replace(".", "")
                        print("icon: ", icon)
                        print("right: ", right)
                        ruleIndex = self.getRuleIndex(icon, right)
                        items = Op.follow(icon, self.DescRecG.ReglasG)
                        for i in items:
                            if ruleIndex != 0 or i != str("$"):
                                self.TablaLR0[e.Si][i] = "r" + str(ruleIndex)
                            else:
                                self.TablaLR0[e.Si][i] = "Aceptar"

    def getRuleIndex(self, left, right):
        print()
        print("searching index")
        print()
        reglas = self.DescRecG.ReglasG
        for i in range(len(reglas)):
           if str(reglas[i].simbolo) == str(left):
                if "".join([str(n.simbolo) for n in reglas[i].nodos]) == right:
                    return i
        return -1


    def printTabla(self):
        for i in range(self.NumRenglonesIrA):
            for e in self.V:
                print(self.TablaLR0[i][e], end=" ")
            print()


    def initTable(self):
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        print(base_dir)
        file_path = os.path.join(base_dir, 'LL1', 'todo.txt')

        with open(file_path, 'r') as file:
            table = file.read()


        afd = AFD.AFD()
        afd.leerString(table)
        return afd
    
    def generarLexico(self, sigma):
        afd = self.initTable()

        analisis = A.AnalizadorLexico()
        analisis.initWithTable(sigma, afd)
        self.LexGram = analisis
        auxS = ""
        while True:
            token = analisis.yylex()
            if token == s.Simbolos.FIN:
                break  
            auxS = auxS + " ".join([str(analisis.Lexema), "\t", str(token), "\n"])
        print(auxS)
        return auxS

    def analizarSigma(self,sigma, matrix):
        print("in analizar sigma")
        print(sigma)
        print(matrix)
        tabla = []
        pilaT = []
        cadenaT = []
        destinoT = []
        cadena = []

        afd = self.initTable()

        analisis = A.AnalizadorLexico()
        analisis.initWithTable(sigma, afd)
        self.LexGram = analisis

        while True:
            token = self.LexGram.yylex()
            if token == s.Simbolos.FIN:
                break  
            cadena.append(matrix[token])
        print("cadena: ", cadena)

        pila = ["0"]
        previous = []
        while len(cadena) > 0:
            cadenaT.append("".join(cadena))
            pilaT.append("".join(pila))

            previous = cadena[:]
            element = cadena.pop(0)
            print("element: ", element)
            print("pila[-1]: ", pila[-1])
            print("tabla", self.TablaLR0)
            destino = self.TablaLR0[int(pila[-1])][element]

            destinoT.append(destino)


            if destino == "":
                return False, None
            elif destino == "Aceptar":
                tabla.append(pilaT)
                tabla.append(cadenaT)
                tabla.append(destinoT)
                return True, tabla
            elif destino[0] == "d":
                pila.append(element)
                pila.append(str(destino[1:]))
                print("pila:", pila)
            elif destino[0] == "r":
                cadena = previous
                left = self.DescRecG.ReglasG[int(destino[1:])].simbolo
                for _ in range(len(self.DescRecG.ReglasG[int(destino[1:])].nodos) * 2):
                    pila.pop()
                destinoAux = self.TablaLR0[int(pila[-1])][left]
                pila.append(left)
                pila.append(str(destinoAux))