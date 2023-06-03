def mostra(raiz):
    # criando funcao que edita a lista
    def filhos(raiz):
        if raiz:
            tupla = ((raiz.dado),(filhos(raiz.esq)),(filhos(raiz.dir)))
            return tupla
        else:
            return ()

    # chamando a funcao que faz a tupla
    arvore = filhos(raiz)
    # tratando a arvore para printar do jeito desejado
    arvore_str = str(arvore)
    arvore_str = arvore_str.replace(',','')
    print(arvore_str)
