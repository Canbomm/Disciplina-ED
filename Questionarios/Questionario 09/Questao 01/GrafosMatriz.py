class Grafo_matriz:
    def __init__(self,tamanho):
        self.matriz = []
        for _ in range(tamanho):
            linha = []
            for _ in range(tamanho):
                linha.append(0)
            self.matriz.append(linha)
    
    def __str__(self):
        saida = ""
        for linha in self.matriz:
            for coluna in linha:
                casas = len(str(coluna))-1
                if casas > 0:
                    saida += ("   "[:-casas]) + (str(coluna))
                else:
                    saida += "   " + (str(coluna))
            saida += "\n"
        return saida
    
    def addVertice(self,linha,coluna,peso):
        self.matriz[linha][coluna] = peso

total_vertices, arestas, tipo_grafo = input().split()
total_vertices = int(total_vertices)
arestas = int(arestas)

Grafo = Grafo_matriz(total_vertices)
maior = 0
if tipo_grafo == "D":
    for ent in range(0,arestas):
        aresta = [int(elem) for elem in input().split()]
        Grafo.addVertice(aresta[0]-1,aresta[1]-1,aresta[2])
else:
    for ent in range(0,arestas):
        aresta = [int(elem) for elem in input().split()]
        Grafo.addVertice(aresta[0]-1,aresta[1]-1,aresta[2])
        Grafo.addVertice(aresta[1]-1,aresta[0]-1,aresta[2])

print(Grafo)
