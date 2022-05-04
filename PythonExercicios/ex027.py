nome = str(input('Digite o nome de uma pessoa: ')).strip() #Strip serve para remover os espaços vazios no começo e final
print('Ex: {}'.format(nome))
splitado = nome.split()
print('primeiro= {}'.format(splitado[0]))
#print('último= {}'.format())
print('último= {}'.format(splitado[len(splitado)-1]))
