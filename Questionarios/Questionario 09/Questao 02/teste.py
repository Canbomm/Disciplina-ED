class Grafo:
    def __init__(self):
        self.vertices = {}
    
    def addBola(self,valor,lista):
        self.vertices[valor] = Vertice(valor)
        for vizinho in lista:
            self.vertices[valor].addVizinho(vizinho)

class Vertice:
    def __init__(self,valor):
        self.pai = valor
        self.vizinhos = []
    
    def addVizinho(self,vizinho):
        self.vizinhos.append(vizinho)

def temCiclo(grafo):
    pais = grafo.vertices.keys()
    # percorrendo todos os pais
    for pai in pais:
        # pegando os vizinhos de um determinado pai
        vizinhos = grafo.vertices[pai].vizinhos
        for vizinho in vizinhos:
            ligacoes = grafo.vertices[vizinho].vizinhos
            if pai in ligacoes:
                return True
    return False

grafo = Grafo()
grafo.addBola("Joao",["Teresa", "Lili", "Maria"])
grafo.addBola("Maria",["Teresa"])
grafo.addBola("Teresa",["Lili"])
grafo.addBola("Lili",["Joao","Maria"])

ciclo = temCiclo(grafo)
if ciclo:
    print("Hoje tem!")
else:
    print("... que ama ninguem.")
