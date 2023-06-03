class Folha:
    def __init__(self,id):
        self.id = id
        self.prob = None
        self.filhos = []
    
    def addFilho(self,filho):
        self.filhos.append(filho)

def calculaprob(arvore):
    # caso base, nao tem filhos
    dic_status = {"V":100,"D":0,"E":0,"?":-1}
    status = arvore.id
    if dic_status.get(status) != -1:
        arvore.prob = dic_status[status]
        return
    # tem filhos
    total = 0
    filhos = 0
    for filho in arvore.filhos:
        filhos += 1
        if filho.prob == None:
            calculaprob(filho)
        total += filho.prob
    arvore.prob = (total/filhos)
    return

def gametree(arvore,nivel=0):
    espaco = ("__"*nivel)
    print(f"{espaco}{arvore.id}")
    for filho in arvore.filhos:
        gametree(filho,nivel+1)

def probtree(arvore,nivel=0):
    espaco = (".."*nivel)
    prob = arvore.prob
    print(f"{espaco}{arvore.id} ({prob:.2f}%)")
    for filho in arvore.filhos:
        probtree(filho,nivel+1)

fila = []
# Construindo a raiz:
comando = input().split()
if len(comando) == 2:
    raiz = Folha(comando[0])
    filhos = int(comando[1])
    fila.append((raiz,filhos))
    # Construindo o restante da arvore
    while len(fila) > 0:
        atual = fila.pop(0)
        folha_atual = atual[0]
        # criando filhos
        for _ in range(atual[1]):
            comando = input().split()
            sub_folha = Folha(comando[0])
            sub_filhos = int(comando[1])
            fila.append((sub_folha,sub_filhos))
            folha_atual.addFilho(sub_folha)
    # Pegando o comando final -> gametree ou probtree
    comando = input()
    if comando == "gametree":
        gametree(raiz)
    else:
        calculaprob(raiz)
        probtree(raiz)
else:
    print()
