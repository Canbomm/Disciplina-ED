class Grafo:
    def __init__(self):
        self.vertices = {}
    
    def addBola(self,valor,lista):
        self.vertices[valor] = Vertice(valor)
        for vizinho in lista:
            self.vertices[valor].addVizinho(vizinho)
    
    def __str__(self):
        chaves = self.vertices.keys()
        print(f"Esses são os vertices: {chaves}\nConexoes:")
        for chave in chaves:
            print(f"Vertice: {chave}, Conexoes: {self.vertices[chave].vizinhos}")
        return ""

class Vertice:
    def __init__(self,valor):
        self.pai = valor
        self.vizinhos = []
    
    def addVizinho(self,vizinho):
        self.vizinhos.append(vizinho)

# Pegando a entrada e formando o grafo
tamanho = int(input())
grafo = Grafo()
for _ in range(tamanho):
    vertice,arestas,*conexoes = input().split()
    grafo.addBola(vertice,conexoes)

# Comecando o processo de encontrar os amigo
# pegando todo mundo (menos o Mussum)
geral = list(grafo.vertices.keys())
geral.remove("Mussum")
# pegando os amigos atuais do Mussum
amigos_atuais = grafo.vertices["Mussum"].vizinhos
novos_amigos = []
# procurando possiveis amigos
for amigo in geral:
    if not (amigo in amigos_atuais):
        # achei alguem que nao e amigo dele
        # vou verificar se tem pelo menos 3 conexoes
        amigos = grafo.vertices[amigo].vizinhos
        conexoes = 0
        for poss_amigo in amigos:
            if poss_amigo in amigos_atuais:
                conexoes += 1
            if conexoes == 3:
                novos_amigos.append(amigo)
                break

# Printando o resultado final
if novos_amigos:
    novos_amigos.sort()
    for amigo in novos_amigos:
        print(amigo)
else:
    print("Cacildis! Cade elis?")
