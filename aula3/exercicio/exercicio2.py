#Medias
m1 = float(input('Nota 1: '))
m2 = float(input('Nota 2: '))
m3 = float(input('Nota 3: '))
#Modo de fazer o if, neste caso e mais facil fazer com uma variavel final para evitar repetir o processo
mf = (m1 + m2 + m3) / 3
#Dava pra ter feito isso2
#if ((m1 + m2 + m3) / 3) >= 6:
if mf >= 6:
    print('Sua Media: {}'.format(mf))
    print('Media maior ou igual a 6')
elif mf >= 4 and mf <=5.9:
    print('Sua Media: {}'.format(mf))
    print('Media ficou entre 4 a 5.9, tem exame pra fazer')
else:
    print('Sua Media: {}'.format(mf))
    print('Media menor que 6')
