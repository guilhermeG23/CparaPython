#Velocidade = distancia / tempo
dist = float(input('Entre com a distancia(\'KM\'): '))
tempo = float(input('Entre com o tempo(\'Hora\'): '))

#Operação
dist = dist / 1000
tempo = ((tempo / 60) / 60)
vm = dist / tempo

print('Velocidade Média: {:.2f} M/s'.format(vm))
