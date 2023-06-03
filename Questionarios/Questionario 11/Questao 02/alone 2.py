class Grafo:
    def __init__(self):
        self.vertices = {}
    
    def addVertice(self,valor):
        self.vertices[valor] = Vertice(valor)
    
    def remVertice(self,valor):
        if self.vertices.get(valor) != None:
            self.vertices.pop(valor)
        # removendo conexoes
        for vertice in self.vertices:
            vertice = self.vertices[vertice]
            if valor in vertice.conexoes:
                vertice.remAresta(valor)
    
    def addAresta(self,vert_o,vert_d):
        if self.vertices.get(vert_o) != None:
            self.vertices[vert_o].addAresta(vert_d)
    
    def remAresta(self,vert_o,vert_d):
        if self.vertices.get(vert_o) != None:
            self.vertices[vert_o].remAresta(vert_d)
    
    def __str__(self):
        saida = ""
        vertices = self.vertices
        for vertice in vertices:
            saida += f"Vertice: {vertice} - {self.vertices[vertice].conexoes}\n"
        return saida

class Vertice:
    def __init__(self,valor):
        self.id = valor
        self.conexoes = {}

    def addAresta(self,vert_d,peso=-1):
        if self.conexoes.get(vert_d) == None:
            self.conexoes[vert_d] = peso
    
    def remAresta(self,vert_d):
        if self.conexoes.get(vert_d) != None:
            self.conexoes.pop(vert_d)

"""
def dijkstra(aGraph,start):
    pq = PriorityQueue()
    start.setDistance(0)
    pq.buildHeap([(v.getDistance(),v) for v in aGraph])
    while not pq.isEmpty():
        currentVert = pq.delMin()
        for nextVert in currentVert.getConnections():
            newDist = currentVert.getDistance() \
                    + currentVert.getWeight(nextVert)
            if newDist < nextVert.getDistance():
                nextVert.setDistance( newDist )
                nextVert.setPred(currentVert)
                pq.decreaseKey(nextVert,newDist)
"""

def dijkstra(grafo,origem):
    fila = []
    if grafo.vertices.get(origem) != None:
        origem = grafo.vertices[origem]
        fila.append(origem)
        origem.dist = 0
        while fila:
            atual = fila.pop(0)
            for prox in atual.conexoes:
                novadist = atual.dist + 1
            

# Pegando a entrada e formando o grafo
grafo = Grafo()
for _ in range(int(input())):
    vertice,arestas,*conexoes = input().split()
    grafo.addVertice(vertice)
    for conec in conexoes:
        grafo.addAresta(vertice,conec)
meu_id,Mussum_id = input().split()

# Pegando a distancia pro Mussum
print(grafo)
