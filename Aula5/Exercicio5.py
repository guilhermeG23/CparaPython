#Facilita muito usar o Range nestes casos
boi = int(input('Numero de Bois: '))
abatidos = 0
Nabatidos = 0
for numeros in range(boi):
    print('Boi {}'.format(numeros + 1))
    peso = float(input('Peso: '))

    if peso >= 150:
        print('Abate')
        abatidos += 1
    else:
        print('Engorda')
        Nabatidos += 1

print('Numero de Bois: {}\nNumero de Abates: {}\nEngorda: {}'.format(boi, abatidos,Nabatidos))
