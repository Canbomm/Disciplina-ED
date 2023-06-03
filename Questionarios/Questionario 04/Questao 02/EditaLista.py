import collections
from collections import deque

lista = deque()

while True:
    entrada = input().split()
    if entrada[0] == "I":
        # insere no inicio
        lista.appendleft(entrada[1])

    elif entrada[0] == "F":
        # insere no final
        lista.append(entrada[1])

    elif entrada[0] == "P":
        # remove do final
        if len(lista) > 0:
            print(lista.pop())
        #else:
        #    print()

    elif entrada[0] == "D":
        # remove do inicio
        if len(lista) > 0:
            print(lista.popleft())
        #else:
        #    print()

    else:
        for e in lista:
            print(e)
        break
