def verificaordem(lista):
    maior = float("inf")
    for num in lista:
        if maior < num:
            return False
        else:
            maior = num
    return True

print(verificaordem([5, 4, 3, 2, 1]))
