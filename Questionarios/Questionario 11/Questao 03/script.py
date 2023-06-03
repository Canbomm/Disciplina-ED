class Grafo:
    def __init__(self):
        self.vertices = {}

    def addVertice(self,valor):
        self.vertices[valor] = Vertice(valor)
    
    def addAresta(self,origem,conexao,peso=0):
        if self.vertices.get(origem) != None:
            self.vertices[origem].addConexao(conexao,peso)
    
    def nao_dijkstra(self,origem):
        fila = []
        visitados = []
        fila.append(origem)
        visitados.append(origem)
        origem.dist = 0
        while fila:
            atual = fila.pop(0)
            for conec in atual.conexoes:
                if not (conec in fila):
                    if not (self.vertices[conec] in visitados):
                        fila.append(self.vertices[conec])
                        nova_dist = int(atual.conexoes[conec]) + atual.dist
                        if nova_dist > self.vertices[conec].dist:
                            self.vertices[conec].dist = nova_dist
            visitados.append(atual)
        return visitados

    def __str__(self):
        saida = ""
        for vertice in self.vertices:
            saida += f"{vertice} - {self.vertices[vertice].conexoes}\n"
        return saida

class Vertice:
    def __init__(self,valor,dist=-1):
        self.id = valor
        self.dist = dist
        self.conexoes = {}
    
    def addConexao(self,conexao,peso=0):
        self.conexoes[conexao] = peso

grafo = Grafo()
for cmd in range(int(input())):
    cmd = input().split()
    vertice = cmd[0]
    conexoes = cmd[2:]
    # criando o grafo
    grafo.addVertice(vertice)
    for ind in range(0,len(conexoes)-1,2):
        grafo.addAresta(vertice,conexoes[ind+1],conexoes[ind])
print(grafo)

ordem = grafo.nao_dijkstra(grafo.vertices["1"])

# printando os visitados
for ent in ordem:
    print(ent.dist)
