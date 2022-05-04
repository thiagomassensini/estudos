from time import sleep
print('Programa que lê dois valores')
va1 = float(input("Primeiro valor: "))
va2 = float(input("Segundo valor: "))
menu = 0
while menu != 5:
    print('[1] somar\n[2] multiplicar\n[3] maior\n[4] novos números\n[5] sair do programa')
    menu = int(input('Digite a opção desejada: '))
    if menu == 1:
        print('A soma entre {} e {} é {}'.format(va1, va2, va1+va2))
        sleep(2)
    if menu == 2:
        print('A multiplicação de {} com {} é {}'.format(va1, va2, va1*va2))
        sleep(2)
    if menu == 3:
        if va1 > va2:
            print('O maior numero é o primeiro, {}'.format(va1))
            sleep(2)
        elif va1 < va2:
            print('O maior numero é o segundo. {}'.format(va2))
            sleep(2)
        else:
            print('Os números são iguais')
            sleep(2)
    if menu == 4:
        print('-=-' * 20)
        print('Você optou por novos números!')
        sleep(1)
        va1 = float(input("Primeiro valor: "))
        va2 = float(input("Segundo valor: "))
sleep(1)
print('*_' * 25)
sleep(1)
print('Fim')