class Grafo:
    def __init__(self):
        self.vertices = {}
    
    def addBola(self,valor,lista):
        self.vertices[valor] = Vertice(valor)
        for vizinho in lista:
            self.vertices[valor].addVizinho(vizinho)
    
    def __str__(self):
        chaves = self.vertices.keys()
        print(f"Esses são os vertices: {chaves}\nConexoes:")
        for chave in chaves:
            print(f"Vertice: {chave}, Conexoes: {self.vertices[chave].vizinhos}")
        return ""

class Vertice:
    def __init__(self,valor):
        self.pai = valor
        self.vizinhos = []
    
    def addVizinho(self,vizinho):
        self.vizinhos.append(vizinho)

def procuraIdolo(grafo,eu,idolo,nivel,visitados,niveis):
    conexoes = grafo.vertices.get(eu).vizinhos
    if conexoes:
        for conec in conexoes:
            if conec == idolo:
                return nivel
            elif not (conec in visitados):
                visitados.append(conec)
                novo_nivel = procuraIdolo(grafo,conec,idolo,nivel+1,visitados,niveis)
                niveis.append(novo_nivel)
        return nivel
    else:
        return "Forevis alonis..."

# Pegando a entrada e formando o grafo
tamanho = int(input())
grafo = Grafo()
for _ in range(tamanho):
    vertice,arestas,*conexoes = input().split()
    grafo.addBola(vertice,conexoes)

meu_id,Mussum_id = input().split()
#print(grafo)

print(procuraIdolo(grafo,meu_id,Mussum_id,0,[],[]))
