for valor in [1, 2, 3, 4, 5]:
    print('Notas Aluno: {}'.format(valor))
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))
    n3 = float(input('Nota 3: '))
    print('\nAluno: {}, media: {}\n'.format(valor, (n1 + n2 + n3) / 3))
