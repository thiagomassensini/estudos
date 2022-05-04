tabela = ('Bahia', 'Operário-PR', 'Chapecoense', 'Sport',
          'Londrina', 'Criciúma', 'Brusque', 'Cruzeiro',
          'Vasco', 'Tombense', 'Vila Nova', 'Ituano',
          'CRB', 'Novorizonte', 'CSA', 'Sampaio Corrêa',
          'Grêmio', 'Guarani', 'Ponte Preta', 'Náutico')
print(f'Os cinco primeiro colocados são {tabela[:5]}')
print(f'Os quatro últimos colocados da tabela são {tabela[-4:]}')
print(f'Times em ordem alfabetica {sorted(tabela)}')
print('A Chape está na {}ª posição'.format(tabela.index('Chapecoense') + 1)) # ou o de baixo vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
print(f'A Chapecoense está na {tabela.index("Chapecoense")+1}')
