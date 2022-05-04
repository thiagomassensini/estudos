from math import radians, sin, cos, tan
angulo = float(input('Digite o ângulo que você deseja: '))
seno = sin(radians(angulo))
coss = cos(radians(angulo))
tan = tan(radians(angulo))
print('Angulo: {}º\nSeno: {:.2f}\nCosseno: {:.2f}\nTangente: {:.2f}'.format(angulo, seno, coss, tan))