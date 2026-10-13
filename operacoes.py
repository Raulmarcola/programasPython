# Exercício 1: Algoritmo que recebe dois números calcula e imprime os resultados das quatro operações matemáticas básicas.

print('')
print('Operações Matemáticas com 2 Números.')
print('')
num1 = float(input('Informe o primeiro número: '))
num2 = float(input('informe o segundo número: '))


soma = num1 + num2

sub = num1 - num2

mult = num1 * num2

print('')
print(f'SOMA: {soma:.2f}')
print('')
print(f'SUBTRAÇÃO: {sub:.2f}')
print('')
print(f'MULTIPLICAÇÃO: {mult:.2f}')

if num2 != 0:
    div = num1 / num2

    print('')
    print(f'DIVISÃO: {div:.2f}')

else:
    print('')
    print('IMPOSSÍVEL DIVIDIR POR ZERO.')