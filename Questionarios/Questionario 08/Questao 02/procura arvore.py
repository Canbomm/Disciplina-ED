def nivel(raiz,dado,level=0):
    if raiz:
        if raiz.dado == dado:
            return level
        else:
            if raiz.esq:
                sub_nivel = nivel(raiz.esq,dado,level+1)
                if sub_nivel != -1:
                    return sub_nivel
            if raiz.dir:
                return nivel(raiz.dir,dado,level+1)
            return -1
    else:
        return -1
