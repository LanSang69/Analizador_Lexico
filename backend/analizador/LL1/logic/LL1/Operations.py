eps = 'ε'

def first(L, reglas):
    R = set()
    
    if L[0].terminal:
        R.add(L[0].simbolo)
        return R
    
    for regla in reglas:
        if regla.simbolo == L[0].simbolo:
            R.update(first(regla.nodos, reglas))
    
    if eps not in R:
        return R

    if len(L) == 1:
        return R

    R.discard(eps)
    L2 = L[1:]
    R.update(first(L2, reglas))
    return R

def follow(simb_no_t, reglas):
    R = set()

    if simb_no_t == reglas[0].simbolo:
        R.add("$")
    
    for i in range(len(reglas)):
        aux = reglas[i].nodos
        for j in range(len(aux)):
            if aux[j].simbolo == simb_no_t:
                if (j+1) < len(aux):
                    temp = first([aux[j+1]], reglas)
                    if eps in temp:
                        temp.discard(eps)
                        R.update(temp)
                        if str(reglas[i].simbolo) != str(simb_no_t):
                            R.update(follow(reglas[i].simbolo, reglas))
                    else:
                        R.update(temp)
                else:
                    if reglas[i].simbolo != simb_no_t:
                        R.update(follow(reglas[i].simbolo, reglas))
    return R        