opc = True
num = 0
cont = 0
soma = 0
while opc == True:
    num = int(input('Digite um numero inteiro ou "999" para sair: '))
    if num != 999:
        soma += num
        cont += 1
    else:
        print('SAIR!')
        opc = False
print('Foram digitados {} numeros'.format(cont))
print('A soma entre os numeros é {}'. format(soma))