num = int(input("Digite um número para ver sua tabuada: "))
print("Tabuada de {}".format(num))

for c in range(1, 11):
    print("{} * {} = {}".format(num, c, num * c))