divisores = {")":"(","]":"[","}":"{"}
abertos = {"(":False,"[":False,"{":False}

def duplicata(string):
    # formatando a string do jeito: ((o))(o)
    # onde cada "o" representa uma operacao
    # string = [(4-77)]*21
    # string 2 = ((4-77))*21
    # string 3 = ((4-2)-2)
    # string 4 = [[(1+(2*3))]*2]
    # string 5 = [[((1+4)*2)*2]]
    # string 6 = [[[[2]]]]
    # string 7 = {[(4-77)*21]}+((3*4)+(4*3)) -> Não duplicata
    for index,char in enumerate(string[1:]):
        if (char == "(" or char == "[" or char == "{") and string[index] == char:
            abertos[char] = True
        elif divisores.get(char) and abertos[divisores[char]] and string[index] == char:
            return "A expressão possui duplicata."
    return "A expressão não possui duplicata."

quant_entradas = int(input())
for _ in range(0,quant_entradas):
    operacao = input()
    print(duplicata(operacao))
