nome = str(input('Nome: ')).capitalize()
sexo = str(input('Sexo(M/F): ')).lower()
idade = int(input('Idade: '))
tempo = int(input('Contribuição: '))
prof = str(input('Professor(S/N): ')).lower()

final = idade + tempo

if prof == 's':
    if sexo == 'm':
        if final >= 85:
            print('{} tem {} anos de contribuição, professor aposentado'.format(nome, final))
        else:
            print('{} tem mais {} anos de trabalho a contribuir'.format(nome, 85 - final))
    elif sexo == 'f':
        if final >= 75:
            print('{} tem {} anos de contribuição, professora aposentada'.format(nome, final))
        else:
            print('{} tem mais {} anos de trabalho a contribuir'.format(nome, 75 - final))
    else:
        print('Sexo Indefinido')
elif prof == 'n':
    if sexo == 'm':
        if final >= 95:
            print('{} tem {} anos de contribuição'.format(nome, final))
        else:
            print('{} tem mais {} anos de trabalho a contribuir'.format(nome, 95 - final))
    elif sexo == 'f':
        if final >= 85:
            print('{} tem {} anos de contribuição'.format(nome, final))
        else:
            print('{} tem mais {} anos de trabalho a contribuir'.format(nome, 85 - final))
    else:
        print('Sexo Indefinido')
else:
    print('Indefinido')
