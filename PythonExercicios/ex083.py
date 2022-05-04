expressao = str(input('Digite a extressão: ')).strip()
a = b = 0
for i in expressao:
    if i == '(':
        a += 1
    if i == ')':
        b += 1
if a == b:
    print('Sua espressão está válida!')
else:
    print('Sua expressão está errada!')
