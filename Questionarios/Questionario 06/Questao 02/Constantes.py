# reais a inteiros
# organizar constante em ordem crescente de seu valor decimal
# partes decimais iguais = ordenar decrescente(apenas parte inteira)

def organizador(constantes):
    tamanho_lista = len(constantes)

    # organizando com apenas 2 constantes
    if tamanho_lista == 2:
        int_const1,frac_const1 = [int(x) for x in constantes[0][1].split(".")]
        int_const2,frac_const2 = [int(x) for x in constantes[1][1].split(".")]
        # 1 caso, ja esta ordenado
        if frac_const2 > frac_const1:
            return constantes
        
        # segundo caso, possuem o mesmo valor
        elif frac_const2 == frac_const1:
            # ordernar de forma decrescente pelo inteiro
            if int_const1 > int_const2:
                return constantes
            else:
                return [(constantes[1]),constantes[0]]

        # terceiro caso, nao esta ordenado
        else:
            return [(constantes[1]),(constantes[0])]

    # organizando com mais de 2 constantes
    else:
        meio_constantes = tamanho_lista//2
        metade_1 = organizador(constantes[meio_constantes:])
        metade_2 = organizador(constantes[:meio_constantes+1])
        for _ in range(tamanho_lista):
            const_1 = metade_1[-1][0]
            numero_1 = metade_1[-1][1]

            const_2 = metade_2[-1][0]
            numero_2 = metade_2[-1][1]

            print(numero_1)
            print(numero_2)
        return ""

while True:
    num_constantes = int(input())
    # criterio de parada
    if num_constantes == 0:
        break

    constantes = []
    while num_constantes > 0:
        entrada = input().split("=")
        constantes.append((entrada[0][:-1],entrada[1][1:]))
        num_constantes -= 1

    print(organizador(constantes))
