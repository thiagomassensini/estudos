# Digitar uma frase, rmeoevr os espaçsos e verificar se é polidrama(Ex: Apos a sopa invertido e sem espaço fica
# aposasopa)
frase = str(input('Digite uma frase: ')).strip().replace(' ', '').upper()
print('O inverso de {} é {}'.format(frase, frase[::-1]))
if frase == frase[::-1]:
    print('É um polindrama!')
else:
    print('Não é um polidrama!')

