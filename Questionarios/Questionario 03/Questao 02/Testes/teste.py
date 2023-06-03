import random

print("Esse programa foi feito para testar casos muito grandes na questao")
alfabeto = {1:'a',2:'b',3:'c',4:'d',5:'e',6:'f',7:'g',8:'h',9:'i',10:'j',11:'k',12:'l',13:'m',14:'n',15:'o',16:'p',17:'q',18:'r',19:'s',20:'t',21:'u',22:'v',23:'w',24:'x',25:'y',26:'z'}

tamanho = int(input("Qual o tamanho do arquivo:\n"))
saida = ""

for i in range(0,tamanho):
    chave = random.randint(1,26)
    e_numero = random.randint(0,1)

    if e_numero == 0:
        letra = alfabeto[chave]
        saida += (letra + " ")
    else:
        saida += (str(chave) + " ")
    
    print(f"Rodando o programa, operacao {i} de {tamanho}")

nome_arq = ""
for i in range(0,5):
    chave = random.randint(1,26)
    letra = alfabeto[chave]
    nome_arq += letra

print(f"Colocando sua geracao em um arquivo chamado: {nome_arq}")
f = open(nome_arq,"x")
f.write(saida)
f.close()
