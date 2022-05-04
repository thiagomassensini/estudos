##################CORES#################
branco = '\033[0;30m'
vermelho = '\033[0;31m'
verde = '\033[0;32m'
amarelo = '\033[0;33m'
azul = '\033[0;34m'
roxo = '\033[0;35m'
azulclaro = '\033[0;36m'
cinza = '\033[0;37m'
negrito = '\033[1m'
sublinhado = '\033[4m'
cor = '\033[m'
########################################
for c in range(0 , 20):
    print(f'{verde}={cor}', end='')
    print(f'{amarelo}{negrito}={cor}', end='')
print(f'\n{negrito}{verde}      BANCO BITCOIN de ESQUERDA{cor}')
for c in range(0 , 20):
    print(f'{verde}={cor}', end='')
    print(f'{amarelo}{negrito}={cor}', end='')
print('')

contC = contV = contD = contU = 0
valor = int(input('Quantos reais você quer sacar? R$'))
while valor >= 50:
    valor -= 50
    contC += 1
while valor >= 20:
    valor -= 20
    contV += 1
while valor >= 10:
    valor -= 10
    contD += 1
while valor >= 1:
    valor -= 1
    contU += 1
print(f'Total de {contC} cédulas de R$50')
print(f'Total de {contV} cédulas de R$20')
print(f'Total de {contD} cédulas de R$10')
print(f'Total de {contU} cédulas de R$1')
for c in range(0 , 20):
    print(f'{verde}={cor}', end='')
    print(f'{amarelo}{negrito}={cor}', end='')