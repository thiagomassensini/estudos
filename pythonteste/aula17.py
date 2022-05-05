'''#Tuplas ()
#listas []


#metodos para adicionar na lista
listas.append('variavel')#adiciona no final da lista
listas.insert('variavel')#adiciona no inicio da lista

#metodos para remover da lista
del lista[3]#indica que quer remover o o item na posição 3 da lista
lista.pop(3)#faz a mesma coisa que o "del" da linha de cima
lista.pop()#nessa caso, quando não informa a posição da lista ele esclui o ultimo da lista
lista.remove('conteudo da varialvel')#esse ao invés de remover pela posição, remove pelo conteudo da variavel, se não encontrar ele gera um erro

#metodo para ordernar em ordem alfabetica ou numerica
lista.sort()
lista.sort(reverse=True)#colocar em ordem reversa

#saver o tamanho da lista
len(lista)'''
num = [2, 5, 9, 1]
num[2] = 3# subistituindo o numero 9 pelo 3
num.append(7)# adcionando o numero 7 no final da lista
num.sort(reverse=True)# colocando os numeros em ordem reversa
num.insert(3, 0)# adicionar o 0 na posição 2 da lista
num.pop()# apagar o ultimo da lista
if 4 in num:
    num.remove(4)
else:
    print('Não achei o número 4')
print(num)
print(f'Essa lista tem {len(num)} elementos.')