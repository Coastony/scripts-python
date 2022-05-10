n1 = float(input('Primeira Nota: '))
n2 = float(input('Segunda nota: '))
media = (n1 + n2) /2
print('Tirando {:.1f} e {:.1f}, a média do aluno é {:.1f}'.format(n1,n2,media))
if 7 > media >= 5:
    print('Você está APROVADO!')
elif media < 5:
    print('Você está em REPROVADO!')
elif media >= 7:
    print('Você está EM RECUPERAÇÃO!')