class Folha:
    def __init__(self,id):
        self.id = id
        self.prob = None
        self.filhos = []
    
    def addFilho(self,filho):
        self.filhos.append(filho)

def calculaProb(arvore):
    filhos = arvore.filhos
    total = len(filhos)
    ganhadores = 0
    for filho in filhos:
        if filho.id == "?":
            sub_total,sub_ganhadores = calculaProb(filho)
            # menos um pois eu desconsidero o proprio "?"
            total += (sub_total - 1)
            ganhadores += sub_ganhadores
        if filho.id == "V":
            ganhadores += 1
    if total != 0:
        arvore.prob = ganhadores/total
    else:
        arvore.prob = status[arvore.id]
    return total,ganhadores

def gametree(arvore,nivel=0):
    espaco = ("__"*nivel)
    print(f"{espaco}{arvore.id}")
    for filho in arvore.filhos:
        gametree(filho,nivel+1)

def probtree(arvore,nivel=0):
    espaco = (".."*nivel)
    prob = arvore.prob
    if prob == None:
        prob = status[arvore.id]
    print(f"{espaco}{arvore.id} ({(prob*100):.2f}%)")
    for filho in arvore.filhos:
        probtree(filho,nivel+1)

fila = []
status = {"V":1,"D":0,"E":0,"?":0}
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
        calculaProb(raiz)
        probtree(raiz)
else:
    print()
