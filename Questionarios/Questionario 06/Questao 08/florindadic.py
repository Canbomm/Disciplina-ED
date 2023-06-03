def ordenapeso(pesos,dicionario):
    organizado = []

    # organizando pelo menor peso mais proximo do ideal
    maior_ind = 0
    for index,chave in enumerate(pesos):
        if chave > 75:
            break
        else:
            maior_ind = index
        
    pesos_ideais = pesos[:maior_ind+1]
    pesos_leves = pesos[maior_ind+1:]
    
    for chave in pesos_ideais[::-1]:
        nomes = dicionario.get(chave)
        nomes.sort()
        organizado += nomes

    # organizando pelo menor peso
    for chave in pesos_leves:
        nomes = dicionario.get(chave)
        nomes.sort()
        organizado += nomes
    
    return organizado

ordenados = []
dic_altura = {}
dic_peso = {}

pretendentes = int(input())
altura_mais_distante = -1
peso_mais_distante = -1
for _ in range(0,pretendentes):
    pretendente = input().split()
    nome = pretendente[1] + ", " + pretendente[0]
    altura = int(pretendente[2])
    peso = int(pretendente[3])
    dic_altura[nome] = altura
    dic_peso[nome] = peso

    # essa parte serve para determinar o tamanho das listas hasheadas
    altura_ideal = abs(altura-180)
    if altura_mais_distante < altura_ideal:
        altura_mais_distante = altura_ideal
    peso_ideal = abs(peso-75)
    if peso_mais_distante < peso_ideal:
        peso_mais_distante = peso_ideal

# --- Ordenando pela altura ---
alturas = []
for _ in range(0,altura_mais_distante+1):
    alturas.append([])

for nome in dic_altura:
    altura = dic_altura[nome]
    altura_ideal = abs(altura-180)
    alturas[altura_ideal] += [nome]

# --- Ordenando pelo peso ---
for index, lista in enumerate(alturas):
    if lista != []:
        tam_lista = len(lista)
        if tam_lista > 1:
            # caiu nesse if = desempate por peso
            pesos_nomes = {}

            for nome in lista:
                peso = dic_peso[nome]
                if pesos_nomes.get(peso) != None:
                    pesos_nomes[peso] += [nome]
                else:
                    pesos_nomes[peso] = [nome]

            pesos = sorted(pesos_nomes)
            ordenados += ordenapeso(pesos,pesos_nomes)
        else:
            ordenados += lista

for linha in ordenados:
    print(linha)
