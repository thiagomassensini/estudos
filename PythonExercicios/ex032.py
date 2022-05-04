from datetime import date
ano = int(input('Digite o ano: '))
if ano == 0:
    ano = date.today().year
'''
if ano % 4 == 0:
    if ano % 100 == 0:
        if ano % 400 == 0:
            print('O ano {} é bissexto.'.format(ano))
        else: print('O ano {} é bissexto.'.format(ano))
    else: print('O ano {} é bissexto.'.format(ano))
else: print('O ano {} não é um ano bissexto.'.format(ano))
'''
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é BISSEXTO'.format(ano))
else:
    print('O ano {} não é BISSEXTO'.format(ano))

