num=int(input('Digite um numero: '))
u=num//1%10
d=num//10%100
c=num//100
m=num//1000%10
print('Analisando o número {}'.format(num))
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))
