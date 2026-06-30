#Seria mais fácil fazer com for, mas vamos praticar o while!
cont = 1
soma= 0    
qtdPeso = 0
qtdAltura = 0
qtdIdade = 0
print('**ESTATÍSTICAS IDADE-ALTURA-PESO**')
print('')
print('Informe Idade, altura e peso de 10 indivíduos: ')
t = 4
while cont < (t+1):
    print('')
    print(f'*{cont}° Indivíduo*')
    print('')
    idade = int (input('Idade, em anos: '))
    altura = float (input('Altura, em metros: '))
    peso = float (input('Peso, em quilogramas: '))

    soma += idade

    if peso > 90 and altura < 1.5:
        qtdPeso += 1

    if  altura > 1.9:
        qtdAltura += 1 

        if idade > 10 and idade < 30:
            qtdIdade += 1
    
    cont += 1

med = soma / t

porc = (qtdIdade * 100) / qtdAltura

print('')
print('*ESTATÍSTICAS*')
print('')
print(f'MÉDIA DE TODAS AS IDADES: {med}')
print(f'QUANTIDADE COM PESO ACIMA DE 90 KG E ALTURA INFERIOR A 1,50 M: {qtdPeso}')
print(f'PORCENTAGEM DE PESSOAS COM IDADE ENTRE 10 E 30 ANOS ENTRE OS QUE MEDEM MAIS DE 1,90 M: {porc}%')
