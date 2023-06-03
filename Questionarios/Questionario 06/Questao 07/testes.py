quant_testes = 1

while quant_testes > 0:
    plano = "AAAABBBBCCCC"
    turno1 = "ABCC"
    turno2 = "AB"
    turno3 = "A"
    turno = turno1+turno2+turno3
    ralar = []

    while plano:
        print(f"Plano: {plano},Turno:{turno}")

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
        ralar.sort()
        ralar = "".join(ralar)
        print(f"Ralar: {ralar}")
    else:
        print("It's in the box!")

    quant_testes -= 1
