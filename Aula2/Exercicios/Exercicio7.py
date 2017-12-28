#Salario final
salario = float(input('Salario Bruto: '))
inss = ((salario / 100) * 8.5)
irrf = ((salario / 100) * 11)
print('Salario liquido: {}'.format((salario - inss) - irrf))
