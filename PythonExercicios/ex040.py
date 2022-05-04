print('\033[7;30m_*_\033[m' * 13)
print('Calculo de média das notas Alunasticas!!!!!!!!!!')
print('\033[7;30m_*_\033[m' * 13)
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2) / 2
if media < 5:
    print("REPROVADO")
elif 5 <= media <= 6.9:
    print('RECUPERAÇÂO')
else:
    print('APROVADO')
