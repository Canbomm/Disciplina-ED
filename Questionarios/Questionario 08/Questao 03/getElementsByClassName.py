def getElementsByClassName(raiz,classe):
    classes = classe.lower().split()
    achados = []
    for nome,elemento in raiz.items():
        if elemento.get('class') != None:
            if elemento['class'].lower() in classes:
                achados.append(nome)
        if elemento.get('children') != None:
            achados += getElementsByClassName(elemento['children'],classe)
    return achados

#raiz = {'h1': {'text': 'Lorem ipsum.', 'class': 'header', 'children': {'p1': {'text': 'Dolor sit amet.', 'class': 'p'}, 'p2': {'text': 'Consectetur adipiscing elit.', 'class': 'P'}}}}
#print(sorted(getElementsByClassName(raiz, 'p header')))
