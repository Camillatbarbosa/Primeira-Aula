print("Olá", "mundo", sep="-")

print("Olá", "Python", end="!\n")

print("18", "04", "2023", sep="/")

print("nome", "sobrenome", "email", sep=";")

#Contuinuando impressões na mesma linha
print("Loading", end=" ")
print("(OK)") #Saída: Loading (OK)

nome = input("Entre com o seu nome: ")
print("Olá", nome)

itens = input("Digite itens separados por vírgula: ").split(',')
print("itens: ", itens)

idade = int(input("Digite sua idade: "))

idade = int(idade)

print("Daqui a cinco anos, você terá", idade + 5, "anos.")
