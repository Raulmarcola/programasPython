print('**CONTADOR DE PARES**')
cont = 0
print('')
print('Digite dez números: ')
for x in range (1,11):
    print('')
    num = int (input(f'{x}°: '))

    par = num % 2

    if par == 0:
        cont += 1

print('')
print(f'TOTAL DE NÚMEROS PARES: {cont}')
