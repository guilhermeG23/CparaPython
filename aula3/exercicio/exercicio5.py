aumento = float(input('Digite seu salario para receber seu aumento: '))
if aumento < 1200:
    print('Seu salario {}\nvoce teve 20% de aumento\nsalario final {}'.format(aumento, (((aumento / 100) * 20) + aumento)))
if aumento >= 1200 and aumento < 2000:
    print('Seu salario {}\nvoce teve 15% de aumento\nsalario final {}'.format(aumento, (((aumento / 100) * 15) + aumento)))
elif aumento > 2000:
    print('Seu salario {}\nvoce teve 8% de aumento\nsalario final {}'.format(aumento, (((aumento / 100) * 8) + aumento)))
