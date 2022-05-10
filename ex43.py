peso = float(input('Digite seu peso em (kg): '))
altura = float(input('Digite sua altura em (m): '))
imc = peso/(altura** 2)
print('Seu IMC é de: {:.1f}'.format(imc))
print('Seu status: ', end='')
if imc < 18.5:
    print('ABAIXO DO PESO')
elif imc >= 18.5 <= 25:
    print('PESO IDEAL')
elif imc >= 25 <=20:
    print('SOBREPESO')
elif imc >=30 <=40:
    print('OBESIDADE')
else:
    print('OBESIDADE MÓRBIDA')
