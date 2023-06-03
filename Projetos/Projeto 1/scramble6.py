def scramble(string):
    print(f"Chamada da função com: {string}")
    direction = 1
    group_index = 0
    resultado = []
    for char in string:
        if char == "(":
            direction = 0
            group_index = 0
        elif char == ")":
            direction = 1
        else:
            if direction == 1:
                resultado.append(char)
            else:
                resultado.insert(group_index,char)
                group_index += 1
    return "".join(resultado)

#print(scramble("(Um(Dois)Tres"))
#print(scramble("3ce(1c)(6b2)f2e7e3f271df7(12acefea)537afae625b"))
#print(scramble(""))
#print(scramble(")yoroshikuonegaishimasu("))
#print(scramble("(21f41(fc))))15((788f9083ca37bf7e1e(2a60f1e69abdd))))(()()()()()()"))
#print(scramble("(())ab((cd)ef((gh)"))
#print(scramble("()"))
#print(scramble("ab(cd"))
print(scramble("a((b)c)d"))
