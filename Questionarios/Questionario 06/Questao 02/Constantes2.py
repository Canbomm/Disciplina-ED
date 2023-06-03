# ordem crescente de valores decimais
def org_Sarogatip(sequencia):
    # pegando os valores
    valores_dec = []
    for ind in range(1,len(sequencia),2):
        valor = sequencia[ind].split(".")
        valor_dec = int(valor[1])
        valores_dec.append(valor_dec)
    
    print(valores_dec)
    
    # organizando pela casa decimal
    organizados = ordena(valores_dec,True)
    return print(organizados)

def ordena(sequencia,crescente):
    # criterio de parada
    if len(sequencia) < 1:
        return sequencia
    # ordenando de fato
    else:
        criterio = sequencia.pop()
        valores_menores = []
        valores_maiores = []

        for num in sequencia:
            if num > criterio:
                valores_maiores.append(num)
            else:
                valores_menores.append(num)
        
        if crescente:
            return ordena(valores_menores,True) + [criterio] + ordena(valores_maiores,True)
        else:
            return ordena(valores_maiores,False) + [criterio] + ordena(valores_menores,False)

def procura_item(lista,procurado):
    for item in lista:
        if item == procurado:
            return True
    return False

# area para testes

# 1 caso
print(org_Sarogatip(["phi","1.62","e","2.71"]))

print("-------")

# 2 caso
print(org_Sarogatip(["g","9.81","e","2.71","phi","1.62"]))

print("-------")

# 3 caso
print(org_Sarogatip(["pi","3.14","i","-1.00","Geldof","23.14"]))
