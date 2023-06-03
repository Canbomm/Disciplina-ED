def scramble(string):
    #print(f"Chamada da função: {string}")
    ordens = {}
    ordem = 0
    for char in string:
        if char == "(":
            ordem += 1
        if char == ")":
            if ordem > 0:
                ordem -= 1
        # adicionando no dicionario
        if ordens.get(ordem) != None:
            if char != "(" and char != ")":
                ordens[ordem] += [char]
        else:
            if char != "(" and char != ")":
                ordens[ordem] = [char]
    # tratando o dicionario
    # print(f"Chamada da string:\n{string}\n\nDic: {ordens}\n")
    chaves = list(ordens.keys())
    resultado = ""
    for chave in chaves[::-1]:
        resultado += "".join(ordens.get(chave))
    return resultado

#print(scramble("Mensagem(Eis)Secreta"))
#print(scramble("(Um(Dois)Tres"))
print(scramble("3ce(1c)(6b2)f2e7e3f271df7(12acefea)537afae625b"))
