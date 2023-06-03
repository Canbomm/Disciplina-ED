def removeabre(string):
    indice = 0
    for char in string:
        if char == "(":
            indice += 1
        else:
            break
    return string[indice:]

def scramble(string):
    index = 0
    while index < len(string):
        fecha = False
        char = string[index]
        if char == "(":
            sub_index = index + 1
            while sub_index < len(string):
                char = string[sub_index]
                if char == ")":
                    fecha = True
                    comeco = string[index+1:sub_index+1]
                    comeco = removeabre(comeco)
                    resultado = comeco + string[:index] + string[sub_index+1:]
                    string = resultado
                    index = 0
                    break
                sub_index += 1
            if not fecha:
                string = string[index+1:] + string[:index]
        index += 1
    resultado = ""
    for char in string:
        if char != ")" and char != "(":
            resultado += char
    return resultado

def dekey(lista):
    operacoes = int(lista[0])
    sequencia = lista[1:]
    # fazendo as operacoes
    for _ in range(0,operacoes):
        a = sequencia.pop(0)
        b = sequencia.pop(0)
        if a < b:
            sequencia.append(a)
            sequencia.insert(0,b)
        else:
            sequencia.append(b)
            sequencia.insert(0,a)
    return "".join(sequencia)

ordem_prioridade = {0:[],1:[],2:[],3:[],4:[],5:[]}
while True:
    # pegando a entrada
    entrada = input().split()

    # vendo se ele quer parar o programa
    if entrada[0] == "stop":
        orfaos = 0
        for chave in range(0,6):
            orfaos += len(ordem_prioridade[chave])
        print(f"{orfaos} processo(s) órfão(s).")
        break
    
    # vendo se ele quer executar algo e executando
    if entrada[0] == "go":
        for chave in range(0,6):
            if len(ordem_prioridade[chave]) > 0:
                comando = (ordem_prioridade[chave].pop(0)).split()
                # rodando o comando necessario
                if comando[0] == "scramble":
                    mensagem = "".join(comando[1:])
                    print(scramble(mensagem))
                elif comando[0] == "dekey":
                    print(dekey(comando[1:]))
                else:
                    print("Input invalido")
                break
    
    # vendo se ele quer dar enqueue em algo
    if entrada[0] == "enqueue":
        total_comandos = int(entrada[1])
        while total_comandos > 0:
            total_comandos -= 1
            comando = input().split()
            ordem_prioridade[int(comando[0])] += [" ".join(comando[1:])]
