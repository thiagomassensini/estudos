num = int(input("Digite um numero inteiro: "))
cont = 0
atual = 1
ante = 1
prox = 0
while cont <= num:
    ante = atual
    atual = prox
    print('{} '.format(atual), end='')
    prox = atual + ante
    cont += 1
