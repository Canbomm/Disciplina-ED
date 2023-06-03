# esse funciona
class Grafo:
    def __init__(self):
        self.vertices = {}
    
    def addVertice(self,valor):
        self.vertices[valor] = Vertice(valor)
    
    def remVertice(self,valor):
        if self.vertices.get(valor) != None:
            self.vertices.pop(valor)
    
    def addAresta(self,vert_o,vert_d):
        if self.vertices.get(vert_o) != None:
            self.vertices[vert_o].addConec(vert_d)
    
    def __str__(self):
        saida = ""
        vertices = list(self.vertices.keys())
        for vertice in vertices:
            saida += f"{vertice} - {self.vertices[vertice].conexoes}\n"
        return saida

class Vertice:
    def __init__(self,valor):
        self.id = valor
        self.cor = 0
        self.dist = -1
        self.anterior = None
        self.conexoes = []
    
    def addConec(self,valor):
        if not (valor in self.conexoes):
            self.conexoes.append(valor)

def bfs(grafo,origem):
    origem.dist = 0
    fila = []
    fila.append(origem)
    while fila:
        atual = fila.pop(0)
        for conec in atual.conexoes:
            conec = grafo.vertices[conec]
            if conec.cor < 1:
                conec.cor += 1
                conec.dist = atual.dist + 1
                conec.anterior = atual
                fila.append(conec)
        atual.cor += 1

# pegando entrada
grafo = Grafo()
for ent in range(int(input())):
    ent = input().split()
    vertice = ent[0]
    conexoes = ent[2:]
    grafo.addVertice(vertice)
    for conec in conexoes:
        grafo.addAresta(vertice,conec)
meu_id,Mussum_id = input().split()

# calculando distancias
if grafo.vertices.get(meu_id) != None:
    eu = grafo.vertices[meu_id]
    bfs(grafo,eu)
    dist_mussum = grafo.vertices[Mussum_id].dist
    if dist_mussum > -1:
        print(dist_mussum-1)
    else:
        print(f"Forevis alonis...")
else:
    print(f"Forevis alonis...")
