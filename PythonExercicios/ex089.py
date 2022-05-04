notas = [[], [], []]
#aux = 0
while True:
    notas[0].append(str(input('Nome: ')))
    notas[1].append(float(input('Nota 1: ')))
    notas[2].append(float(input('Nota 2: ')))
    if str(input('Quer continuar? [S/N]')).strip() in "Nn":
        break
#    else:
#        aux += 1
print('-=' * 30)
print('No. NOME                MÉDIA')
print('-' * 30)
for c, i in enumerate(notas[0]):
    print(f'{c}  {notas[0][c]}', '.' * (20 - len(notas[0][c])), f'{(notas[1][c]+notas[2][c])/2:.2f}')
print('-' * 30)
while True:
    aluno = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if aluno == 999:
        break
    else:
        print(f'Notas de {notas[0][aluno]} são [{notas[1][aluno]}, {notas[2][aluno]}]')
        print('-=' * 30)


'''print(notas[0][0])
print(notas[1][0])
print(notas[2][0])'''