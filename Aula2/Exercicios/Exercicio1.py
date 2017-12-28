#Entrada de notas
nota1 = float(input('Nota1: '))
nota2 = float(input('Nota2: '))
nota3 = float(input('Nota3: '))

#Duas formas de fazer a media
media = (nota1 + nota2 + nota3) / 3
print('Sua média foi: {:.2f}'.format(media))

#Ou "Sem variavel final"
print('Sua média foi: {:.2f}'.format((nota1 + nota2 + nota3) / 3
))
