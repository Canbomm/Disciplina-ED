num_discos,origem,destino,temp = input().split()
num_discos = int(num_discos)

min_mov = (2**num_discos) - 1

def jogada(pecas,origem,destino,temp):
    if pecas <= 0:
        return
    if pecas == 1:
        print(f"Mover de {origem} para {destino}.")
        return
    
    jogada(pecas-1,origem,temp,destino)
    print(f"Mover de {origem} para {destino}.")
    jogada(pecas-1,temp,destino,origem)

jogada(num_discos,origem,destino,temp)
