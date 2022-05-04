opc = 'S'
cont = maior = menor = media = 0
while opc == 'S':
    opc = ''
    num = int(input('Digite o valor: '))
    if cont == 0:
        maior = menor = num
    elif maior < num:
        maior = num
    elif menor > num:
        menor = num
    media += num
    while opc != 'S' and opc != 'N':
        opc = str(input('Deseja digitar mais um valor? (S|N): ')).upper().strip()
        if opc != 'S' and opc != 'N':
            print('Valor inválido!')
    cont += 1
print('A media entre todos os valores digitados foi {}'.format(media // cont))
print('O maior valor diigitado foi {}'.format(maior))
print('O menor valor digitado foi {}'.format(menor))

