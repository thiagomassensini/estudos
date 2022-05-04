num1 = int(input('Digite o um numero: '))
num2 = int(input('Digite o outro  numero: '))
num3 = int(input('Digite o outro numero: '))
if num1 > num2:
    if num1 > num3:
        maior = num1
elif num1 < num3:
    menor = num1
if num2 > num1:
    if num2 > num3:
        maior = num2
elif num2 < num3:
    menor = num2
if num3 > num1:
    if num3 > num2:
        maior = num3
elif num3 < num2:
    menor = num3
print('O maior numero é \033[0;34;41m{}\033[m e o menor é \033[1;33m{}\033[m'.format(maior, menor))
