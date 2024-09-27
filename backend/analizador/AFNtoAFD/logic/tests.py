import AFN
import estado
import transicion

count = 0
afn, afn2 = AFN.AFN(), AFN.AFN()
afn, count = afn.crearAFNBasicoChar('a', count)
afn2, count = afn2.crearAFNBasicoChar('b', count)

afn = afn.Unir(afn, afn2)

for a in afn.edosAFN:
    print('Estado: ', a._idEdo)
    for t in a.transiciones:
        print("Transicion desde el estado", a._idEdo, "con el símbolo", t.simboloInf,"-",t.simboloSup, "hacia el estado", t.edoDestino._idEdo)