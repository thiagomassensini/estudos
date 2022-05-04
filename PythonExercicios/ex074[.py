from random import randint
a = randint(0, 10) , randint(0, 10) , randint(0, 10) , randint(0, 10) , randint(0, 10)
maior = menor = cont = 0
for i in range(0, 5):
    if cont == 0 or maior < a[i]:
        maior = a[i]
    if cont == 0 or menor > a[i]:
        menor = a[i]
    cont += 1
########### Desse jeito ou do outro
print(f'Os valores sorteados foram ', end='')
for i in range(0, 5):
    print(f'{a[i]} ', end='')
print('')
############ Do jeito de cima ou desse aqui em baixo
print(f'Os valores sorteados foram ', end='')
for j in a:
    print(f'{j} ', end='')
print('')
#############################################
print(f'O maior valor sorteado foi {maior}')############ Desse jeito ou do outro
print(f'O menor valor sorteado foi {menor}')####################################
####### outro VVVVVVVVVVVVVVVVV
print(f'O maior valor sorteado foi {max(a)}')##################Desse outro aqui!!!
print(f'O menor valor sorteado foi {min(a)}')#####################################
