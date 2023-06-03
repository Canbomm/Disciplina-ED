total_pecas = int(input())
pecas = input().split()
duplicatas = 0

def procura_item(lista,procurado):
    for item in lista:
        if item == procurado:
            return True
    return False

while total_pecas > 0:
    peca = pecas.pop()
    if procura_item(pecas,peca):
        duplicatas += 1
    total_pecas -= 1

print(duplicatas)
