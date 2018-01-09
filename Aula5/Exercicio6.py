quantos = int(input('Numero de entradas: '))
final = 0
positivos = 0
negativos = 0
for x in range(quantos):
    x += 1
    entrada = float(input('valores: '))

    if entrada >= 0:
        final = final + entrada
        positivos += 1
    else:
        negativos += 1

print('Positivos: {}\nNegativos: {}\nSoma Final: {:.2f}'.format(positivos, negativos, final))
        
        
