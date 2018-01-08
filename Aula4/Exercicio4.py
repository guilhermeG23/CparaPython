#Media
nota1 = float(input('Nota1: '))
nota2 = float(input('Nota2: '))
nota3 = float(input('Nota3: '))

media = (nota1 + nota2 + nota3) / 3

if media >= 7 and media <= 10:
    print('Aprovado: {:.2f}'.format(media))
elif media >= 4 and media <= 6.9:
    print('Vai de exame: {:.2f}'.format(media))
else:
    print('Reprovado: {:.2f}'.format(media))
