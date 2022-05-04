#Mostrar todos os numeros pares entre 1 e 50
metodo = int(input("Metodo 1 ou 2: "))
if metodo == 1:
    for c in range(2, 51, 2):
        print(c, end=' ')
elif metodo == 2:
    for c in range(1, 51):
        if c % 2 == 0:
            print(c, end=' ')
else:
    print('Meetodo inválido!')
print('Acabou')
