# esse meu codigo estorou o limite de recursao
# nao consigo pensar em um jeito mais otimizado no momento entao....
import sys
sys.setrecursionlimit(10000)
# ainda sim nao deu certo, provavelmente estorou o tempo

def Anacleto(mesaA,tentativas=1):
    # verificar se a mesa ja nao esta ordenada
    ordenada = verificaordem(mesaA)
    if ordenada:
        # desconsiderar essa tentativa
        return tentativas-1

    # 1 etapa
    mesaB = []
    atual = mesaA.pop()
    tam_mesaA = len(mesaA)

    # etapas 2 e 3
    while tam_mesaA > 0:
        proximo = mesaA.pop()
        if proximo < atual:
            mesaB.append(proximo)
        else:
            mesaB.append(atual)
            atual = proximo
        tam_mesaA -= 1

    # etapa 4
    mesaA.append(atual)
    while mesaB:
        mesaA.append(mesaB.pop())
    
    # etapa 5
    inicial = float("inf")
    for num in mesaA:
        if num > inicial:
            tentativas = Anacleto(mesaA,tentativas+1)
        else:
            inicial = num
    return tentativas

def verificaordem(lista):
    maior = float("inf")
    for num in lista:
        if maior < num:
            return False
        else:
            maior = num
    return True

quant_processos = int(input())
identificadores = [int(x) for x in input().split()]
print(Anacleto(identificadores))
