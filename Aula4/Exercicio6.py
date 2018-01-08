#Menu
print('-=' * 20)
print('Menu')
print('-=' * 20)
print('1 - Contas\n2 - Problemas Tecnicos\n3 - Reclamações\n4 - Falar com atendente\n0 - Sair')
print('-=' * 20)
while True:
    valor = int(input('Digite a Opção: '))

    if valor == 0:
        print('Saindo...')
        exit(0)
    elif valor == 1:
        print('Contas...')
    elif valor == 2:
        print('Problemas Tecnicos...')
    elif valor == 3:
        print('Reclamacoes')
    elif valor == 4:
        print('Falar com a atendente')
    else:
        print('Opção Não existe...\nTente novamente')
