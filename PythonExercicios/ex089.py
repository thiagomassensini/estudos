notas = list()
#aux = 0
while True:
    nome = (str(input('Nome: ')))
    nota1 = (float(input('Nota 1: ')))
    nota2 = (float(input('Nota 2: ')))
    media = (nota1 + nota2) / 2
    notas.append([nome, [nota1, nota2], media])
    if str(input('Quer continuar? [S/N]')).strip() in "Nn":
        break
#    else:
#        aux += 1
print('-=' * 30)
print('No. NOME                MÉDIA')
print('-' * 30)
for c, i in enumerate(notas):
    print(f'{c}  {notas[c][0]}', '.' * (20 - len(notas[c][0])), f'{(notas[c][2]):.2f}')
print('-' * 30)
while True:
    aluno = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if aluno == 999:
        break
    else:
        print(f'Notas de {notas[aluno][0]} são [{notas[aluno][1][0]}, {notas[aluno][1][1]}]')
        print('-=' * 30)


'''print(notas[0][0])
print(notas[1][0])
print(notas[2][0])'''