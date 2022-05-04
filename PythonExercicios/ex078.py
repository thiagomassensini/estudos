valores = []
maior = menor = 0
for i in range(0, 5):
    valores.append(int(input(f'Digite o valor da posição {i}: ')))
    if i == 0:
        maior = menor = valores[i]
    else:
        if valores[i] > maior:
            maior = valores[i]
        if valores[i] < menor:
            menor = valores[i]
print(f'Você digitou os valores {valores}')
print(f'O maiorr valor digitado foi {maior} nas posições ', end='')
for c, v in enumerate(valores):
    if v == maior:
        print(f'{c}.. ', end='')
print(f'\nO menor valor digitado foi {menor} nas posições ', end='')
for c, v in enumerate(valores):
    if v == menor:
        print(f'{c}.. ', end='')