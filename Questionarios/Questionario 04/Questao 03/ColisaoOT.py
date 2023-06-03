# fiz esse codigo baseado na ideia do professor de listas de listas
# nao sei se ele realmente e mais leve do que a versao original
# mas e mais simples de compreender e possui menos linhas

tamanho_ram,quant_chave = [int(x) for x in input().split()]
ram = [[] for _ in range(0,tamanho_ram)]

valores = []
if quant_chave > 0:
    valores = [int(x) for x in input().split()]

for val in valores:
    if val > tamanho_ram:
        novo_val = val%tamanho_ram
        ram[novo_val].append(val)
    else:
        ram[val].append(val)

for index,val in enumerate(ram):
    if val == []:
        print(f"{index} - [x]")
    else:
        if len(val) == 1:
            print(f"{index} - {int(val[0])}")
        else:
            print(f"{index} - {val[0]} -> {int(val[1:])}")
