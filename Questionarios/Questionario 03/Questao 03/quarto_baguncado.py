pilha_roupas = []
quantas_entr = int(input())
for _ in range(0,quantas_entr):
    organizacao = input().split()
    pilha_roupas.append(organizacao)

min_total = 0
total_roupas = 0
for item in pilha_roupas[::-1]:
    print(f"Tipo: {item[0]}, Cor: {item[1]}")
    min_total += int(item[2])
    total_roupas += 1

print(f"Total de roupas: {total_roupas}")
print(f"Total de tempo: {min_total}")
