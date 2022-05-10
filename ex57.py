sexo = str(input('Digite seu sexo [M/F]: ')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Dados inválidos. Informe novamente! ')).strip().upper()
print('Sexo {} registrado com sucesso!'.format(sexo))