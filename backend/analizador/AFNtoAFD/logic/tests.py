import AFN
import estado
import transicion

count = 0
afn, afn2, afn3 = AFN.AFN(), AFN.AFN(), AFN.AFN()
afn = afn.crearAFNBasicoChar('a')
afn2 = afn2.crearAFNBasicoChar('b')
afn3 = afn3.crearAFNBasicoChar('c')
afn = afn.Concatenar(afn, afn3)
afn = afn.CerraduraPositiva(afn)

count = 0
for e in afn.edosAFN:
    count = count + 1
    e.id_edo = count

print("Estado incial: ", afn.edoInicial.id_edo)
for e in afn.edosAcept:
    print("Estado aceptacion: ", e.id_edo) 
for e in afn.edosAFN:
    for t in e.transiciones:
        print('Estado: ', e.id_edo, 'SimboloInf: ', t.simboloInf, 'SimboloSup: ', t.simboloSup, 'EdoDestino: ', t.edoDestino.id_edo)