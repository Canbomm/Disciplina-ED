def procuraSTR(frase,procurado):
    for index, char in enumerate(frase):
        if char == procurado:
            frase = frase[:index] + frase[index:]
            return True,frase
    return False,frase

def tratalista(lista):
    lista.sort()
    tratado = []
    while lista:
        original = lista.pop()
        for index,char in enumerate(lista):
            if char == original:
                lista.pop(index)
        tratado.append(original)
    return "".join(tratado[::-1])

quant_testes = int(input())

while quant_testes > 0:
    plano = input()
    turno1 = input()
    turno2 = input()
    turno3 = input()
    turno = turno1+turno2+turno3
    ralar = []

    while plano:
        planejado = plano[-1]
        nao_achou = True
        for index,char in enumerate(turno):
            if char == planejado:
                nao_achou = False
                turno = turno[:index] + turno[index+1:]
                break
        if nao_achou:
            ralar.append(planejado)
        plano = plano[:-1]

    if turno:
        print("You died!")
    elif ralar != []:
        ralar = tratalista(ralar)
        print(f"Bora ralar: {ralar}")
    else:
        print("It's in the box!")

    quant_testes -= 1
