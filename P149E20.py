opcao = 0
print('Menu de opções:')
print('1. Média Aritmética')
print('2. Média Ponderada')
print('3. Sair')
print('')
while opcao != 3:
    opcao = int (input('Digite a opção desejada.'))
    print('')
    if opcao == 1:
        print('Informe as notas - ')
        n1 = float (input('1° Nota: '))
        n2 = float (input('2° Nota: '))
        med = (n1 + n2) / 2
        print('')
        print(f'MÉDIA ARITMÉTICA:{med:.2f}')

    elif opcao == 2:
        print('Informe as notas e seus respectivos pesos - ')
        n1 = float(input('1° Nota: '))
        p1 = float(input('peso: '))
        n2 = float(input('2° Nota: '))
        p2 = float(input('peso: '))
        n3 = float(input('3° Nota: '))
        p3 = float(input('peso: '))
        med = ( (n1 * p1) + (n2 * p2) + (n3 * p3) ) / (p1 + p2 + p3)
        print('')
        print(f'MÉDIA PONDERADA:{med:.2f}')
    
    elif opcao == 3:    
        print('FIM DA APLICAÇÃO')
    
    else:
        print('OPÇÃO INVÁLIDA')
