def scramble(string):
    #print(f"Chamada da função com: {string}")
    index = 0
    while index < len(string):
        char = string[index]
        if char == "(":
            sub_index = index + 1
            while sub_index < len(string):
                char = string[sub_index]
                if char == ")":
                    #print(f"String default: {string}")
                    #print("Vou fatiar")
                    #print(string[index+1:sub_index+1])
                    #print(string[:index])
                    #print(string[sub_index+1:])
                    #print()
                    resultado = string[index+1:sub_index+1] + string[:index] + string[sub_index+1:]
                    #print(f"O resultado foi esse: {resultado}")
                    string = resultado
                    print(f"Passei nas verificacoes: {string}")
                    index = 0
                    break
                sub_index += 1
        index += 1
    resultado = ""
    for char in string:
        if char != ")" and char != "(":
            resultado += char
    return resultado

#print(scramble("(Um(Dois)Tres"))
#print(scramble("3ce(1c)(6b2)f2e7e3f271df7(12acefea)537afae625b"))
#print(scramble(""))
#print(scramble(")yoroshikuonegaishimasu("))
print(scramble("(21f41(fc))))15((788f9083ca37bf7e1e(2a60f1e69abdd))))(()()()()()()"))
