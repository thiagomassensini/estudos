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

baratoNome = nome = sn = ''
baratoPreço = total = maisMil = aux = preço = 0
while True:
    aux += 1
    nome = str(input(f'Digite o nome  do {aux} produto: '))
    preço = float(input(f'Digite o preço do {aux} produto: '))
    sn = str(input('Deseja continuar S/N: ')).strip().upper()
    while 'S' != sn != 'N':
        print(f'{vermelho}Entrada Inválida!{cor}')
        sn = str(input(f'Tente novamente {negrito}S/N{cor}: ')).strip().upper()
    total += preço
    if preço > 1000:
        maisMil += 1
    if baratoPreço == 0 or baratoPreço > preço:
        baratoNome = nome
        baratoPreço = preço
    if sn == 'N':
        print('=' *5, 'Fim', '=' *20)
        break
print(f'O total gasto na compra foi {total:.2f}')
print(f'O total de produtos que custam mais de mil é {maisMil}')
print(f'O produto mais barato é {baratoNome} que custa R${baratoPreço}')

