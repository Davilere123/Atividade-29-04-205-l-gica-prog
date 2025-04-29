aluno = str(input("Nome do aluno: "))
aluno = aluno.upper()

nota1 = float(input("Nota 1: "))
nota2 = float(input("Nota 2: "))
nota3 = float(input("Nota 3: "))
nota4 = float(input("Nota 4: "))

media = (nota1 + nota2 + nota3 + nota4) / 4

print("ALUNO: {}".format(aluno))
print("MÉDIA: {:.1f}".format(media))

if media >= 7:
    print("SITUAÇÃO: APROVADO")
else:
    print("SITUAÇÃO: REPROVADO")