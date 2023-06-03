numeros = []
palavras = []

frase = input().split()
for entrada in frase:
    if entrada.isnumeric():
        numeros.append(entrada)
    else:
        palavras.append(entrada)

print("Palavras:")
for item in palavras[::-1]:
    print(item)
print()
print("Numeros:")
for item in numeros[::-1]:
    print(item)
