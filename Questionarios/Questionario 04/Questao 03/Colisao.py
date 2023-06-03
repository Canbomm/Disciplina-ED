tam,numchaves = [int(x) for x in input().split()]

ram = {}
for chave in range(0,tam):
    ram[chave] = "[x]"

valores = []
if numchaves > 0:
    valores = [int(x) for x in input().split()]

for val in valores:
    # primeiro caso: o valor tem uma posicao correta e ta vazio
    if ram.get(val) == "[x]":
        ram[val] = val
    else:
        # segundo caso: o valor tem uma posicao correta e nao ta vazio
        if val < tam:
            ram[val] = str(ram[val]) + f" -> {val}"
        else:
            pos = val%tam
            # terceiro caso: o valor tem uma posicao incorreta e ta vazio
            if ram.get(pos) == "[x]":
                ram[pos] = val
            else:
                # quarto caso: o valor tem uma posicao incorreta e nao ta vazio
                ram[pos] = str(ram[pos]) + f" -> {val}"

for chave in range(0,tam):
    print(str(chave) + " - " + str(ram[chave]))
