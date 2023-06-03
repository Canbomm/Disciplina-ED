divisores = {")":"(","]":"[","}":"{"}
abertos = {"(":False,"[":False,"{":False}

def duplicata(string):
    # string = {[(4-77)*21]}+((3*4)-(2*3))
    # string = (6)
    for index,char in enumerate(string[1:]):
        if (char == "(" or char == "[" or char == "{") and string[index] == char:
            abertos[char] = True
        elif divisores.get(char) and abertos[divisores[char]] and string[index] == char:
            return "A expressão possui duplicata."
    return "A expressão não possui duplicata."

print(duplicata("{[(4-77)*21]}+((3*4)+(4*3))"))
