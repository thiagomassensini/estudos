from random import randint
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
num1 = randint(0, 10)
num2 = 99
cont = 0
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 10. Tente adivinhar...')
print('-=-' * 20)
while num1 != num2:
    cont += 1
    num2 = int(input('Em que número pensei? '))
    print('-=-' * 20)
    print('{}{}Acertou{}'.format(verde, sublinhado, cor) if num1 == num2 else '{}{}Errou{}'.format(vermelho, sublinhado, cor))
    if num2 < num1:
        print('{}Mais... Tente mais uma vez.{}'.format(roxo, cor))
    elif num2 > num1:
        print('{}Menos... tente mais uma vez.{}'.format(azulclaro, cor))
print('{}-=-{}'.format(amarelo, cor) * 20)
print('Eu escolhi o numero {}{}{}{}'.format(azulclaro, negrito, num1, cor))
print('{}{}-=-{}'.format(amarelo, sublinhado, cor) * 20)
print('Foram necessários {}{}{}{} palpites para poder vencer!'.format(roxo, negrito, cont, cor))
