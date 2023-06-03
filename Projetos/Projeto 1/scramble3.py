def scramble(string):
    #print(string)
    index = 0
    tam_str = len(string)
    #print(f"Tamanho da string: {tam_str}")
    while index < tam_str:
        print(f"Trabalhando com a string: {string}")
        #print(f"eu sou o index: {index}, e esse é o tamanho da str atual: {tam_str}")

        char = string[index]
        nao_fechou = True
        # caso ja comece com um fecha
        if char == ")":
            string = string[:index] + string[index+1:]

        # encontrei um deslocamento
        if char == "(":
            sub_index = index
            # vou procurar onde fecha
            while sub_index < tam_str:
                #print(f"Estou no segundo while\nSub_index = {sub_index}\nString: {string}\n")
                sub_char = string[sub_index]
                if sub_char == ")":
                    # atualizando o fechou
                    nao_fechou = False
                    # fatiando a string
                    removida = string[:index] + string[sub_index+1:]
                    comeco = string[index+1:sub_index]
                    string = comeco + removida

                    # resetando o indice, atualizando o tam da str e parando o while
                    index = 0
                    tam_str -= 2
                    break

                sub_index += 1
            
            # conferindo se o negocio fechou
            if nao_fechou:
                print(f"Cai no if, com essa string: {string}")

        index += 1
    return string

#print(scramble("(Um(Dois)Tres"))
#print(scramble("3ce(1c)(6b2)f2e7e3f271df7(12acefea)537afae625b"))
#print(scramble(""))
#print(scramble(")yoroshikuonegaishimasu("))
print(scramble("(21f41(fc))))15((788f9083ca37bf7e1e(2a60f1e69abdd))))(()()()()()()"))
#print(scramble("batata(arroz)abacate"))
