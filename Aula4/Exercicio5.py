#Areas
print('Tamanho da area')
largura = float(input('Largura(M): '))
altura = float(input('Altura(M): '))
print('Tamanho do piso')
larguraP = float(input('Largura(Cm): '))
alturaP = float(input('Altura(cm): '))

#Equacao de area
area = (largura * altura) * 100
areaP = (larguraP * alturaP) / 100

#Variavel a mais
xpisos = 0

#Verifica a quantidade de pisos
while area >= areaP:
    area = area - areaP
    xpisos = xpisos + 1

#Valor a printar
if xpisos >= 100:
    print('Area maior de 100 pisos, a comprar de pisos: {}'.format(xpisos + 10))
elif xpisos >= 200:
    print('Area maior de 200 pisos, a comprar de pisos: {}'.format(xpisos + 20))
else:
    print('Area menor de 100 pisos, comprar: {}'.format(xpisos))
