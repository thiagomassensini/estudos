matrix = [0, 1, 2], [0, 1, 2], [0, 1, 2]
somaPar = somaTer = maiorSeg = 0
for x in range(0, 3):
    for y in range(0, 3):
        matrix[x][y] = int(input(f'Digite o valor para [{x}, {y}]: '))
print('-=' *30)
for i in range(0, 3):
    for j in range(0, 3):
        print(f'[ {matrix[i][j]} ]', end='')
        if matrix[i][j] % 2 == 0:
            somaPar += matrix[i][j]
        if j == 2:
            somaTer += matrix[i][j]
        if i == 1 and j == 0:
            maiorSeg = matrix[i][j]
        elif i == 1 and maiorSeg < matrix[i][j]:
            maiorSeg = matrix[i][j]
    print('')
print('-=' *30)
print(f'A soma dos valores pares é {somaPar}')
print(f'A soma dos valores da terceira coluna é {somaTer}')
print(f'O maior valor da segunda linha é {maiorSeg}')
