def fatorial(num):
    if num > 1:
        resposta = num * fatorial(num-1)
        if resposta >= 2357:
            return resposta % 2357
        else:
            return resposta % 2357
    else:
        return 1
        