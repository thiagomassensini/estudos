listagem = ('Lápis', 1.75, 'Borracha', 2,
            'Caderno', 15.90, 'Estojo', 25,
            'Transferidor', 4.20, 'Compasso', 9.90,
            'Mochila', 120.32, 'Canetas', 22.30,
            'Livro', 34.90)
print('-' *41, f'\n{"LISTAGEM DE PREÇOS":^40}\n', '-' *41)
#print(f'{"LISTAGEM DE PREÇOS":^40}')
#print('-' *41)
########################
for i in range(0, len(listagem), 2):
    print(listagem[i], end='')
    print('.' * (31 - len(listagem[i])), end='')
    print('R$', end='')
    print(f'{listagem[i + 1]:7.2f}')
print('-' *41)
##################### Ou
for pos in range(0, len(listagem)):
    if pos % 2 == 0:#quer dizer que os numeros pares são os nomes dos produtos e os impares os preços
        print(f'{listagem[pos]:.<30}', end='')
    else:
        print(f'R${listagem[pos]:>7.2f}')
print('-' *41)
######################### ou
for i in range(0, len(listagem), 2):
    print(listagem[i], '.' * (31 - len(listagem[i])), 'R$', f'{listagem[i + 1]:7.2f}')
print('-' *41)