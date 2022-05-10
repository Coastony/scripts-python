from random import randint
comp = randint(0, 10)
print('Vou pensar em um número entre 0 a 10.')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual é seu palpite? '))
    palpites += 1
    if jogador == comp:
        acertou = True
    else:
        if jogador < comp:
            print('Mais...Tente novamente!')
        elif jogador > comp:
            print('Menos...Tente novamente!')
print('Acertou com {} tentativas!'.format(palpites))
