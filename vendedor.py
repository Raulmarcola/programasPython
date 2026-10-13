# Exercício 2: receber nome salário e vendas, calcular salário final a parti da comissão de 15% e imprimir
print('')
print('Calculadora de Salário e Comissão de Vendedor')
print('')
print('Informe sobre o vendedor - ')

nome = input('Nome: ')
salario = float(input('Salário Fixo: '))
vendas = float(input('Total de vendas (em R$): '))

salFin = salario + (vendas * 0.15) #vendas * 0.15 = comissão, pode ou não ser uma variável

print('')
print(f'HOLERITE DO(A) FUNCIONÁRIO(A) {nome} - ')
print(f'Salário Fixo: {salario}')
print(f'Salário Final: {salFin}')