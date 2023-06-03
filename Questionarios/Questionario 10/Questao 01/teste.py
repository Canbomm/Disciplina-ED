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
                #print(f"Filhos do {vert1}: {filhos_vert1}")
                #print(f"Filhos do {vert2}: {filhos_vert2}")
                #print("----")
                #print(filhos_vert2.get(vert1))
                #print(filhos_vert1.get(vert2))
                if (filhos_vert2.get(vert1) == 0) and (filhos_vert1.get(vert2) == 0):
                    #print("!!!!!!!tentando remover!!!!!!!")
                    node_vert1.nodeDesconecta(vert2)
                    node_vert2.nodeDesconecta(vert1)
    
    def maiorGrau(self):
        chaves = self.vertlist.keys()
        grau = 0
        for chave in chaves:
            grau_chave = len(self.vertlist[chave].conexoes)
            if grau_chave > grau:
                grau = grau_chave
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
#cmds = ["IV A","IV B","IA A B","IV C","IA A C","IA C B","RA A B",]
#cmds = ["IV A","IV B","IA A B","IV C","IA A C","IA B C","RV A"]
#cmds = ["IV A","IA B A","IV B","IA A B"]
#cmds = ["IV Alice","IV Bob","IA Alice Bob","IA Bob Alice","RV Bob","RV Eva"]
cmds = ['IV Alfa', 'IV Beta', 'IV Charlie', 'IV Delta', 'IA Alfa Beta', 'IA Alfa Charlie', 'IA Beta Alfa', 'IA Beta Charlie', 'IA Charlie Alfa', 'IA Charlie Beta', 'IV Delta', 'IV Echo', 'IA Delta Echo', 'RV Alfa']

for comando in cmds:
    print(f"Esse foi o comando: {comando}")
    comando = comando.split()
    cmd = comando[0]
    if cmd == "IV":
        # insere o vertice com ID
        grafo.graphAddVertex(comando[1])
    elif cmd == "IA":
        # insere aresta entre os 2 IDs (caso os 2 existam)
        grafo.graphAddConecta(comando[1],comando[2])
    elif cmd == "RV":
        # remove o vertice com ID (e todas as arestas)
        grafo.graphRemVertex(comando[1])
    elif cmd == "RA":
        # remove aresta entre os 2 IDs (caso os 2 existam)
        grafo.graphRemConecta(comando[1],comando[2])
    else:
        # comando invalido
        print("Comando invalido")
        break
    print(grafo)

# pegando a quantidade de conexoes
print(grafo.maiorGrau())
