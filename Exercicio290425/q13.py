nome = input("Qual o seu nome? ")
idade = int(input("Qual a sua idade? "))

print("Olá, {}!".format(nome))

if idade >= 18:
    print("Você é maior de idade.")
else:
    print("Você é menor de idade.")