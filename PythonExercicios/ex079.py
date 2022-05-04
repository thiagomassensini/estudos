var = []
while True:
   tmp = int(input('Digite um valor: '))
   if tmp not in var:
      var.append(tmp)
      print('Valor adicionado com sucesso.. ')
   else:
      print('Valor duplicado! Não vou adicionar...')
   opc = str(input('Quer continuar? [S/N] ')).strip().upper()
   if opc == 'N':
      break
var.sort()
print('-=' *20)
print(f'Você digitou os valores {var}')