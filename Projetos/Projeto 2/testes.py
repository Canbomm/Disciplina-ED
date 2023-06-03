"""
# criando a fila de tuplas
fila = []
while True:
    ent = input().split()
    if len(ent) == 2:
        fila.append((ent[0],ent[1]))
    else:
        break

print("[")
for ent in fila:
    print(ent,",",sep="")
print("]")
"""

saida = "? 100"
for i in range(100):
    saida += "\n? 20"
for i in range(100):
    for i in range(20):
        saida += "\nD 0"
saida += "\nprobtree"
print(saida)
