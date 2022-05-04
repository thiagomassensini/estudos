nome = str(input('Digite o nome de uma cidade: '))
dividido = nome.lower().split()
print('A cidade {} começa com o nome santo: {}'.format(nome, 'santo' in dividido[0]))
