def removefecha(string):
    indice = 0
    for char in string:
        if char == ")":
            indice += 1
        else:
            break
    return string[indice:]

def scramble(string):
    #print(f"Recebi a string: {string}")
    subiu = False
    resultado = ""
    index = 0
    tam_str = len(string)
    while index < tam_str:
        #print(f"Rodei o while superior com a string: {string}")
        char = string[index]
        if char == "(":
            subiu = True
        if char == ")":
            subiu = False
        # tratando a string
        if subiu:
            subiram = ""
            sub_index = index
            while sub_index < tam_str:
                #print(f"Rodei o while inferior com a string: {string}")
                char = string[sub_index]
                if char == ")":
                    comeco = string[:index]
                    final = string[sub_index+1:]
                    final = removefecha(final)
                    string = subiram + comeco + final
                    tam_str = len(string)
                    print(f"Modifiquei a string, ficou assim: {string}")
                    break
                subiram += char
                print(subiram)

                sub_index += 1

        index += 1
    return string

print(scramble("(())ab((cd)ef((gh)"))
#print(scramble("ab((cd)ef((gh)"))
#print(scramble("cdabef((gh)"))
