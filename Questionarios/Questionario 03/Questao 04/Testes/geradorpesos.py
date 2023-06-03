import random

total = int(input("Quantos pesos você deseja?\n"))
maior = int(input("Qual maior peso desejado?\n"))
menor = int(input("Qual menor peso desejado?\n"))

saida = ""
for _ in range(0,total):
    saida += str(random.randint(menor,maior)) + "\n"

nome_arq = input("Qual nome do arquivo voce deseja utilizar?\n")

print(f"Colocando sua geracao em um arquivo chamado: {nome_arq}")
f = open(nome_arq,"x")
f.write(saida)
f.close()
