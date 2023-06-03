class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)
      
    def pop(self):
        if self.items != []:
            self.items.pop()
    
    def peek(self):
        return self.items[0]

    def size(self):
        return len(self.items)

numeros = Stack()
palavras = Stack()

frase = input().split()
for entrada in frase:
    if entrada.isnumeric():
        numeros.push(entrada)
    else:
        palavras.push(entrada)

print("Palavras:")
for item in palavras.items:
    print(item)
print()
print("Numeros:")
for item in numeros.items:
    print(item)
