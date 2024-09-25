import AFN
import estado
import transicion

afn = AFN.AFN()
afn = afn.crearAFNBasicoChar('a')
afn2 = afn.crearAFNBasicoRange('a','z')

print(afn.alphabet)
print(afn2.alphabet)