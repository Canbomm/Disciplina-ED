alfabeto = input("Por favor digite o alfabeto:\n")

index = 1
dicionario = "{"

for letra in alfabeto:
    dicionario += (str(index) + ":'" + letra + "',")
    index += 1

dicionario_final = dicionario[:-1] + "}"

print(dicionario_final)
