horas = int(input('Horas trabalhadas durante a semana: '))
valor = float(input('Valor da Hora: '))

final = horas * valor
b1 = (final / 100) * 50
if horas <= 40:
    print('Salario: {}'.format(final))
elif horas > 40 and horas <= 60:
    print('Salario: {}'.format(final + b1))
else:
    print('Salario: {}'.format(final * 2))
