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
    
    def percorre(self,origem,passou):
        passou.append(origem)
        conexoes = self.vertices[origem].conexoes
        maior_p = 0
        maior_v = None
        # pegando a maior distancia
        for conec in conexoes:
            if not (conec in passou):
                peso = int(conexoes[conec])
                if maior_p < peso:
                    maior_p = peso
                    maior_v = conec
        # percorrendo a partir dessa distancia
        if maior_v != None:
            return maior_p + self.percorre(maior_v,passou)
        else:
            total = list(self.vertices.keys())
            if len(total) == len(passou):
                return 0
            else:
                dist_add = 0
                for vert in total:
                    if not (vert in passou):
                        print(vert,end=",")
                        dist_add += self.vertices[vert].maiordist()
                return dist_add
    
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
    
    def addConexao(self,vert2,peso=0):
        self.conexoes[vert2] = peso
    
    def remConexao(self,vert2):
        self.conexoes.pop(vert2)
    
    def maiordist(self):
        maior = 0
        for conec in self.conexoes:
            dist = int(self.conexoes[conec])
            if dist > maior:
                maior = dist
        return maior

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
distancias = []
for vertice in grafo.vertices:
    print("--------------")
    distancias.append(grafo.percorre(vertice,[])*3.14)
print(f"R$ {max(distancias):.2f}")
