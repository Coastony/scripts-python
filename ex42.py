seg1 = float(input('Primeiro segmento: '))
seg2 = float(input('SEgundo segmento: '))
seg3 = float(input('Terceiro segmento: '))
if seg1 < seg2 + seg3 and seg2 < seg1 + seg3 and seg3 <seg1 + seg2:
    print('Os segmentos acima podem formar um triângulo.', end='')
    if seg1 == seg2 == seg3:
        print('EQUILÁTERO!')
    elif seg1 != seg2 != seg3:
        print('ESCALENO!')
    else:
        print('ISÓSCELES!')
else:
    print('Os segmentos acima não podem formar um triângulo.')
