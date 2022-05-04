print('''\033[1;36mOlá! As formas de pagamentos são:
Dinheiro/Pix: 10% desconto
Débito: 5% desconto
Em até 2x: Sem desconto
3x ou mais: 20% de juros\033[m''')
valor = float(input('Digite o valor do produto: '))
pgmt = int(input('Digite 1 para pagamento em Dinehiro\Pix,\n'
                 'Digite 2 para pagamento cartão de débito,\n'
                 'Digite 3 para pagamento até 2x,\n'
                 'Digite 4 para parcelas de 3x ou mais.\n'
                 '=>'))
if pgmt == 1:
    print('O valor á ser pago: R${:.2f}'.format(valor * 0.9))
elif pgmt == 2:
    print('O valor a ser pago: R${:.2f}'.format(valor * 0.95))
elif pgmt == 3:
    print('O valor a ser pago: R${:.2f}'.format(valor))
elif pgmt == 4:
    print('O valor a ser pago: R${:.2f}'.format(valor * 1.2))
else:
    print("Opção de pagamento inválida!")

