# import AFN
# import Operations as op
# import AFD
# import Analizador as A

# count = 0
# input1 = input("Ingrese una expresion regular: ")

# afn = op.expToAFN(input1)

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
# auxAnalizador.initWithTable("babababab",auxAFD)

# # Print the table rows
# auxAFD.guardarEnString()
# with open("output.txt", "w") as f:
#     f.write("Tabla de transiciones:\n")
#     for e in auxAFD.getTablaAFD():
#         f.write(" ".join(str(m) for m in e) + "\n")

# print("yylex: ")
# print(auxAnalizador.yylex())
# print(auxAnalizador.Lexema)