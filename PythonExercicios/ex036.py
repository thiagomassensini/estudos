print('Bem vindo ao simulador de emprestimos OpenSource.')
print('*' * 50)
casa = flaot(input('Digite o valor da casa: '))
salario = float(input("Digite o salário do fiador: "))
anos = int(input('Digite em quantos anos vai pagar:'))
parcelas = anos * 12
prestacao = casa / parcelas
if prestacao <= (salario * 0.30):
    print('O valor da prestação da casa será de R${:.2f}'.format(prestacao))
else:
    print('Você não pode realizar o emprestimo! ')