var = 0
for c in range(0, 6):
    num = int(input('Digite um {}º numero: '.format(c+1)))
    if num % 2 == 0:
        var = var + num
print('A soma dos numeros pares da entrada é {}'.format(var))
