# Versao que o coderunner aceitou
class Grafo:
    def __init__(self):
        self.vertices = {}
        self.arestas = []
    
    def insere_v(self,id,dado):
        self.vertices[id] = dado
    
    def insere_a(self,id_o,id_d):
        if self.vertices.get(id_o) != None:
            if self.vertices.get(id_d) != None:
                if not ((id_o,id_d) in self.arestas):
                    self.arestas.append((id_o,id_d))
    
    def remove_v(self,id):
        # removendo o vertice
        if self.vertices.get(id) != None:
            self.vertices.pop(id)
        # removendo possíveis conexoes
        arestas = self.arestas
        ind = 0
        while ind < len(arestas):
            if id in arestas[ind]:
                self.arestas.pop(ind)
                ind = 0
            else:
                ind += 1

    def remove_a(self,id_o,id_d):
        if (id_o,id_d) in self.arestas:
            self.arestas.remove((id_o,id_d))

    def grau_saida(self,id):
        arestas = self.arestas
        grau = 0
        for aresta in arestas:
            if aresta[0] == id:
                grau += 1
        return grau
    
    def grau_entrada(self,id):
        arestas = self.arestas
        grau = 0
        for aresta in arestas:
            if aresta[1] == id:
                grau += 1
        return grau

    def alcancavel(self,id_o,id_d):
        arestas = self.arestas
        for aresta in arestas:
            if aresta[0] == id_o:
                # ja encontrei o destino
                if aresta[1] == id_d:
                    return True
                else:
                    return grafo.alcancavel(aresta[1],id_d)
        return False
    
    # essa funcao nao e usada pelo coderunner mas me auxiliou bastante
    def __str__(self):
        vertices = list(self.vertices.keys())
        arestas = self.arestas
        return f"Vertices: {vertices}" + "\n" + f"Arestas: {arestas}"

# <---------------------------------------------->
# Daqui pra baixo, nao precisava para o coderunner
# <---------------------------------------------->

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
