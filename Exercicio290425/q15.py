import datetime

idade = int(input("Digite o ano em que você nasceu: "))
ano = datetime.date(idade, 1, 1)
hoje = datetime.date.today()

calc = (hoje - ano).days

anos = calc // 365
resto = calc % 365
meses = resto // 30
dias = resto % 30


print("Você tem {} ano(s), {} mese(s) e {} dia(s)".format(anos, meses, dias))

