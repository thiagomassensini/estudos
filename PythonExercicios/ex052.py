#sabe se o numero é primo
num = int(input('Digite um numero: '))
cont = 0
for c in range(1, num+1):
    if num % c == 0:
        print('\033[0;33m', end=' ')
        cont += 1
    else:
        print('\033[0;31m', end=' ')
    print('{} \033[m'.format(c), end='')
print('\nO número {} foi divispivel por {} vezes'.format(num, cont))
if cont == 2:
    print('E por isso ele È PRIMO!')
else:
    print('E por isso ele NÂO È PRIMO!')

############
'''
#sabe se o numero é primo
num = int(input('Digite um numero: '))
primo = True
cont = 2
print('\033[0;33m1\033[m', end=' ')
for c in range(2, num+1):
    if c != num:
        if num % c == 0:
            print('\033[0;33m{}\033[m'.format(c), end=' ')
            cont += 1
            primo = False
        else:
            print('\033[0;31m{}\033[m'.format(c), end=' ')
print('\033[0;33m{}\033[m'.format(num))
print('O número {} foi divispivel por {} vezes'.format(num, cont))
if primo == True:
    print('E por isso ele È PRIMO!')
else:
    print('E por isso ele NÂO È PRIMO!')
'''