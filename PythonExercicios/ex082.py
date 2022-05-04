lista = []
par = []
impar = []
while True:
    lista.append(int(input('Digite um número: ')))
    if str(input('Quer continuar? [S/N] ')).strip().upper() == 'N':
        break
for i in lista:
    if i % 2 == 0:
        par.append(i)
    else:
        impar.append(i)
print(f'A lista completa é {lista}')
print(f'A lista de pares é {par}')
print(f'A lista de ímpares é {impar}')
