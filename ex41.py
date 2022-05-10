from datetime import date
atual = date.today().year
ano = int(input('Em qual ano você nasceu? '))
idade = atual - ano
print('Você tem {} anos.'.format(idade))
if idade <= 9:
    print('Sua categoria é MIRIM!')
elif idade <= 14:
    print('Sua categoria é INFANTIL!')
elif  idade <= 19:
    print('Sua categoria é JUNIOR!')
elif idade <= 25:
    print('Sua categoria é  SENIOR!')
else:
    print('Sua categoria é MASTER!')