def mostra_nivel(raiz, nivel):
    # funcao que pega a raiz no nivel especifico e imprime
    def pega_nivel(raiz,nivel):
        if raiz:
            if nivel > 0:
                mostra_nivel(raiz.esq,nivel-1)
                mostra_nivel(raiz.dir,nivel-1)
            else:
                print(trata(filhos(raiz)))

    # funcao que transforma a raiz do jeito que ele quer
    def filhos(raiz):
        if raiz:
            tupla = ((raiz.dado),(filhos(raiz.esq)),(filhos(raiz.dir)))
            return tupla
        else:
            return ()
    
    # funcao que trata o print pro jeito que ele quer
    def trata(tupla):
        tupla_str = str(tupla)
        tupla_str = tupla_str.replace(',','')
        return tupla_str
    
    # chamando a funcao
    pega_nivel(raiz,nivel)
