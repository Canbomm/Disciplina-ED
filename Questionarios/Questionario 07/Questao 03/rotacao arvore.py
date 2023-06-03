# nao passou em algum caso oculto
def rotaciona_direita(raiz):
    if raiz == None:
        return ()
    
    if raiz.esq:
        pai = raiz.esq
        raiz.esq = ()
        pai.dir = raiz
        raiz = pai
        return raiz

    else:
        return raiz

original = ('a', (), ('c', (), ()))
esperado = ('b', (), ('a', (), ('c', (), ())))
print(rotaciona_direita(None))
