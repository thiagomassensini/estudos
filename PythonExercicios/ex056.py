media = 0
idvelho = 0
novinhas = 0
for c in range(0, 4): for (i = 0; i < 10; i++)
    print('-' * 5, end='')
    print('{}ª PESSOA'.format(c+1), end='')
    print('-' * 5)
    nome = str(input("Nome: ")).strip().capitalize()
    idade = int(input('Idadade: '))
    sexo = str(input('Sexo (mulher/homem): ')).strip().lower()
    while sexo != 'mulher' and sexo != 'homem':
        sexo = str(input('Sexo inválido, digite novamente (mulhor ou homem): ')).strip().lower()
    media += idade
    if sexo == 'homem':
        if idade > idvelho:
            nomevelho = nome
            idvelho = idade
    else:
        if idade < 20:
            novinhas += 1
print('\n\nA media de idade do grupo: {}'.format(media/4))
print('O nome do homem mais velho é {}'.format(nomevelho))
print('Quantas mulhers tem menos de 20 anos: {}'.format(novinhas))
