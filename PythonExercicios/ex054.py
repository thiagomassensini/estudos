from datetime import date
maior = 0
menor = 0
for c in range(1, 8):
    data = int(input('Digite o ano de nascimento da {}ª pessoa: '.format(c)))
    if date.today().year - data < 21:
        menor += 1
    else:
        maior += 1
print('{} não atingiram a mior idade e '.format(menor), end='')
print("{} já são maiores de idade. ".format(maior))