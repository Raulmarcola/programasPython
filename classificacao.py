# Exercício 9: Receber 5 times e suas respectivas pontuações (um vetor para cada). Mostrar quem foi o campeão e o último colocado.
#Desafios: fazer validação da pontuação informada e, no caso de empate (dois campeões e/ou dois últimos), mostrar ambos 

print('\nCampeonato Brasileiro - ')

times = []
pontuacoes = []
campeao = [] #Transformei-os em vetor para fazer o segundo desafio
ultimo = []
max = 0
min = 0

for i in range(5):

    times.append(input(f'\nInforme o nome do {i+1}° time: '))
    #Validação da pontuação (deve ser positiva)
    while True: #ou valid == 1, por exemplo
        pontuacao = int(input(f'Informe a pontuação de {times[i]}: '))
        if pontuacao >= 0:
            break #valid = 1. Mas é mais simples com while e break
        print('Pontuação deve ser inteira e positiva.')
    
    pontuacoes.append(pontuacao)

    if i == 0:
        #Se for a primeira inserção de dados, a maior e a menor pontuação serão o que foi informado 
        max = pontuacoes[i]
        min = pontuacoes[i]
    
    if pontuacoes[i] >= max:
        max = pontuacoes[i]

    if pontuacoes[i] <= min:
        min = pontuacoes[i]

for i in range(len(pontuacoes)):
    if max == pontuacoes[i]:
        campeao.append(times[i])
    if min == pontuacoes[i]:
        ultimo.append(times[i])
    

print(f'\nCAMPEÕES: {campeao} com {max} pontos. \nÚLTIMOS: {ultimo} com {min} pontos.')