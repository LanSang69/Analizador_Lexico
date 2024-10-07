import AFN
import estado
import transicion
import Operations as op

count = 0
afn, afn2, afn3, afn4 = AFN.AFN(), AFN.AFN(), AFN.AFN(), AFN.AFN()
afn.crearAFNBasicoChar('a')
afn2.crearAFNBasicoChar('b')
afn3.crearAFNBasicoRange('c', 'f')
afn.CerraduraKleene()


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
print("")

# for e in Sj:
#     print(e)
new = queue
while len(queue) > 0:
    top = queue.pop(0)
    print(top.movimientos)
    for i in range(1,len(top.movimientos)-1):
        if top.movimientos[i] != -1:
            if top.movimientos[257] != -1:
                p1 = "("
                p2 = ")"
            else:
                p1 = " "
                p2 = " "
            print("(", top.movimientos[0], ")", chr(i), "-->", p1, "(", top.movimientos[i], ")", p2)

