import math , random
r1 = float(input('Digite a reta 1: '))
r2 = float(input('Digite a reta 2: '))
r3 = float(input('Digite a reta 3: '))
if r1 + r2 > r3:
    if r1 + r3 > r2:
        if r2 + r3 > r1:
            print('{}Formam{} um triangulo'.format('\033[1;32m', '\033[m'))
        else:
            print('{}Não formam{} um triangulo'.format('\033[1;31m', '\033[m'))
    else:
        print('{}Não formam{} um triangulo'.format('\033[1;32m', '\033[m'))
else:
    print('{}Não formam{} um triangulo'.format('\033[1;31m', '\033[m'))


