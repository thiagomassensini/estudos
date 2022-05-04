#a = int(input("Digite um valor: "))
#b = int(input("Digite um valor: "))
#c = int(input("Digite um valor: "))
#d = int(input("Digite um valor: "))
#tupla = a, b, c, d
tupla = (int(input('Digite um número: ')),
         int(input('Digite outro número: ')),
         int(input('Digite mais um número: ')),
         int(input('Digite o último número: ')))
cont = 0
print(f'Você digitou os valores {tupla}')
print((f'O valor 9 aparece {tupla.count(9)} vezes'))
#for i in range(0, 4):
#    if tupla[i] == 3:
#        print(f'O valor 3 apareceu na {tupla.index(3) + 1} posição')
#    elif tupla[i] == 4:
#        print('O numero 3 não apareceu em enhuma posição')
if 3 in tupla:
    print(f'O valor 3 apareceu na {tupla.index(3)+1}ª posição')
else:
    print('O valor 3 não foi digitado em nenhuma posição')
print('Os valores pares digitados foram ', end='')
for j in range(0, 4):
    if tupla[j] % 2 == 0:
        print(f'{tupla[j]} ', end='')
        cont += 1
    if j == 3 and cont == 0:
        print('nenhum')
