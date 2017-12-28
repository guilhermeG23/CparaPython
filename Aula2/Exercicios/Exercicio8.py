#Melhorar
picole1 = str(input('Nome do Picole: '))
numero1 = int(input('Quantos: '))
quanto1 = float(input('Valor Picole: '))
picole2 = str(input('Nome do Picole: '))
numero2 = int(input('Quantos: '))
quanto2 = float(input('Valor Picole: '))
picole3 = str(input('Nome do Picole: '))
numero3 = int(input('Quantos: '))
quanto3 = float(input('Valor Picole: '))

#Melhorias na escolha e quantidas de picoles(Tive preguiça de fazer isso no C, melhor agora)
print('\nPicoles Escolhidos')
if numero1 >= 1:
    print(picole1)
else:
    quanto1 = 0
if numero2 >= 1:
    print(picole2)
else:
    quanto1 = 0
if numero3 >= 1:
    print(picole3)
else:
    quanto1 = 0

picoleFinal = (numero1 + numero2 + numero3)
valorFinal = (quanto1 + quanto2 + quanto3)
print('Numero de Picoles: {}\nValor: {:.2f}'.format(picoleFinal, valorFinal))
