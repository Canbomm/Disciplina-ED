# esse codigo aqui ta mais correto do que o que a questao pedia kkkk
# na questao a operacao: "[(4-77)]*21" nao possui duplicata
# mas na verdade existe um colchetes desnecessario ali

def duplicata(string):
    # formatando a string do jeito: ((o))(o)
    # onde cada "o" representa uma operacao
    formatada = ""
    comeco = False
    # percorrendo a string
    for char in string:
        if char == "(" or char == "[" or char == "{":
            formatada += char
            comeco = True
        elif char == ")" or char == "]" or char == "}":
            formatada += char
        else:
            if comeco:
                formatada += "o"
                comeco = False
    print(formatada)
    # removendo cada (o) para verificar se ha duplicatas
    while True:
        tem_o = False
        for index,char in enumerate(formatada):
            if char == "o" and (formatada[index-1] == "(" or formatada[index-1] == "[" or formatada[index-1] == "{") and (formatada[index+1] == ")" or formatada[index+1] == "]" or formatada[index+1] == "}"):
                tem_o = True
                formatada = (formatada[:index-1] + "o" + formatada[index+2:])
                print("dentro do while",formatada)
                break
        if not tem_o:
            break
    # caso a formatada tenha qualquer coisa, entao ha duplicatas
    print(formatada)
    if formatada != "o":
        return "A expressão possui duplicata."
    else:
        return "A expressão não possui duplicata."

quant_entradas = int(input())
for _ in range(0,quant_entradas):
    operacao = input()
    print(duplicata(operacao))
