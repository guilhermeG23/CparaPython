#Fahrenheit
temp = float(input('Entre com a temperatura em Celsius: '))

#Duas forma de fazer a Operação
#Primeira com variavel
fahr = (temp * 1.8) + 32
print('Temperatura em Fahrenheit: {:.2f}'.format(fahr))

#Sem variavel final
print('Temperatura em Fahrenheit: {:.2f}'.format((temp * 1.8) + 32
))
