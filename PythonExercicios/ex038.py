print('\033[1;32mVocê vai precisar digitar dois numeros!\033[m')
num1 = int(input('Digite o primeiro numero: '))
num2 = int(input('Digite o segundo numero: '))
print('\033[7;30m_*_\033[m' * 13)
print('Primeiro valor: {}{}{}\nSegundo valor: {}{}{}'.format('\033[1;32m', num1, '\033[m', '\033[1;31m', num2, '\033[m'))
print('\033[7;30m_*_\033[m' * 13)
if num1 > num2:
    print('O primeiro valor é maior')
elif num1 < num2:
    print('O segundo valor é maior')
else:
    print('Não exisite valor maior, os dois são iguais')