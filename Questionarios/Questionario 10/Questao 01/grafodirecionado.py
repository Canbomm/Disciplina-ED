class Graph:
    def __init__(self):
        self.vertlist = {}
    
    def graphAddVertex(self,valor):
        # Adiciona um vertice no grafo
        self.vertlist[valor] = Node(valor)
    
    def graphRemVertex(self,valor):
        # Remove um vertice no grafo
        # removendo o vertice
        if self.vertlist[valor]:
            self.vertlist.pop(valor)
        # removendo as possiveis conexoes
        vertices = self.vertlist.keys()
        for vertice in vertices:
            conexoes = self.vertlist[vertice].conexoes
            if conexoes.get(valor):
                conexoes.pop(valor)
            
    def graphAddConecta(self,vert1,vert2):
        # Conecta dois vertices (caso existam) do grafo
        if self.vertlist.get(vert1):
            if self.vertlist.get(vert2):
                self.vertlist[vert1].nodeConecta(vert2)
                #self.vertlist[vert2].nodeConecta(vert1)
    
    def graphRemConecta(self,vert1,vert2):
        # Remove a conexao entre dois vertices (caso exista) do grafo
        node_vert1 = self.vertlist.get(vert1)
        if node_vert1:
            filhos = node_vert1.conexoes
            if vert2 in filhos:
                node_vert1.nodeDesconecta(vert2)
    
    def __str__(self):
        print(f"Esses são os vertices: {self.vertlist.keys()}\nConexoes:")
        chaves = self.vertlist.keys()
        for chave in chaves:
            print(f"Chave: {chave}, conexoes: {self.vertlist[chave].conexoes}")
        return ""

class Node:
    def __init__(self,valor):
        self.id = valor
        self.conexoes = {}
    
    def nodeConecta(self,valor):
        self.conexoes[valor] = 0
    
    def nodeDesconecta(self,valor):
        self.conexoes.pop(valor)

grafo = Graph()
quant_cmd = int(input())
for cmd in range(quant_cmd):
    entrada = input().split()
    cmd = entrada[0]
    if cmd == "IV":
        # insere o vertice com ID
        grafo.graphAddVertex(entrada[1])
    elif cmd == "IA":
        # insere aresta entre os 2 IDs (caso os 2 existam)
        grafo.graphAddConecta(entrada[1],entrada[2])
    elif cmd == "RV":
        # remove o vertice com ID (e todas as arestas)
        grafo.graphRemVertex(entrada[1])
    elif cmd == "RA":
        # remove aresta entre os 2 IDs (caso os 2 existam)
        grafo.graphRemConecta(entrada[1],entrada[2])
    else:
        # comando invalido
        print("Comando invalido")
        break

# a questao pedia nao direcionado kkkk