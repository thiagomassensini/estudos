salario = float(input('Digite o salário do funcionário: R$'))
if salario > 1250:
    print('Seu novo salário é de {}R${:.2f}{}!'.format('\033[0;30;42m', salario * 1.1, '\033[m'))
else:
    print('Seu novo salário é de {}R${:.2f}{}!'.format('\033[1;36m', salario * 1.15, '\033[m'))
