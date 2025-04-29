prod = float(input("Qual o valor do produto(em reais)? "))

print("FORMAS DE PAGAMENTO:")
print("1 - À vista (dinheiro ou PIX) - 15% de desconto")
print("2 - À vista no cartão - 10% de desconto")
print("3 - Parcelado em 2x")
print("4 - Parcelado em 3x ou mais - 10% de juros")

escolha = int(input("Escolha uma opção: "))

if escolha == 1:
    print("Opção 1 selecionada")
    desc = prod * 0.15
    prod = prod - desc
    print("Preço final: {}".format(prod))
elif escolha == 2:
    print("Opção 2 selecionada")
    desc = prod * 0.1
    prod = prod - desc
    print("Preço final: {}".format(prod))
elif escolha == 3:
    print("Opção 3 selecionada")
    print("Preço final: {}".format(prod))
elif escolha == 4:
    print("Opção 4 selecionada")
    aum = prod * 0.1
    prod = prod + aum
    print("Preço final: {}".format(prod))
else:
    print("Opção inválida. Tente novamente.")