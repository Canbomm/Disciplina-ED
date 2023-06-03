class Grafo:
    def __init__(self):
        self.vertices = {}
        self.arestas = {}
    
    def insere_v(self,id,dado):
        # Adiciona um vertice no grafo
        self.vertices[id] = dado
    
    def remove_v(self,id):
        # Remove um vertice no grafo
        # removendo o vertice
        if self.vertices.get(id):
            self.vertices.pop(id)
            self.arestas.pop(id)
        # removendo as possiveis conexoes
        vertices = self.vertices.keys()
        for vertice in vertices:
            conexoes = self.arestas.get(vertice)
            if conexoes:
                if id in conexoes:
                    self.arestas[vertice].remove(id)
            
    def insere_a(self,id_o,id_d):
        # Conecta dois vertices (caso existam) do grafo
        if self.vertices.get(id_o) and self.vertices.get(id_d):
            if self.arestas.get(id_o):
                self.arestas[id_o] += [id_d]
            else:
                self.arestas[id_o] = [id_d]
            #self.vertices[id_d].nodeConecta(id_o)
    
    def remove_a(self,id_o,id_d):
        # Remove a conexao entre dois vertices (caso exista) do grafo
        if self.vertices.get(id_o) and self.arestas.get(id_o):
            filhos = self.arestas[id_o]
            if id_d in filhos:
                self.arestas[id_o].remove(id_d)

    def grau_saida(self,id):
        # Quantos vertices saem do vertice escolhido
        if self.arestas.get(id):
            return len(self.arestas[id])
        else:
            return 0
    
    def grau_entrada(self,id):
        # Quantos vertices se conectam ao vertice escolhido
        grau = 0
        vertices = list(self.vertices.keys())
        for vertice in vertices:
            conexoes = self.arestas.get(vertice)
            if conexoes and id in conexoes:
                grau += 1
        return grau
    
    def alcancavel(self,id_o,id_d):
        if self.vertices.get(id_o) and self.vertices.get(id_d):
            conexoes = self.arestas[id_o]
            if id_d in conexoes:
                return True
        return False

    def __str__(self):
        chaves = self.vertices.keys()
        print(f"Esses são os vertices: {chaves}\nConexoes:")
        for chave in chaves:
            print(f"Chave: {chave}, conexoes: {self.arestas.get(chave)}")
        return ""

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

#print(grafo)
#print(grafo.alcancavel('C', 'B'), grafo.alcancavel('A', 'C'), grafo.alcancavel('C', 'A'))
#print(grafo.grau_saida('A'), grafo.grau_entrada('A'), grafo.grau_saida('B'), grafo.grau_entrada('B'), grafo.grau_saida('C'), grafo.grau_entrada('C'))
#print(grafo.grau_entrada('A'), grafo.grau_saida('A'), grafo.grau_entrada('B'), grafo.grau_saida('B'))
