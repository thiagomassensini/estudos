import math
print('_*_' * 15)
print('Programa \033[1;33mBase de Converssão\033[m')
print('_*_' * 15)
num = int(input('Digite um numero inteiro para converssão: '))
print('_*_' * 15)
print('Você digitou o numero {}, o que deseja fazer com ele?'.format(num))
opc = int(input('Digite 1 para Binário\nDigite 2 para Octal\nDigite 3 para Hexadecimal\n:'))
print('_*_' * 15)
if opc == 1:
    print('{} em binário é {} !'.format(num, bin(num)[2:]))
    print('{} em binario é {:b}'.format(num, num))
elif opc == 2:
    print('{} em octal é {} !'.format(num, oct(num)[2:]))
    print('{} em octal é {:o}'.format(num, num))
elif opc == 3:
    print('{} em hexadecimal é {} !'.format(num, hex(num)[2:]))
    print('{} em hexadecimal é {:x}'.format(num, num))
else:
    print('Opção inválida!')
