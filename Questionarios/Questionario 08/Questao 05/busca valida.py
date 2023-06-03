class ArvoreBinaria():
    def __init__(self, dado, esq = None, dir = None):
        self.dado = dado
        self.esq = esq
        self.dir = dir

def constituiArvoreBinariaDeBusca(raiz):
    if raiz:
        if raiz.esq:
            dadoesq = raiz.esq.dado
            if dadoesq > raiz.dado or not constituiArvoreBinariaDeBusca(raiz.esq):
                return False
        if raiz.dir:
            dadodir = raiz.dir.dado
            if dadodir < raiz.dado or not constituiArvoreBinariaDeBusca(raiz.dir):
                return False
        return True
    else:
        return True

#raiz = ArvoreBinaria(1,ArvoreBinaria(0,ArvoreBinaria(-1),ArvoreBinaria(3)),ArvoreBinaria(2))
#print(constituiArvoreBinariaDeBusca(raiz))
