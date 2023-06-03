# entendi errado dnv a questao
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

def addAmigos(listaog,amigosdeamigos,sugestao):
    for atual in listaog:
        if atual in amigosdeamigos:
            amigosdeamigos.remove(atual)
    for possivel in amigosdeamigos:
        if not (possivel in sugestao):
            sugestao.append(possivel)
    return sugestao

tamanho = int(input())
grafo = Grafo()
for _ in range(tamanho):
    vertice,arestas,*conexoes = input().split()
    grafo.addBola(vertice,conexoes)

print("\n\n\n")
# pegando os amigos
amigos_atuais = grafo.vertices["Mussum"].vizinhos
print(f"Amigos do Mussum: {amigos_atuais}")
novos_amigos = []
for atual_amigo in amigos_atuais:
    amigos = grafo.vertices[atual_amigo].vizinhos
    print(f"Amigos do {atual_amigo}: {amigos}")
    mesmos_amigos = 0
    for amigo in amigos:
        if amigo in amigos_atuais:
            mesmos_amigos += 1
        if mesmos_amigos == 2:
            novos_amigos = addAmigos(amigos_atuais,amigos,novos_amigos)
            break

print("\n\n\n")
# printando as sugestoes
novos_amigos.remove("Mussum")
for amigo in novos_amigos:
    amigos = grafo.vertices[amigo].vizinhos
    print(f"Amigos do {amigo}: {amigos}")

print("\n\n\n")
if novos_amigos:
    novos_amigos.sort()
    for amigo in novos_amigos:
        print(amigo)
else:
    print("Cacildis! Cade elis?")
