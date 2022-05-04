from datetime import date
hoje = date.today().year
data = int(input('Digite seu ano de nascimento: '))
idade = hoje - data
print('Quem nasceu em {} tem {} anos em {}.'.format(data, idade, hoje))
if idade < 18:
    print('Vai se alistar em {}'.format(data + 18))
    print('Faltam {} anos'.format(18 - idade))
elif idade == 18:
    print('Hora de se alistar')
else:
    print('Passou do tempo')
    print('Você deveria ter se alistado em {}.'.format(data + 18))
    print('Deveria ter se alistado a {} anos atrás '.format(idade - 18))
