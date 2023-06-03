# altura ideal = 180
# peso ideal = 75
# mesma altura, prevalece o menor peso
# mesma altura, mesmo peso, ordenar pelo sobrenome e depois nome

def ordenapeso(pesos,dicionario):
    #print(f"\nEstou na função\n")
    organizado = []
    
    # organizando pelo menor peso mais proximo do ideal
    #print(f"Procurando o peso ideal\nPesos: {pesos} com tamanho: {len(pesos)}")
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
        #print(f"Menor peso (ideal): {chave} {nomes}")
        organizado += nomes

    # organizando pelo menor peso
    for chave in pesos_leves:
        nomes = dicionario.get(chave)
        nomes.sort()
        #print(f"Menor peso: {chave} {nomes}")
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
            #print(f"Entrei no if, eu sou a lista: {lista}")
            # vou ter que desempatar pelo peso
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
            #print(f"Entrei no else, eu sou a lista: {lista}")
            ordenados += lista

print("------")
for linha in ordenados:
    print(linha)
