def rotaciona_direita(raiz):
    if raiz == None:
        return ()
    if raiz.esq:
        pai = raiz.esq
        raiz.esq = pai.dir
        pai.dir = raiz
        return pai
    else:
        return raiz
