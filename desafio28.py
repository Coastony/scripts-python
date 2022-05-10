'''n=0
d=str(input('Descubra qual numero eu pensei entre 0 e 5: '))
print('Você acertou' if n>0 else'Você errou')'''

from random import randint
from time import sleep
computador=randint(0,5) #faz o computador pensar
print('-=-' *20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-'*20)
jogador=int(input('Em que numero eu pensei? ')) #Jogador tenta adivinhar
print('Processando...')
sleep(3)
if jogador==computador:
    print('Parabens! Voc~e me venceu')
else:
    print('Ganhei Eu pensei no numero {} e nao no {}'.format(computador,jogador))
