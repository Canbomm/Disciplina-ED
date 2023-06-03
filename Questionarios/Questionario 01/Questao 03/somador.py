entrada = "0"
total = 0

while True:
    entrada = input()
    if entrada.isnumeric():
        total += int(entrada)
    else:
        break

print(total)
