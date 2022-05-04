'''n = int(input('Digite um numero inteiro: '))
x = 1
print('-' * 12)
while (x <= 10):
    print('{} x {:2} = {:2}'.format(n, x, n * x))
    x = x + 1
print('-' * 12)'''

num = int(input('Digite um numero: '))
for c in range(0, 11):
    print('{} x {:2} = {:2}'.format(num, c, num * c))
