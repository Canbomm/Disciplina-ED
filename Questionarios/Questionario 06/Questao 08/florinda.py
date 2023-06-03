# altura ideal = 180
# peso ideal = 75
# mesma altura, prevalece o menor peso
# mesma altura, mesmo peso, ordenar pelo sobrenome e depois nome

# esse meu codigo IRIA considerar o peso ideal
# mas pelo o que eu entendi do problema, apenas importa o MENOR peso

def ordenapeso(pesos):
    # [['Tostes, Heitor', 'Costa, Bruno'], [], ['Carvalho, Juca'], [], [], [], [], [], [], [], ['Kleber, Joao'], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]
    organizados = []
    for lista in pesos:
        tam_lista = len(lista)
        if tam_lista > 1:
            lista.sort()
            for nome in lista:
                organizados.append(nome)
        elif tam_lista == 1:
            organizados.append(lista)
    return organizados

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
            pesos = []
            for _ in range(0,peso_mais_distante+1):
                pesos.append([])

            for nome in lista:
                peso = dic_peso[nome]
                peso_ideal = abs(peso-75)
                print(f"Eu sou o {nome} e meu peso ideal é {peso_ideal}")
                pesos[peso_ideal] += [nome]

            #print(f"Pesos passados para a funcao: {pesos}")
            ordenados.append(ordenapeso(pesos))
        else:
            #print(f"Entrei no else, eu sou a lista: {lista}")
            ordenados.append(lista)

print(ordenados)
