anilha = int(input())
pesos = []
while anilha != 0:
    pesos.append(anilha)
    anilha = int(input())
peso_desejado = int(input())

if pesos != []:
    # retirando a anilha do topo
    total_retirado = 1
    peso_topo = pesos.pop()
    total_peso = peso_topo
    print(f"Peso retirado: {peso_topo}")
    # retirando mais anilhas ate o desejado
    while peso_topo != peso_desejado:
        peso_topo = pesos.pop()
        print(f"Peso retirado: {peso_topo}")
        total_retirado += 1
        total_peso += peso_topo

    print(f"Anilhas retiradas: {total_retirado}")
    print(f"Peso total movimentado: {total_peso}")
else:
    print(f"Anilhas retiradas: 0")
    print(f"Peso total movimentado: 0")
