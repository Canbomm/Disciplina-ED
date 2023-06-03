import sys
sys.setrecursionlimit(10**8)

sequencia = {0:"contado",1:"contado"}
fibonaccis = {0:0,1:1}

def fibonacci(num):
    if fibonaccis.get(num) != None:
        return fibonaccis[num]
    else:
        # criando a sequencia
        resposta = fibonacci(num-1) + fibonacci(num-2)
        if sequencia.get(resposta) == None:
            sequencia[resposta] = "contado"
        # salvando os ja calculados
        fibonaccis[num] = resposta
        return resposta

num = int(input())

# criando a fibonacci
if num < 3:
    fibonacci(8)
else:
    fibonacci(num*2)

# criando a nao fibonacci
contados = 0
printados = 0
nao_fibo = ""
while printados < num:
    contados += 1
    if sequencia.get(contados) == None:
        printados += 1
        nao_fibo += (str(contados) + ", ")

print(nao_fibo[:-2])
