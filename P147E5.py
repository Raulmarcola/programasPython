print('TABUADA DOS NÚMEROS DE 1 A 10:')
for x  in range (1,11):
    print('')
    print(f'TABUADA DO {x} -')
    for y in range (11):
        result = x * y
        print(f'{x} X {y} = {result}')
print('')
print('FIM DA APLICAÇÃO!')
#Considerie tabuada sendo do 0 até o 10, mas daria para fazer a partir do 1, colocando ele no range.
