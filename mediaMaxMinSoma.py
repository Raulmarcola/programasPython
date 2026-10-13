# Exercício 6: Receber vários números e devolver qual foi o máximo, o mínimo, a soma e a média. Parar quando o número recebido for negativo

cont = 0 #Contador para tirar a média
soma = 0
max = 0
mini = 0

while True:
    num = int(input(f'\nInforme números inteiros positivos e um número negativo para sair. \nDigite valor: \n'))
    if num < 0:
        break

    cont += 1
    soma += num

    if cont == 1: #Aproveitando o contador para definir o maior e o menor
        max = num
        mini = num
    #Na primeira inserção de dados tanto o menor quanto o maior devem ser o número que foi informado

    if num > max:
        max = num

    if num < mini:
        mini = num

if cont <= 0:
    print('Não foram digitados valores')
    #Daria erro no cálculo da média se a pessoa não informar números, pois seria uma divisão por zero
else:
    media = soma / cont

    print(f'Sobre os números informados -\n \nMAIOR: {max} \nMENOR: {mini} \nMÉDIA: {media} \nSOMA: {soma}')