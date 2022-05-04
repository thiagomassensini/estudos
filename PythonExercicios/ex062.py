print('=' * 20)
print('10 TERMOS DE UMA PA')
print('=' * 20)
menu = True
while menu  == True:
    print('Digite 0 termos se quiser sair do programa')
    termo = int(input('Primeiro termo: : '))
    if termo == 0:
        menu = False
    else:
        razao = int(input('Razao: '))
        decimo = termo + (10 - 1) * razao
        #for c in range(termo, decimo, razao):
        print('=' * 60)
        while termo <= decimo:
            print('{} >'.format(termo), end=' ')
            termo += razao
        print('ACABOU')
        print('=' * 60)
print('Fim')
