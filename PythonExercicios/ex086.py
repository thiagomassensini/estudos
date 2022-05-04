matrix = [0, 1, 2], [0, 1, 2], [0, 1, 2]
for x in range(0, 3):
    for y in range(0, 3):
        matrix[x][y] = int(input(f'Digite o valor para [{x}, {y}]: '))
print('-=' *30)
for i in range(0, 3):
    for j in range(0, 3):
        print(f'[ {matrix[i][j]} ]', end='')
    print('')

