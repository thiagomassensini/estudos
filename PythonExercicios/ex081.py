lista = []
while True:
    lista.append(int(input('Digite um valor: ')))
    opc = str(input('Quer continuar? [S/N] ')).upper().strip()
    if opc == 'N':
        break
lista.sort(reverse=True)
print('-=' *20)
print(f'Você digitou {len(lista)} elementos.')
print(f'Os valores em ordem decrescente são {lista}')
if 5 not in lista:
    print('O valor 5 não foi encontrado na lista!')
else:
    print('O valor 5 foi encontrado na lista nas posções: ', end='')
    for c, i in enumerate(lista):
        if 5 == i:
            print(f'{c}...', end='')