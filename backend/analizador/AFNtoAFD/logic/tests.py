import AFN
import Operations as op
import AFD
import Analizador as A

# count = 0
# afn, afn2, afn3, afn4 = AFN.AFN(), AFN.AFN(), AFN.AFN(), AFN.AFN()
# afn.crearAFNBasicoChar('a')
# afn2.crearAFNBasicoChar('b')
# afn3.crearAFNBasicoRange('c',"z")
# afn.Unir(afn3)

# for e in afn.edosAFN:
#    count += 1
#    e.idEdo = count

# print("inicial: ", afn.edoInicial.idEdo)
# for e in afn.edosAcept:
#     print("Aceptacion: ", e.idEdo)
# for element in afn.edosAFN:
#     for t in element.transiciones:
#         print(element.idEdo, "(", t.simboloInf, "-" , t.simboloSup, ")","-->",t.edoDestino.idEdo)
# Sj, queue = afn.EstadoSi()

# auxAFD = AFD.AFD()
# auxAFD.initTabla(queue)
# auxAnalizador = A.AnalizadorLexico()
# auxAnalizador.initWithTable("ababababab",auxAFD)

# for i in range(257):
#     if i > 47:
#         print(chr(i), end='\t')
#     else:
#         print("-1", end='\t')
# # Print the table rows
# auxAFD.guardarEnString()
# print(auxAFD.archivo)

# # print("yylex: ")
# # print(auxAnalizador.yylex())
count = 0
input1 = input("Ingrese una expresion regular: ")

afn = op.expToAFN(input1)