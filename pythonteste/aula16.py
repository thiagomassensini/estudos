#TUPLAS com Strings
lanche = ('hamburguer', 'Suco', 'Pizza', 'Pudim')
print(lanche.index('Suco'))
print(lanche[1])
print(lanche[-2])
print(lanche[1:3])
print(lanche[2:])
print((lanche[:2]))
print(lanche[-3:])
for comida in lanche: #NÃO TEM COMO SABER A POSÇÃO USANDO DESSA MANEIRA
    print(f'Eu vou comer {comida}')
for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')
for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')
print(sorted(lanche))

#TUPLAS com Números
a = (2, 5 ,4)
b = (8, 5, 1, 2)
c = a + b
d = b + a
print(c)
print(d)
print(c.count(5))# .count é pra saber a qyabntidade de numeros 5 que tem na tulipa
print(b)
print(b.index(1))# .index é pra saber a posição do numero 1 da tulipa