n = s = c = 0
while True:
    n = int(input('Digite um númoro ou 999 para sair: '))
    if n == 999:
        print('Fim!')
        break
    s += n
    c += 1
print(f'Foram digitados {c} números e a soma entre eles é {s}')
