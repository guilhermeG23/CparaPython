for cliente in [1, 2, 3]:
    print('Info cliente: {}'.format(cliente))
    altura = float(input('Altura: '))
    peso = float(input('Peso: '))
    operacao = peso / (altura ** 2)

    if operacao < 18.5:
        print('IMC: {:.2f}'.format(operacao))
        print('Abaixo do peso normal')
    elif operacao >= 18.5 and operacao <= 24.9:
        print('IMC: {:.2f}'.format(operacao))
        print('Peso Normal')
    elif operacao >= 25 and operacao <= 29.9:
        print('IMC: {:.2f}'.format(operacao))
        print('Excesso de Peso')
    elif operacao >= 30 and operacao <= 34.9:
        print('IMC: {:.2f}'.format(operacao))
        print('Obesidade I')
    elif operacao >= 35 and operacao <= 39.9:
        print('IMC: {:.2f}'.format(operacao))
        print('Obesidade II')
    else:
        print('IMC: {:.2f}'.format(operacao))
        print('Obesidade III')
