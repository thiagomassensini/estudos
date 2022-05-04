sexo = str(input('Digite o sexo da pessoa (M|F): ')).upper().strip()
while sexo not in 'MF':
    print('Entrada Inválida')
    sexo = str(input('Digite novamente  (M|F): ')).upper().strip()
if sexo == 'M':
    print('Sexo Masculino')
else:
    print('Sexo Feminino')
print('Fim')
