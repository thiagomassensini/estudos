menor = 0
maior = 0
for c in range(1, 6):
    peso = float(input("Diigite o peso da {} pessoa: ".format(c)))
    if menor > peso or menor == 0:
        menor = peso
    if maior < peso:
        maior = peso
print('O maior peso digitador foi {}'.format(maior))
print('O menor peso digitado foi {}'.format(menor))
