from random import randint
from time import sleep
print('\033[7;30m_*_\033[m' * 13)
print(' ' * 5, '\033[1;31mBem vindo ao nosso Jokenpô\033[m')
print('\033[7;30m_*_\033[m' * 13)
play = True
game = ['Pedra', 'Papel', 'Tesoura']
while play == True:
    ia = randint(1, 3)
    opc = int(input('\nDigite 1 para Pedra,\n'
                    'Digite 2 para Papel,\n'
                    'Digite 3 para Tesoura,\n'
                    'Ou 0 para sair do jogo.\n'
                    '=> '))
    if opc == 0:
        play = False
        print('\nJogo Encerrado')
    elif opc == 1 or opc == 2 or opc == 3:
        print('JO')
        sleep(1)
        print('KEN')
        sleep(1)
        print('PO!!!')
        #print('\n''\033[7;30m_*_\033[m' * 13)
        if opc == ia:
            print('\033[7;30m_*_\033[m' * 20)
            print("\033[4;33mVocê escolheu {} e a IA escolheu {}, empate\033[m".format(game[opc - 1], game[ia - 1]))
            print('\033[7;30m_*_\033[m' * 20)
        elif (opc == 1 and ia == 3) or (opc == 2 and ia == 1) or (opc == 3 and ia == 2):
            print('\033[7;30m_*_\033[m' * 20)
            print('\033[4;32mVocê escolheu {} e a IA escolheu {}, você ganhou\033[m'.format(game[opc - 1], game[ia - 1]))
            print('\033[7;30m_*_\033[m' * 20)
        elif (opc == 1 and ia == 2) or (opc == 2 and ia == 3) or (opc == 3 and ia == 1):
            print('\033[7;30m_*_\033[m' * 20)
            print("\033[4;35mVocê escolheu {} e a IA escolheu {}, IA aganhou\033[m".format(game[opc - 1], game[ia - 1]))
            print('\033[7;30m_*_\033[m' * 20)
    else:
        print('\n\033[1;31mOpção inválida\033[m')
