from datetime import date
ano = date.today().year
data = int(input('Digite o ano de nasscimento: '))
idade = ano - data
if idade <= 9:
    print('MIRIM')
elif idade <= 14:
    print('INFANTIL')
elif idade <=19:
    print('JUNIOR')
elif idade <= 25:
    print('SENIOR')
else:
    print('MASTER')