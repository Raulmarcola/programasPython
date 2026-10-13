# Exercício 4: Receber um número, calcular e imprimir sua paridade.
print('')
print('Par ou Ímpar')
print('')

num = int(input('Digite um Número: '))
print('')

if num % 2 == 0: # % calcula o resto da divisão pelo número que você colocar
    # % 2 ser = 0 indica que a divisão por 2 é exata; se é divisível por 2, é par.
    print(f'Número {num} é PAR.')
else:
    print(f'Número {num} é ÍMPAR')