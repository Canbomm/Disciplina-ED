def mostra_arvore_e_altura(raiz):
    # definindo uma lista de alturas
    alturas = [0]

    # criando a funcao que percorre e imprime os galhos
    def imprimeAltura(raiz,espacamento=0):
        if raiz:
            print(f"{'_'*espacamento}{raiz.dado}")
            espacamento += 2
            imprimeAltura(raiz.dir,espacamento)
            imprimeAltura(raiz.esq,espacamento)
        else:
            # atualizando o alturas
            alturas.append(int((espacamento / 2) - 1))
    
    # chamando a funcao
    imprimeAltura(raiz)

    # printando a maior altura
    print(f"\naltura: {max(alturas)}")
