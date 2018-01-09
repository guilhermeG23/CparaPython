#Calculo Fatorial
valor = int(input('Calculo Fatorial: '))
final = 1
for x in range(valor, 0, -1):
    final = x * final
    print('Valor Atual: {}\nValor Fatorial Atual: {}'.format(x, final))
