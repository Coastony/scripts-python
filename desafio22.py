nome=str(input('Digite seu nome completo: ')).strip()
print('Analisando seu nome...')
print('Seu nome em maiusculas é {}'.format(nome.upper()))
print('Seu nome em minusculas é {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras'.format(len(nome)-nome.count(' ')))
print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))

'''separa=nome.split()
print('Seu primeiro nome tem {} letras'.format(separa[0], len(separa[0])))'''
