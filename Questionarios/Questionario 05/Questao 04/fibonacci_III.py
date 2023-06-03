chamadas = {0:0}
def fibonacci(num):
    # guardando as chamadas
    if chamadas.get(num) != None:
        chamadas[num] += 1
    else:
        chamadas[num] = 1
    # calculando fibonacci
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return fibonacci(num-1) + fibonacci(num-2)

num = int(input())
print(f"fibonacci({num}) = {fibonacci(num)}.")

chamadas_sorted = sorted(chamadas)
for chave in chamadas_sorted:
    print(f"{chamadas[chave]} chamada(s) a fibonacci({chave}).")
