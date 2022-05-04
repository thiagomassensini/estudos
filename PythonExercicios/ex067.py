n = 0
while True:
    n = int(input('Digite um numero para saber a taboada (Número negativo para sair): '))
    if n < 0:
        break
    for i in range(1, 10):
        print(f'{n} x {i} = {n*i}')

print('Programa tabuada encerrado. Volte sempre!')