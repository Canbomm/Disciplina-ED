class Grafo:
    def __init__(self):
        self.vertices = {}
        self.simulados = []

    def addVertice(self,valor):
        self.vertices[valor] = Vertice(valor)

    def Painel(self):
        vertices = list(self.vertices.keys())
        for vertice in vertices:
            if not (vertice in self.simulados):
                self.simulados.append(vertice)
                novos_vertices = self.vertices[vertice].simulaPainel()
                for novo in novos_vertices:
                    self.addVertice(novo)
    
    def encontrou(self,desejado):
        if self.vertices.get(desejado) != None:
            return True
        else:
            return False
    
    def __str__(self):
        saida = ""
        for vertice in self.vertices:
            saida += f"{vertice} - {self.vertices[vertice].conexoes}\n"
        return saida

class Vertice:
    def __init__(self,valor):
        self.id = valor
        self.conexoes = []
    
    def simulaPainel(self):
        incrementa = self.id + 1
        duplica = self.id * 2
        inverte = int(str(self.id)[::-1])
        self.conexoes.append(incrementa)
        self.conexoes.append(duplica)
        self.conexoes.append(inverte)
        return incrementa, duplica, inverte

def rodaPainel(grafo,origem,objetivo):
    grafo.Painel()
    if grafo.encontrou(objetivo):
        return
    else:
        rodaPainel(grafo,origem,objetivo)

def destravarPainel(painel, origem, objetivo):
    grafo = Grafo()
    grafo.addVertice(origem)
    rodaPainel(grafo,origem,objetivo)
    print(grafo)

destravarPainel(None,761,835)