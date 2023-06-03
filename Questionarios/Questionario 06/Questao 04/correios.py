def ordena(sequencia):
    # criterio de parada
    if len(sequencia) < 1:
        return sequencia
    # ordenando de fato
    else:
        criterio = sequencia.pop()
        valores_menores = []
        valores_maiores = []

        for numero in sequencia:
            if numero > criterio:
                valores_maiores.append(numero)
            else:
                valores_menores.append(numero)
        
        return ordena(valores_menores) + [criterio] + ordena(valores_maiores)

def conta_economia(sequencia):
    # definindo variaveis iniciais
    economia = 0
    penultimo_index = len(sequencia)-1

    # contando a economia comparando o valor atual com o proximo
    index = 0
    while index != penultimo_index:
        if sequencia[index] == sequencia[index+1]:
            economia += 1
        index += 1
    return economia

# pegando a entrada
quant_ceps = int(input())
ceps = []
while quant_ceps > 0:
    quant_ceps -= 1
    cep = int(input())
    ceps.append(cep)
# ordenando o cep
ceps = ordena(ceps)

# montando a matriz e contando a economia
economia = 0
for ind_linha in range(0,len(str(ceps[0]))):
    linha = []
    for ind_coluna in range(0,len(ceps)):
        valor = int(str(ceps[ind_coluna])[ind_linha])
        linha.append(valor)
    economia += conta_economia(linha)

print(f"R$ {(economia*7)/100:.2f}")
