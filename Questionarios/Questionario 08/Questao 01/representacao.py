class Arvore():
    def __init__(self, dado):
        self.dado = dado
        self.filhos = []

def mostra(raiz,simbolo,espacamento=0):
    if raiz:
        print(f"{espacamento*simbolo}{raiz.dado}")
        espacamento += 1
        filhos = raiz.filhos
        for filho in filhos:
            mostra(filho,simbolo,espacamento)
