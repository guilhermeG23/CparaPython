#IMC
peso = float(input('Entre com seu Peso: '))
altura = float(input('Entre com a altura: '))

imc = peso / (altura ** 2)
if imc < 18.5:
    print('Sua media: {:.2f}'.format(imc))
    print('Abaixo do Peso')
elif imc >= 18.5 and imc <= 24.9:
    print('Sua media: {:.2f}'.format(imc))
    print('Peso normal')
elif imc >= 25 and imc <= 29.9:
    print('Sua media: {:.2f}'.format(imc))
    print('Excesso de peso')
elif imc >= 30 and imc <= 34.9:
    print('Sua media: {:.2f}'.format(imc))
    print('Obsidade 1')
elif imc >= 35 and imc <= 39.9:
    print('Sua media: {:.2f}'.format(imc))
    print('Obsidade 2')
else:
    print('Sua media: {:.2f}'.format(imc))
    print('Obsidade 3')
