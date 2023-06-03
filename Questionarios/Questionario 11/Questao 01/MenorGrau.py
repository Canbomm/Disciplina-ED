# literalmente mudei 2 linhas do meu codigo de maior grau
class Graph:
    def __init__(self):
        self.vertlist = {}
    
    def graphAddVertex(self,valor):
        # Adiciona um vertice no grafo
        self.vertlist[valor] = Node(valor)
    
    def graphRemVertex(self,valor):
        # Remove um vertice no grafo
        # removendo o vertice
        if self.vertlist.get(valor):
            self.vertlist.pop(valor)
        # removendo as possiveis conexoes
        vertices = self.vertlist.keys()
        for vertice in vertices:
            conexoes = self.vertlist[vertice].conexoes
            conexoes.pop(valor,None)
            
    def graphAddConecta(self,vert1,vert2):
        # Conecta dois vertices (caso existam) do grafo
        if self.vertlist.get(vert1):
            if self.vertlist.get(vert2):
                self.vertlist[vert1].nodeConecta(vert2)
                self.vertlist[vert2].nodeConecta(vert1)
    
    def graphRemConecta(self,vert1,vert2):
        # Remove a conexao entre dois vertices (caso exista) do grafo
        node_vert1 = self.vertlist.get(vert1)
        if node_vert1:
            node_vert2 = self.vertlist.get(vert2)
            if node_vert2:
                filhos_vert1 = node_vert1.conexoes
                filhos_vert2 = node_vert2.conexoes
                if (filhos_vert2.get(vert1) == 0) and (filhos_vert1.get(vert2) == 0):
                    node_vert1.nodeDesconecta(vert2)
                    node_vert2.nodeDesconecta(vert1)

    def menorGrau(self):
        chaves = self.vertlist.keys()
        grau = float("inf")
        for chave in chaves:
            grau_chave = len(self.vertlist[chave].conexoes)
            if grau_chave < grau:
                grau = grau_chave
        if grau == float("inf"):
            return 0
        return grau

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

# pegando a quantidade de conexoes
print(grafo.menorGrau())
