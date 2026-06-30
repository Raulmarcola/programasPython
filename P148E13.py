t = 15
somaPeso1 = 0
contFaixa1 = 0
somaPeso2 = 0
contFaixa2 = 0
somaPeso3 = 0
contFaixa3 = 0
somaPeso4 = 0
contFaixa4 = 0
print('**MÉDIA DOS PESOS POR FAIXAS ETÁRIAS**')
for x in range (1, (t+1)):
    print('')
    print(f'Informe sobre o {x}° indivíduo - ')
    print('')
    idade = int (input('Idade, em anos: '))
    peso = float (input('Peso, em quilogramas: '))

    if idade <= 0:
        print('IDADE FORA DE FAIXA ETÁRIA')    

    elif idade >= 1 and idade <= 10:
        contFaixa1 += 1
        somaPeso1 += peso

    elif idade <= 20:
        contFaixa2 += 1
        somaPeso2 += peso

    elif idade <= 30:
        contFaixa3 += 1
        somaPeso3 += peso    

    else:
        contFaixa4 += 1
        somaPeso4 += peso
    
med1 = somaPeso1 / contFaixa1
med2 = somaPeso2 / contFaixa2
med3 = somaPeso3 / contFaixa3
med4 = somaPeso4 / contFaixa4
print('')
print('MÉDIA DE PESO')
print('')
print(f'1 a 10 anos: {med1:.2f}')
print(f'11 a 20 anos: {med2:.2f}')
print(f'21 a 30 anos: {med3:.2f}')
print(f'Acima de 30 anos: {med4:.2f}')
