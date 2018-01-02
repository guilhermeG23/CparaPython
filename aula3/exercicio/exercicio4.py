salario = float(input('Entre com seu salario: '))
if salario > (780 * 15):
    print('Seu salario: {}\nMais de 15 salarios minimos'.format(salario))
elif salario >= (780 * 5) and salario <= (salario * 15):
    print('Seu salario: {}\nEntre 5 a 15 salarios minimos'.format(salario))
elif salario >= (780 * 3) and salario < (salario * 5):
    print('Seu salario: {}\nEntre 3 a 5 salarios minimos'.format(salario))
elif salario > 780 and salario < (salario * 3):
    print('Seu salario: {}\nEntre 1 a 3 salarios minimos'.format(salario))
else:
    print('Seu salario: {}\n1 salario minimo'.format(salario))
