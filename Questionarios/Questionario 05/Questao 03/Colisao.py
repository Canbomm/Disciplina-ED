numero = int(input())
somados = []
for i in range(1,numero*2,2):
    somados.append(i)

def soma(numero,somados):
    if somados[1:] != []:
        print(str(somados[0]) + " + " + "soma(" + str(somados[1:]) + ")")
    else:
        print(str(somados[0]))
    if len(somados) > 1:
        soma(numero,somados[1:])
    return sum(somados)

resposta = soma(numero,somados)
print("---------------")
print(f"{numero} ** 2 == {resposta}")
