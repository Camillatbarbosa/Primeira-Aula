print("Digite números para adicioar à lista (digie 'done' para terminar):")
numeros = []
while True:
    entrada = input()
    if entrada.lower() == 'done':
        break
    else:
        numeros.append(int(entrada))
print("Números coletados:", numeros)
