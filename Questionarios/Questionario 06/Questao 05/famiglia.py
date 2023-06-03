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

populacao = int(input())
rua = ordena([int(x) for x in input().split()])
endereço_pizzopato = len(rua)//2
pizzopato = rua[endereço_pizzopato]

primeira_met = rua[:endereço_pizzopato]
segunda_met = rua[endereço_pizzopato:]

distancia = []
for casa in primeira_met:
    distancia.append(abs(casa-pizzopato))
for casa in segunda_met:
    distancia.append(abs(casa-pizzopato))

print(sum(distancia))
