# esse código não funciona e eu não sei bem o que fazer com esse input
class ArvoreBinaria():
    def __init__(self, dado, pai = None, esq = None, dir = None):
        self.pai = pai
        self.dado = dado
        self.esq = esq
        self.dir = dir

def printaArvore(arvore):
    print("Essa é a árvore:")
    print(filhos(arvore))
    print()

def filhos(raiz):
    if raiz:
        tupla = ((raiz.dado),(filhos(raiz.esq)),(filhos(raiz.dir)))
        return tupla
    else:
        return ()

def transformaArvore(arvore_str):
    print(f"Recebi: {arvore_str}")
    if arvore_str[0] == ")":
        return None, arvore_str[1:]
    
    tempArvore = ArvoreBinaria(arvore_str[0])
    arvore_str = arvore_str[1:]
    index = 0
    esquerda = True
    while index < len(arvore_str):
        #printaArvore(tempArvore)
        char = arvore_str[index]
        if esquerda:
            tempArvore.esq, arvore_str = transformaArvore(arvore_str[index+1:])
            index = 0
        else:
            tempArvore.dir, arvore_str = transformaArvore(arvore_str[index+1:])
            index = 0
        if not esquerda:
            return tempArvore, arvore_str
        if char == ")":
            esquerda = False
        index += 1

#arvore_str = input().replace(" ","")[1:-1]
arvore_str = "a(b()())(c()())"
arvore = transformaArvore(arvore_str)
printaArvore(arvore)
