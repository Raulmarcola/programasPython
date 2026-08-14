#** Faça uma função que receba N e some todos os números de 1 a té N

#Código
#n = 3
#soma = 0
#
#for x in range(1, n+1):
#    print(f'{soma} + {x} = {soma + x}')
#    soma += x

#Função
def soma(n):
    soma = 0
    if n < 0:
        print('Número inválido')
        return soma

    for x in range(1, n+1):
        print(f'{soma} + {x} = {soma + x}')
        soma += x
    return soma

print(soma(3))
print(soma(-3))
