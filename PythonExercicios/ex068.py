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

from random import randint
jogador = ''
#numJogador = 0
computador = 'PAR', 'IMPAR'
#numComputador = 0
result = ''
cont = 0
print(f'{azulclaro}Bem vindo ao GAME de Par ou Ímpar{cor}')
while True:
    jogador = str(input('Digite PAR ou IMPAR: ')).strip().upper()
    while 'PAR' != jogador != 'IMPAR':
        print(f'{vermelho}Entreda Inválida.{cor} Tente novamente!')
        jogador = str(input('Digite PAR ou IMPAR: ')).strip().upper()
    #numJogador = int(input('Digite seu numero: '))
    rand = randint(0, 1)
    if jogador == computador[rand]:
        result = 'PAR'
    else:
        result = 'IMPAR'
    if result == jogador:
        print(f'{verde}Você venceu essa rodada!{cor}')
        cont += 1
    else:
        print(f'{roxo}Você perdeu essa rodada a maquuina escolheu {vermelho}{computador[rand]}{cor}')
        break
if cont > 1:
    print(f'{amarelo}Paranéns, você conseguiu {verde}{cont}{amarelo} vitórias!{cor}')
elif cont == 1:
    print(f'{amarelo}Paranéns, você conseguiu {verde}{cont}{amarelo} vitória!{cor}')
else:
    print(f'{vermelho}Você foi derrotado e conseguiu a incrível marca de {sublinhado}{cont}{cor}{vermelho}{negrito} VITORIAS!!!!{cor}')
