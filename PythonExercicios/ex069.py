##################CORES#################
vermelho = '\033[0;31m'
cor = '\033[m'
negrito = '\033[1m'
########################################

idade = aux = maiores = mulheres = homens = 0
sexo = ''
opc = ''
while True:
    aux += 1
    idade = int(input(f'Digite a Idade da {aux} pessoa: '))
    sexo = str(input(f'Digite o sexo da {aux} pessoa: F ou M: ')).strip().upper()
    while 'F' != sexo != "M":
        print(f'{vermelho}Entrada Inválida!{cor}')
        sexo = str(input(f'Tente novamente {negrito}F|M{cor}: ')).strip().upper()
    if idade <= 18:
        maiores += 1
    if sexo == 'M':
        homens += 1
    elif idade < 20:
        mulheres += 1
    opc = str(input('Deseja continuar S/N? ')).strip().upper()
    while 'S' != opc != "N":
        print(f'{vermelho}Entrada Inválida!{cor}')
        opc = str(input(f'Tente novamente {negrito}S|N{cor}: ')).strip().upper()
    if opc == 'N':
        break
print(f'{maiores} tem mais de 18 anos')
print(f'{homens} homens foram cadastrados')
print(f'{mulheres} mulheres tem menos de 20 anos')
