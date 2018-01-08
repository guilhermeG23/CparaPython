#Calculadora
valor1 = float(input('Entre com o valor: '))
valorCal = str(input('Com a operação(+, -, /, *): '))
valor2 = float(input('Entre com o 2 valor: '))

if valorCal == '+':
    print('Valor final da Soma: {}'.format(valor1 + valor2))
elif valorCal == '-':
    print('Valor final da Subtração: {}'.format(valor1 - valor2))
elif valorCal == '/':
    print('Valor final da Divisão: {}'.format(valor1 / valor2))
elif valorCal == '*':
    print('Valor final da Multiplicação: {}'.format(valor1 * valor2))
else:
    print('Operador invalido')
