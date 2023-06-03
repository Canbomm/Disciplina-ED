import math

# pegando entrada e iniciando
tam_arq = int(input())
print(f"Transmitindo {tam_arq} bytes...")

# variaveis iniciais
contagem = 0
mostra = 0
media = 0
media_total = 0
tempo_total = 0

# fazendo o loop
while tam_arq > 0:
    # taxa de transferencia atual
    taxa = int(input())

    # contando a quantidade de vezes do loop
    contagem += 1

    # fazendo as medias de transferencia
    media_total += taxa
    media = media_total / contagem

    # calculando o quanto que falta
    tam_arq -= taxa

    # mostrando pro usuario o tempo restante
    mostra += 1
    if mostra == 5:
        if media != 0:
            # tenho que subtrair um numero mto pequeno, pois o math.ceil arredonda numeros tipo 2.0 para 3, sendo assim ele arredondaria 1.999 para 2.
            tempo_restante = math.ceil((tam_arq/media)-0.001)
            if tempo_restante != 0:
                print(f"Tempo restante: {tempo_restante} segundos.")
        else:
            print(f"Tempo restante: pendente...")
        # resetando as variaveis
        media = 0
        media_total = 0
        contagem = 0
        mostra = 0

    # calculando o tempo total
    tempo_total += 1

    # encerrando o loop e imprimindo o tempo total
    if tam_arq == 0:
        print(f"Tempo total: {tempo_total} segundos.")
        break
