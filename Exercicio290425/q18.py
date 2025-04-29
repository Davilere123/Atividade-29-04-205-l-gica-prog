francisco = 1.5
sara = 1.1
ano = 0

while sara < francisco:
    sara = sara + 0.3
    francisco = francisco + 0.2
    ano += 1

print("Levará {} ano(s) para Sara ficar do mesmo tamanho de Francisco (com {:.2f} metros)".format(ano, sara))