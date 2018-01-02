#Triangulo
print('Entre com  os lados de um triangulo')
l1 = float(input('Lado1: '))
l2 = float(input('Lado2: '))
l3 = float(input('Lado3: '))

#variaveis
ab = l1 *1 l2
ac = l1 * l3
bc = l2 * l3

print('\nTipo de triangulo')
if ab == ac and ab == bc and bc == ac:   
    print('ab {}\nac {}\nbc {}'.format(ab, ac, bc))
    print('Equilatero')
elif ab == ac and bc != ab:
    print('ab {}\nac {}\nbc {}'.format(ab, ac, bc))
    print('isoceles')
elif ab != ac and ab != bc and bc != ac:
    print('ab {}\nac {}\nbc {}'.format(ab, ac, bc))
    print('Escaleno')
else:
    print('ab {}\nac {}\nbc {}'.format(ab, ac, bc))
    print('Nao registrado')
