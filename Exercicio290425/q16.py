a = float(input("Lado a: "))
b = float(input("Lado b: "))
c = float(input("Lado c: "))

if a + b > c and b + c > a and a + c > b:
    if a == b == c:
        print("Esse triângulo é equilátero.")
    elif a == b or b == c:
        print("Esse triângulo é isóceles.")
    else:
        print("Esse triângulo é escaleno.")
else:
    print("Esse triângulo é inválido.")