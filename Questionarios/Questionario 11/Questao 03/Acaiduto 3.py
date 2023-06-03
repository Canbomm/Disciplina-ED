class Grafo:
    def __init__(self):
        self.vertices = {}
    
    def addVertice(self,valor):
        self.vertices[valor] = Vertice(valor)
    
    def removeVertice(self,valor):
        if self.vertices.get(valor):
            self.vertices.pop(valor)
    
    def addAresta(self,vert1,vert2,peso):
        if self.vertices.get(vert1) != None:
            self.vertices[vert1].addConexao(vert2,peso)
    
    def remAresta(self,vert1,vert2):
        if self.vertices.get(vert1) != None:
            if vert2 in self.vertices[vert1].conexoes:
                self.vertices[vert1].remConexao(vert2)

    def __str__(self):
        saida = ""
        vertices = list(self.vertices.keys())
        for vertice in vertices:
            saida += f"Conexoes de {vertice}: {self.vertices[vertice].conexoes}\n"
        return saida

class Vertice:
    def __init__(self,valor):
        self.id = valor
        self.conexoes = {}
        self.cor = 0
        self.dist = 0
        self.anterior = None
        # 0 = branco
        # 1 = cinza
        # 2 = preto
    
    def addConexao(self,vert2,peso=0):
        self.conexoes[vert2] = peso
    
    def remConexao(self,vert2):
        self.conexoes.pop(vert2)

# pegando a entrada
grafo = Grafo()
for i in range(int(input())):
    cmd = input().split()
    vertice = cmd[0]
    conexoes = cmd[2:]
    # criando o grafo
    grafo.addVertice(vertice)
    for ind in range(0,len(conexoes)-1,2):
        grafo.addAresta(vertice,conexoes[ind+1],conexoes[ind])

# pegando a maior distancia
print(grafo)
