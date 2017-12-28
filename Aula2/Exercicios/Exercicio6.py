import math

a = float(input('Entre com A: '))
b = float(input('Entre com B: '))
c = float(input('Entre com C: '))

positivo = ((-b + math.sqrt((b ** 2) - 4 * a * c)) / 2 * a)
negativo = ((-b - math.sqrt((b ** 2) - 4 * a * c)) / 2 * a)
print('Valor final: S = {},{}'.format(negativo, positivo))
