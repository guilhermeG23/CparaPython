#modulo datetime
from datetime import datetime

idade = int(input('Digite o ano de seu nascimento: '))

#Resultado do modulo time
anoAtual = datetime.now().year

final = anoAtual - idade

#IF ELSE

if final <= 3:
    print('Bebe: {} Anos'.format(final))
elif final >= 4 and final <= 13:
    print('Criança: {} Anos'.format(final))
elif final >= 14 and final <= 18:
    print('Adolescente: {}'.format(final))
elif final >= 19 and final <= 59:
    print('Adulto: {}'.format(final))
elif final >= 60 and final <= 100:
    print('Idoso: {}'.format(final))
elif final >= 101 and final <= 127:
    print('Imortal(Silvio santos) {}'.format(final))
else:
    print('Valor incorreto')
