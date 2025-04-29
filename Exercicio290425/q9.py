peso = float(input("Qual o seu peso? "))
altura = float(input("Qual a sua altura? "))

imc = peso / (altura ** 2)
print("O seu IMC é de {:.2f}".format(imc))

if imc < 18.5:
    print("Você está abaixo do peso!")
elif imc >=18.6 and imc < 25:
    print("Parabéns! Você está no peso ideal!")
elif imc >= 25 and imc < 30:
    print("Você está levemente acima do peso!")
elif imc >= 30 and imc < 35:
    print("Você está com obesidade em grau I!")
elif imc >= 35 and imc < 40:
    print("Você está com obesidade grau II (severa)!!")
else:
    print("Cuidado! Você está com obesidade grau III (mórbida)!!!")
