from random import randint
from time import sleep

sena = []
print('-' * 20)
print(f'JOGO NA MEGA SENA')
print('-' * 20)
sleep(1)
jogo = int(input('Quantos jogos você quer q eu sorteie? '))
print(f'-=' * 3, f' SORTEANDO {jogo} JOGOS ', '-=' * 3)
for i in range(0, jogo):
    aux = 0
    sleep(1)
    while aux < 6:
        num = randint(1, 60)
        if num not in sena:
            sena.append(num)
            aux += 1
    sena.sort()
    print(f'Jogo {i+1}: {sena}')
    sena.clear()
print(f'-=' * 5, f' BOA SORTE! ', '-=' * 5)