#1
def imprimir_informações(nome, idade, cidade):
    print("nome:", nome, sep=" ", end=" - ")
    print("idade:", idade, sep=" ", end=" - ")
    print("cidade:", cidade, end="!\n\n")
imprimir_informações("Camilla", 21, "Rio")

#2
def operacao_desejada():
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    operacao = str(input("Digite a operação desejada: "))
    if operacao == "+":
        print(num1 + num2)
    elif operacao == "-":
        print(num1-num2)
    elif operacao == "*":
        print(num1*num2)
    elif operacao == "/":
        print(num1/num2)

#3
def itens_lista_de_compras():
    itens = input("Insira os itens de sua lista de compras, separados por vírgula: ").split(',')
    print("itens: ", itens)

#4
def conversão_temperatura():
    grausc = float(input("Digite a temperatura em graus celsius: "))
    grausf = (grausc * 9/5) + 32
    print("A temperatura em graus farenheit é igual a ", grausf)

#5
def nomes():
    print("Digite nomes para adicionar à lista (digite 'sair' para terminar):")
    nomes = []
    while True:
        entrada = input()
        if entrada.lower() == 'sair':
            break
        else:
            nomes.append(entrada)
    for n in nomes:
        print("Nomes coletados:", n)
