maior = 0
menor = 0
for p in range(1,6):
    peso = float(input('Digite o peso da {}°: '.format(p)))
    if p == 1:
        maior = p
        menor = p
    else:
        if peso > maior:
            maior = peso
        if peso < maior:
            menor = peso
print('O maior peso lido foi de {}Kg'.format(maior))
print('O menor peso lido foi de {}'.format(menor))
