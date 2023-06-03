# esse script nao funciona

def mostra_nivel(raiz,nivel):
    # criando funcao que edita a lista
    def filhos(raiz):
        if raiz:
            tupla = ((raiz.dado),(filhos(raiz.esq)),(filhos(raiz.dir)))
            return tupla
        else:
            return ()

    # funcao que trata a raiz
    def trata(tupla):
        tupla_str = str(tupla)
        tupla_str = tupla_str.replace(',','')
        return tupla_str
    
    # chamando a funcao que faz a tupla
    filho_dir = raiz.dir
    filho_esq = raiz.esq
    atual = 0
    while atual < nivel:
        if filho_dir.dir:
            filho_dir = filho_dir.dir
        if filho_esq.esq:
            filho_esq = filho_esq.esq    
        atual += 1
    
    esquerda = filhos(filho_esq)
    direita = filhos(filho_dir)
    print(trata(esquerda))
    print(trata(direita))
 

arvore_teste = (4, (2, (1, (0, (), ()), ()), (3, (), ())), (5, (), (6, (), ())))

'''
(1 (0 () ()) ())
(3 () ())
(6 () ())
'''
