km = float(input('Digite a quantidade de KM rodados: '))
dias = int(input('Digite a quantidade de dias de aluguel: '))
kmrodado = km * 0.15
diaria = dias * 60
soma = kmrodado + diaria
print('O valor total do aluguel é de: R${:.2f}, sendo R${:.2f} em KM rodado e R${:.2f} pelas diarias'.format(soma, kmrodado, diaria))

