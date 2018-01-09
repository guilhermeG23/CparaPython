#Valores pares  de 1 a 500 mais somatorios dos proprios
soma = 0
#Uso do Range
for x in range(2, 500, 2):
    soma = x + soma
    print(x)
print(500)
print('Soma dos 500 valores pares positivos: {}'.format(soma + 500))
