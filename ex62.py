print('-=-' * 12)
print("PROGRESSÃO ARITIMÉTICA")
print('-=-' * 12)
primeiro = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{} -> '.format(termo), end='')
        termo += razao
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos voc~e quer mostrar a mais? '))
print('PA finalizada com {} termos!'.format(total))
