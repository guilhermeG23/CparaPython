#Entrada de dados
#Modelos de entrada de dados

#Sempre que se usar assim entrada é str(string)
x1 = input('Entrada 1: ')

#Mas como provar
print('Tipo da entrada: {}'.format(type(x1)))

#Como mudar o type da entrada, fazemos isso já no imput ou depois do input

#Primeiro no input
#Confirmando o str
x1 = str(input('Entrada 1: '))
#Entrada inteira
x2 = int(input('Entrada 2: '))
#Entrada Float
x3 = float(input('Entrada 3: '))

print('Entrada1: {}, Seu tipo {}'.format(x1, type(x1)))
print('Entrada2: {}, Seu tipo {}'.format(x2, type(x2)))
print('Entrada3: {}, Seu tipo {}'.format(x3, type(x3)))

#Agora convertendo as entrada para o tipo que você quer
x1 = input('Entrada 1: ')
x2 = input('Entrada 2: ')
x3 = input('Entrada 3: ')

#Convertendo
x1 = str(x1)
x2 = int(x2)
x3 = float(x3)

print('Entrada1: {}, Seu tipo {}'.format(x1, type(x1)))
print('Entrada2: {}, Seu tipo {}'.format(x2, type(x2)))
print('Entrada3: {}, Seu tipo {}'.format(x3, type(x3)))

#Ou "Muito mais trabalhoso"
x1 = input('Entrada 1: ')
x2 = input('Entrada 2: ')
x3 = input('Entrada 3: ')

print('Entrada1: {}, Seu tipo {}'.format(str(x1), type(str(x1))))
print('Entrada2: {}, Seu tipo {}'.format(int(x2), type(int(x2))))
print('Entrada3: {}, Seu tipo {}'.format(float(x3), type(float(x3))))
