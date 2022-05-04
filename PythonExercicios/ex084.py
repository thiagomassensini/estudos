#lista1 = ['', 0]
lista1 = []
lista2 = []
cont = maior = menor = 0
while True:
    cont += 1
    #lista1[0] = str(input('Nome: '))
    lista1.append(str(input('Nome: ')))
    #lista1[1] = int(input('Peso: '))
    lista1.append(str(input('Peso: ')))
    lista2.append(lista1[:])
    if cont == 1:
        maior = menor = lista1[1]
    else:
        if lista1[1] > maior:
            maior = lista1[1]
        if lista1[1] < menor:
            menor = lista1[1]
    if str(input('Quer continuar? [S/N] ')).strip().upper() == 'N':
        break
print('-=' * 30)
print(f'Ao todo, você cadastrou {cont} pessoas.')
print(f'O maior peso foi de {maior:.1f}Kg. peso de ', end='')
for i in lista2:
    if i[1] == maior:
        print(f'{i[0]}... ', end='')
print(f'\nO menor peso foi de {menor:.1f}Kg. ', end='')
for j in lista2:
    if j[1] == menor:
        print(f'{j[0]}... ', end='')
