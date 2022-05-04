##################CORES#################
amarelo = '\033[0;33m'
azul = '\033[0;34m'
cinza = '\033[0;37m'
########################################
num = int(input("Digite um número para calcular seu fatorial: "))
fat = 1
print('{}{}!{}='.format(azul, num, cinza) , end='')
while num != 0:
    fat = fat * num
    print('{}'.format(num), end='')
    if num != 1:
        print('x', end='')
    num -= 1
print('={}{}'.format(amarelo, fat))
