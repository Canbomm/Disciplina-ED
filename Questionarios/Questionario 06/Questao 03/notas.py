def organizador(notas):
    # criterio de parada
    if len(notas) < 1:
        return notas
    # ordenando de fato
    else:
        criterio = notas.pop()
        valores_menores = []
        valores_maiores = []

        for nota in notas:
            if nota > criterio:
                valores_maiores.append(nota)
            else:
                valores_menores.append(nota)
        
        return organizador(valores_menores) + [criterio] + organizador(valores_maiores)

# na saida ele quer (nessa ordem):
# pior nota
# mediana
# melhor nota

quantas_notas = int(input())
notas = []
for _ in range(quantas_notas):
    nota = float(input())
    notas.append(nota)

notas_organizadas = organizador(notas)
pior_nota = notas_organizadas[0]
melhor_nota = notas_organizadas[-1]
mediana = notas_organizadas[len(notas_organizadas)//2]

print(f"{pior_nota:.2f}\n{mediana:.2f}\n{melhor_nota:.2f}")
