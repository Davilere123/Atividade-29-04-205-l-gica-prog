a = input("Digite algo: ")
b = input("De novo: ")

print("A = {}".format(a))
print("B = {}".format(b))

temp = b
b = a
a = temp

print("A = {}".format(a))
print("B = {}".format(b))
