frase = str(input('Digite uma frase: ')).strip()
print('A letra A aparece {} vezes'.format(frase.upper().count('A')))
print('A letra A aparece primeiro na posição {}'.format(frase.upper().find('A')+1))
#revertido = frase[::-1]
#print('A letra A aparece pela ultima vez na posção {}'.format(len(frase) - (revertido.upper().find('A'))))
print('A letra A aparece na posição {}'.format(frase.upper().rfind('A')+1))