def verificaSimetria(raiz):
    # verifica se ta espalhado
    def espelhada(direita,esquerda):
        if direita and esquerda:
            dado_direita = direita.dado
            dado_esquerda = esquerda.dado
            if dado_esquerda != dado_direita:
                return False
            simetria_dir = espelhada(direita.esq,esquerda.dir)
            simetria_esq = espelhada(direita.dir,esquerda.esq)
            if simetria_dir and simetria_esq:
                return True
            else:
                return False
        else:
            if (not direita and esquerda) or (not esquerda and direita):
                return False
            else:
                return True
    
    # caso base
    if raiz:
        return espelhada(raiz.dir,raiz.esq)
    else:
        return True
