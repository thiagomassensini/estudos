'''import random
num = random.random()
num1 = random.randint(1, 10)
print(num)
print(num1)
import random
a1 = input("Primeiro Aluno: ")
a2 = input('Segundo Aluno: ')
a3 = input('Terceiro Aluno: ')
a4 = input('Quarto Aluno: ')
num = random.randint(1, 4)
if num == 1:
    print(a1)
if num == 2:
    print(a2)
if num == 3:
    print(a3)
if num == 4:
    print(a4)'''
#import random
from random import choice
n1 = str(input('Primeiro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Quarto aluno: '))
lista = [n1, n2, n3, n4]
escolhido = choice(lista)
print('O aluno escolhido foi {}'.format(escolhido))
