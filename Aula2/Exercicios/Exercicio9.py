"""
Jeito do exercico
car = int(input('Quanto gerou de lucro: '))
print('Salario final: {}'.format(((car / 100) * 5) + 900)) 
"""

#Meu jeito

car = int(input('Quantos carros vendeu: '))

#Valores pre-definidos para por ser usado
x = 0
final = 0

#While para garantir a somatoria final
while x < car:
    soma = float(input('Valor do carro: '))
    final += soma
    x += 1
    
#Conta final
final = ((final / 100) * 5 + 900)
print('Salario final: {}'.format(final)) 
