# Exercicio 5: Programa que recebe uma combinação de lanche e bebida e mostra se o pedido pode ser atendido ou não, pois algumas combinações devem ser rejeitadas
print('*LANCHONETE*')
#\n pula linha em uma string formatada

#Fazendo uma validação para o pedido do cliente se ele digitar códigos inválidos
valid = True

while(valid):
    lanche = int( input(f'\n1 - Bauru\n2 - X Galinha\n3 - Pizza\nInforme seu lanche pelo código numérico: '))
    bebida = int( input(f'\n1 - Água\n2 - Guaraná\n3 - Vinho\nInforme seu lanche pelo código numérico: '))

    if (lanche > 3 or lanche <= 0) or (bebida > 3 or bebida <= 0):
        print(f'\nCÓDIGOS NUMÉRICOS INVÁLIDOS!')
        #Assim valid vai continuar sendo True e o while vai se repetir 
    else:
        #Se a condicional de cima for False quer dizer que o usuário digitou um número válido, ou seja, podemos tornar valid False e o laço não vai se repetir
        valid = False

if (lanche == 1 and bebida == 2) or (lanche == 2 and bebida == 1) or (lanche == 3 and bebida == 2):
    print(f'\nPedido Rejeitado!')
else:
    print(f'\nPedido Aceito!')