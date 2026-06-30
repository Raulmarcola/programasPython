print('**ESTATÍSTICAS DE FAIXA ETÁRIA**')
print('')
print('Informe a idade, em anos, de 8 Indivíduos.')
qtdF1 = 0
qtdF2 = 0
qtdF3 = 0
qtdF4 = 0
qtdF5 = 0
percF1 = 0
percF5 = 0
for x in range(1,9):
    print('')
    idade = int (input(f'{x}° indivíduo: '))

    if idade <= 15:
        qtdF1 += 1

    elif idade <= 30:
        qtdF2 += 1

    elif idade <= 45:
        qtdF3 += 1

    elif idade <= 60:
        qtdF4 += 1

    else:
        qtdF5 += 1

percF1 = (qtdF1 * 100) / 8
percF5 = (qtdF5 * 100) / 8

print('QUANTIDADE DE INDIVÍDUOS POR FAIXA ETÁRIA: ')
print('')
print(f'1°(Até 15 anos): {qtdF1}')
print('')
print(f'2°(De 16 a 30 anos): {qtdF2}')
print('')
print(f'3°(de 31 a 45 anos): {qtdF3}')
print('')
print(f'4°(46 a 60 anos): {qtdF4}')
print('')
print(f'5°(Acima de 60 anos): {qtdF5}')
print('')
print('PORCENTAGENS - ')
print(f'Porecentagem de indivíduos na 1° Faixa Etária: {percF1}%')
print('')
print(f'Porecentagem de indivíduos na 5° Faixa Etária: {percF5}%')
