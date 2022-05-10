'''co=float(input('Comprimento do cateto oposto: '))
ca=float(input('Digite o cateto adjacente: '))
h1=(co**2 +ca**2) **(1/2)
print('A hipotenusa vai medir {:.2f}'.format(h1))

OU
import math e depois h1=math.hypot(co,ca)'''

from math import hypot
co=float(input('Comprimento do cateto oposto: '))
ca=float(input('Comprimento do cateto adjacente: '))
h1=hypot(co,ca)
print('A hipotenusa vai medir {:.2f}'.format(h1))