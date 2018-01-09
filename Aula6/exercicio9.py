from random import randint
numeros = int(input('Quantos jogos voce quer fazer: '))

for x in range(numeros):
    print('Jogo: {}'.format(x + 1))
    print('Valores: {}  {}  {}  {}  {}  {}'.format(randint(1,60), randint(1,60), randint(1,60), randint(1,60), randint(1,60), randint(1,60)))
    

