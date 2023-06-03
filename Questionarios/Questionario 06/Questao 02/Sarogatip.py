def sarogatip(dicionario):
    organizado = []

    numeros = []
    for chave in dicionario:
        numeros.append(chave)
    # obrigado prof Lucas pelo macete, APC valeu a pena
    chaves = sorted(numeros,key=lambda x:(x[1],-x[0]))
    for chave in chaves:
        organizado.append(dicionario[chave])
    
    return organizado

while True:
    num_constantes = int(input())
    # criterio de parada
    if num_constantes == 0:
        break

    constantes = []
    dic_constantes = {}
    while num_constantes > 0:
        entrada = input().split("=")
        nome_const = entrada[0][:-1]
        valor_const = tuple([int(x) for x in entrada[1][1:].split(".")])
        dic_constantes[valor_const] = nome_const
        num_constantes -= 1
    
    organiza = sarogatip(dic_constantes)
    resposta = " < ".join(organiza)
    print(resposta)
