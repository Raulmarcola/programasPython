# Exercício 7: Sortear um número e receber palpites do usuário, informando se o palpite é maior ou menor que o sorteio até que ele acerte. Mostrar quantas tentativas ele precisou

import random

while True: #while do jogo
    sorteio = random.randint(0,100) #sortear a cada partida 
    print(f'\nA máquina sorteou um inteiro entre 0 e 100. Dê palpites até acertar!')
    qtdTentativas = 0 #zerar as tentativas
    
    while True: #while da partida

        palpite = int(input(f'\nPalpite: '))

        qtdTentativas += 1

        if palpite < sorteio:
            print(f'O número sorteado é maior que seu palpite {palpite}.')

        elif palpite > sorteio:
            print(f'O número sorteado é menor que seu palpite {palpite}.')

        else:
            break

    print(f'Parabéns: Você acertou! \nNúmero sorteado: {sorteio} \nNúmero de Tentativas: {qtdTentativas}')

    resposta = input('Jogar novamente?').lower()

    if resposta == 'nao' or resposta == 'n' or resposta == 'não':
        break

print('Fim de Jogo')

#É criado um while para a partida que seria para cada estrutura de UM sorteio e N palpites e outro while para o jogo no geral com N reprocessamentos