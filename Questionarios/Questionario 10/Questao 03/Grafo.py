class Grafo:
    def __init__(self):
        self.vertlist = {}
    
    def insere_v(self,id,dado):
        # Adiciona um vertice no grafo
        self.vertlist[id] = Node(dado)
    
    def remove_v(self,id):
        # Remove um vertice no grafo
        # removendo o vertice
        if self.vertlist[id]:
            self.vertlist.pop(id)
        # removendo as possiveis conexoes
        vertices = self.vertlist.keys()
        for vertice in vertices:
            conexoes = self.vertlist[vertice].conexoes
            if conexoes.get(id):
                conexoes.pop(id)
            
    def insere_a(self,id_o,id_d):
        # Conecta dois vertices (caso existam) do grafo
        if self.vertlist.get(id_o):
            if self.vertlist.get(id_d):
                self.vertlist[id_o].nodeConecta(id_d)
                #self.vertlist[id_d].nodeConecta(id_o)
    
    def remove_a(self,id_o,id_d):
        # Remove a conexao entre dois vertices (caso exista) do grafo
        node_id_o = self.vertlist.get(id_o)
        if node_id_o:
            filhos = node_id_o.conexoes
            if id_d in filhos:
                node_id_o.nodeDesconecta(id_d)

    def grau_saida(self,id):
        # Quantos vertices saem do vertice escolhido
        if self.vertlist.get(id):
            return len(list(self.vertlist[id].conexoes.keys()))
        else:
            return 0
    
    def grau_entrada(self,id):
        # Quantos vertices se conectam ao vertice escolhido
        grau = 0
        if self.vertlist.get(id):
            vertices = list(self.vertlist.keys())
            for vertice in vertices:
                conexoes = list(self.vertlist[vertice].conexoes.keys())
                if id in conexoes:
                    grau += 1
            return grau
        else:
            return 0
    
    def alcancavel(self,id_o,id_d):
        if self.vertlist.get(id_o) and self.vertlist.get(id_d):
            conexoes = list(self.vertlist[id_o].conexoes.keys())
            if id_d in conexoes:
                return True
        return False

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

grafo = Grafo()
quant_cmd = int(input())
for cmd in range(quant_cmd):
    entrada = input().split()
    cmd = entrada[0]
    if cmd == "IV":
        # insere o vertice com ID
        grafo.insere_v(entrada[1],entrada[2])
    elif cmd == "IA":
        # insere aresta entre os 2 IDs (caso os 2 existam)
        grafo.insere_a(entrada[1],entrada[2])
    elif cmd == "RV":
        # remove o vertice com ID (e todas as arestas)
        grafo.remove_v(entrada[1])
    elif cmd == "RA":
        # remove aresta entre os 2 IDs (caso os 2 existam)
        grafo.remove_a(entrada[1],entrada[2])
    else:
        # comando invalido
        print("Comando invalido")
        break

print(grafo)
#print(grafo.alcancavel('C', 'B'), grafo.alcancavel('A', 'C'), grafo.alcancavel('C', 'A'))
#print(grafo.grau_saida('A'), grafo.grau_entrada('A'), grafo.grau_saida('B'), grafo.grau_entrada('B'), grafo.grau_saida('C'), grafo.grau_entrada('C'))
