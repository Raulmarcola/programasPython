# Exercício 3: Receber dois números e imprimir qual é o maior
print('')
print('Comparador de Números')
print('')
print('Informe os números para fazer a comparação - ')

print('')
num1 = int(input('Primeiro valor: '))
num2 = int(input('Segundo valor: '))
print('')

if num1 > num2:
    print(f'Primeiro valor, {num1}, é o maior.')
elif num2 > num1:
    print(f'Segundo valor, {num2}, é o maior.')
else:
    # se nenhum dos casos for verdadeiro, nem maior nem menor, significa que é o mesmo número
    print('Os valores são iguais.')