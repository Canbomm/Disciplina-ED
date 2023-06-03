def mostra_arvore_e_altura(raiz,espacamento=0,altura=0):
    if raiz != None:
        numraiz = raiz.dado
        print(f"{'_'*espacamento}{numraiz}")
        espacamento += 2
        if numraiz != None:
            if raiz.dir != None:
                mostra_arvore_e_altura(raiz.dir,espacamento)
            if raiz.esq != None:
                mostra_arvore_e_altura(raiz.esq,espacamento)
