# entendi errado a questao
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

tamanho = int(input())
grafo = Grafo()
for _ in range(tamanho):
    vertice,arestas,*conexoes = input().split()
    grafo.addBola(vertice,conexoes)

# pegando os amigos
amigos_atuais = grafo.vertices["Mussum"].vizinhos
novos_amigos = []
for atual_amigo in amigos_atuais:
    amigos = grafo.vertices[atual_amigo].vizinhos
    for amigo in amigos:
        if amigo != "Mussum":
            if (not (amigo in amigos_atuais)) and (not (amigo in novos_amigos)):
                novos_amigos.append(amigo)

# printando
if novos_amigos:
    novos_amigos.sort()
    for amigo in novos_amigos:
        print(amigo)
else:
    print("Cacildis! Cade elis?")
