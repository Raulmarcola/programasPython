# Exercício 12: Definir uma função para cada operação básica; solicitar números e operação ao usuário e exibir resultado. obs: Tratar divisão por zero
# Desafio-extra: Transformar a exibição numa função também

def soma(a, b):
    soma = a + b
    return soma

def sub(a, b):
    subtracao = a - b
    return subtracao

def mult(a, b):
    multiplicacao = a * b
    return multiplicacao

def div(a, b):
    if b == 0:
        resultado = ('Impossível dividir por zero.')
    else:
        resultado = a / b

    return resultado

def exibir(operacao, sinal, num1, num2, funcao):
    if funcao == 'Impossível dividir por zero.':
        print(f'\n{funcao}')
    else:
        print(f'\n{operacao} -> {num1} {sinal} {num2} = {funcao}')

num1 = float(input('\nInforme o primeiro número: '))
num2 = float(input('\nInforme o segundo número: '))
while True:
    operacao = int(input('\nMenu de operações - \n1 - Soma \n2 - Subtração \n3 - Multiplicação \n4 - Divisão \n\nInforme a operação a executar, conforme código numérico: '))
    if operacao < 1 or operacao > 4: #Poderia tornar operacao uma variável float e depois verificar através de => operacao % 1 != 0
        print('\n*Código Numérico Inválido*')
    else:
        break

if operacao == 1:
    operacao = 'Soma'
    sinal = '+'
    funcao = soma
if operacao == 2:
    operacao = 'Subtração'
    sinal = '-'
    funcao = sub
if operacao == 3:
    operacao = 'Multiplicação'
    sinal = 'x'
    funcao = mult
if operacao == 4:
    operacao = 'Divisão'
    sinal = ':'
    funcao = div

exibir(operacao, sinal, num1, num2, funcao(num1, num2))
# Posso colocar a função exibir de forma personalizada em cada if,
# OU personalizar os parâmetros e utilizar a função exibir de forma genérica

#A Função também poderia ser:

# def calculo(operacao, num1, num2):
