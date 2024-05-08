# Nome: Alice - Idade: 25 - Cidade: São Paulo!
def questao1(nome, idade, cidade):
    print("Nome", nome, sep=' : ', end=' - ')
    print("Idade", idade, sep=' : ', end=' - ')
    print("Cidade", cidade, sep=' : ', end='!\n')

questao1("Eduardo", 30, "Rio de Janeiro")
questao1("Gustava", 25, "Niteroi")

def questao2():
    n1_texto = input("Entre com o primeiro número: ")
    n1 = float(n1_texto)

    n2 = float(input("Entre com o seguno número: "))

    op = input("Entre com a operação: ")

    if op == '+':
        print(n1 + n2)
    elif op == '-':
        print(n1 - n2)
    elif op == '/':
        print(n1 / n2)
    elif op == '*':
        print(n1 * n2)
    else:
        print('Operador desconhecido')

def questao3():
    texto = input("Entre com os itens de compras separados por vírgula: ")

    lista = texto.split(',')

    contador = 1
    for item in lista:
        print("Itm", contador, ":", item, sep=' ')
        contador +=1

def questao4():
    celsius = float(input('Entre a temperatura em Celsius: '))
    fahrenheit = (celsius * 9/5) + 32
    print("A temperatura em Fahrenheit é: ", fahrenheit)
    
def questao5():
    print("Entre com nomes. Digite sair para terminar.")

    nomes = []

    while True:
        entrada = input()

        if entrada.lower() == "sair":
            break
        else:
            nomes.append(entrada)

    for nome in nomes:
        print(nome)


