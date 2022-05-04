import math , random
r1 = float(input('Digite a reta 1: '))
r2 = float(input('Digite a reta 2: '))
r3 = float(input('Digite a reta 3: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    if r1 == r2 == r3:
        print('Os segmentos acima PODEM FORMAR um traângulo Equilátero!')
    elif r1 == r2 or r2 == r3 or r3 == r1:
        print('Os segmentos acima PODEM FORMAR um triângulo Isósceles!')
    else:
        print('Os segmentos acima PODEM FORMAR um triângulo Escaleno!')
else:
    print('Os segmentos acima NÂO PODEM FORMAR um triângulo!')