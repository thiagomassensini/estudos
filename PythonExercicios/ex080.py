lista = []
for c in range(0, 5):
    n = int(input('Digite um valor: '))
    if c == 0 or n > lista[-1]:
        lista.append(n)
        print('Adicionado no final da lsita!')
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f'Adicionado na posição {pos} da lista!')
                break
            pos += 1
print('-=' *30)
print(f'Os valores digitados em ordem foram {lista}')
'''lista = []
for i in range(0, 5):
    pb = False
    n = int(input('Digite um valor: '))
    if len(lista) == 0:
        lista.append(n)
        print('Adicionado ao final da lista...')
    else:
        for c, j in enumerate(lista):
            if c == 0 and pb == False:
                if n < j:
                    lista.insert(0, n)
                    print('Adicionado no inicio da lista...')
                    pb = True
            if c == len(lista)-1 and pb == False:
                if n > j:
                    lista.append(n)
                    print('Adcionado no final da lista...')
                    pb = True
                else:
                    if n < j and pb == False:
                        lista.insert(c, n)
                        print(f'Adicionado na pisção {c} da lista...')
                        pb = True
print(lista)'''