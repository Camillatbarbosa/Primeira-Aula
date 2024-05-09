#1
def exercicio1():
    variavel = input("Entre o seu nome: ")
    f = open('meu_arquivo_exercicio1.txt', 'w')
    f.write(variavel)
    f.close()

#2
def exercicio2():
    variavel2 = input("Escreva o nome de um arquivo de texto: ")
    f = open (variavel2, 'w')
    texto = input("Escreva o conteúdo a ser impresso no arquivo: ")
    f.write(texto)
    f.close()

#3
def exercicio3():
    f = open('arquivo-exemplo.txt', 'r')
    exemplo = f.read()

    f = open('novo_arquivo_exercicio3.txt', 'w')
    f.write(exemplo)
    f.close()

#4
def exercicio4():
    numero = input("Escreva um número da lista de exemplos: ")
    f = open('arquivo-exemplo.txt', 'r')
    for linha in f:
        partes = linha.split(';')
        if numero == partes [0]:
            print(partes [1])
    f.close()
