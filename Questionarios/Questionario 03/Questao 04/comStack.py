class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)
      
    def pop(self):
        if self.items != []:
            return self.items.pop()

    def peek(self):
        return self.items[0]

    def size(self):
        return len(self.items)

# pegando e organizando as entradas
anilha = int(input())
pesos = Stack()
while anilha != 0:
    pesos.push(anilha)
    anilha = int(input())
peso_desejado = int(input())

# retirando a anilha do topo
if pesos.items != []:
    total_retirado = 1
    peso_topo = pesos.pop()
    total_peso = peso_topo
    print(f"Peso retirado: {peso_topo}")
    # retirando mais anilhas ate o desejado
    while peso_topo != peso_desejado:
        peso_topo = pesos.pop()
        print(f"Peso retirado: {peso_topo}")
        total_retirado += 1
        total_peso += peso_topo

    print(f"Anilhas retiradas: {total_retirado}")
    print(f"Peso total movimentado: {total_peso}")
else:
    print(f"Peso retirado: 0")
    print(f"Anilhas retiradas: 0")
    print(f"Peso total movimentado: 0")
