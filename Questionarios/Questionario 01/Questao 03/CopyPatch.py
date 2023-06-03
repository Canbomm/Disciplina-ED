import math

tam_arq = int(input())
print(f"Transmitindo {tam_arq} bytes...")
tempo_total = 0

while tam_arq > 0:
    # calculando o total transferido em 5seg
    total_transferido = 0
    for _ in range(0,5):
        taxa = int(input())
        total_transferido += taxa
        if tam_arq - taxa == 0:
            tam_arq -= taxa
            break
    if tam_arq != 0:
        tam_arq -= total_transferido
        media_transf = total_transferido/5

        # calculando o tempo restante
        if media_transf != 0:
            tempo_restante = tam_arq / media_transf
            print(f"Tempo restante: {math.ceil(tempo_restante)} segundos.")
            tempo_total += tempo_restante
        else:
            print(f"Tempo restante: pendente...")
    else:
        print(f"Tempo total: {(math.ceil(tempo_total))+1} segundos.")
        break
