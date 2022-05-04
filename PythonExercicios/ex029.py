velocidade = int(input('Digite a velocidade do carro: '))
if velocidade > 80:
    multa = float(7 * (velocidade - 80))
    print('Você foi multado pot psddst a {}km/h ultrapassando o limite da via.'.format(velocidade))
    print('O valor da multa a ser é pago é de R${:.2f}'.format(multa))
else:
    print('Você passou dentro do limite permitido da via!')

