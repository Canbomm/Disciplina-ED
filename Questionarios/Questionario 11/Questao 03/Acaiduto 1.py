# nao funciona
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
            
    def graphAddConecta(self,vert1,vert2,peso):
        # Conecta dois vertices (caso existam) do grafo
        if self.vertlist.get(vert1):
            self.vertlist[vert1].nodeConecta(vert2,peso)
    
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

    def naoDijkstra(self,origem,ja_passou=[]):
        ja_passou.append(origem)
        conexoes = self.vertlist[origem].conexoes
        maior_p = 0
        maior_c = None
        # procurando o maior peso
        for chave in conexoes:
            if not (chave in ja_passou):
                peso = int(conexoes[chave])
                if peso > maior_p:
                    maior_p = peso
                    maior_c = chave
        print(f"Chamada de: {origem}, ja passou: {ja_passou}")
        print(maior_p)
        # vendo o caminho a partir dai
        if maior_c != None:
            return maior_p + grafo.naoDijkstra(maior_c,ja_passou)
        else:
            # verificando se tem loop
            primeiro = ja_passou[0]
            loop = list(self.vertlist[origem].conexoes.keys())
            if primeiro in loop:
                return 0
            else:
                return 0

    def __str__(self):
        print(f"Esses são os vertices: {self.vertlist.keys()}\nConexoes:")
        chaves = list(self.vertlist.keys())
        chaves.sort()
        for chave in chaves:
            print(f"Vertice: {chave}, conexoes: {self.vertlist[chave].conexoes}")
        return ""

class Node:
    def __init__(self,valor):
        self.id = valor
        self.conexoes = {}
    
    def nodeConecta(self,valor,peso=0):
        self.conexoes[valor] = peso
    
    def nodeDesconecta(self,valor):
        self.conexoes.pop(valor)

grafo = Graph()
quant_cmd = int(input())
for cmd in range(quant_cmd):
    entrada = input().split()
    id = entrada[0]
    residencias = entrada[1]
    conexoes = entrada[2:]
    # criando o grafo
    grafo.graphAddVertex(id)
    for ind in range(0,len(conexoes),2):
        conexao = conexoes[ind]
        peso = conexoes[ind+1]
        grafo.graphAddConecta(id,peso,conexao)

# pegando a quantidade de conexoes
print(grafo)
print("Pegando as distâncias")
for vert in grafo.vertlist.keys():
    print("----------")
    print(grafo.naoDijkstra(vert,[]))
    #print("----------")
