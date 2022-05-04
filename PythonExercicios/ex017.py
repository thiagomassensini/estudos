from math import sqrt
cato = float(input('Digite o comprimento do cateto oposto: '))
cata = float(input('Digite o comprimento do cateto adjacente: '))
hipo = sqrt(cato ** 2 + cata ** 2)
print('O comprimento da hipotenusa é: {}'.format(hipo))

# hipo ** 0.5 = (cato ** 0.5) + (cata ** 0.5)
#