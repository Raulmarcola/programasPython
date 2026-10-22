#Júnior e Raul
# Exercício 11: Permitir que o usuário crie, atualize e consulte produtos em uma lista.

estoque = []

op = 0

while True:
    op = int(input('\nMENU\n \n1 - Adicionar novo produto \n2 - Registrar Venda \n3 - Valor total \n4 - Relatório do Estoque \n5 - Sair\n \nOpção: '))

    if op == 1:
        print('\nAdicionar Produto - ')
        encontrado = False
        nome = input('\nInforme o nome do produto: ')
        for i in range(len(estoque)):
            if nome == estoque[i]['nome']:
                encontrado = True
                quantidade = int(input('Informe a quantidade: '))
                estoque[i]['quantidade'] += quantidade
                (f'Quantidade de produto {nome} atualizada.')

        if not encontrado:
            produto = {
                'nome': nome,
                'preco': float(input('Informe seu preço unitário: ')),
                'quantidade': int(input('Informe a quantidade: '))
            }

            estoque.append(produto)
            print(f'Produto {nome} adicionado!')

    elif op == 2:
        if len(estoque) > 0:
            encontrado = False
            print('\nRegistrar Venda - ')
            nome = input('\nInforme o nome do produto a vender: ')
            for i in range(len(estoque)):
                if nome == estoque[i]['nome']:
                    encontrado = True
                    quantidadeVenda = int(input('Informe a quantidade para venda: '))
                    if quantidadeVenda <= estoque[i]['quantidade']:
                        estoque[i]['quantidade'] -= quantidadeVenda
                        print('Venda registrada com sucesso.')
                    else:
                         print('Quantidade indisponível.')
        if not encontrado:
            print('Produto indisponível/não encontrado.')
        else:
            print('\nEstoque vazio.')

    elif op == 3:
        if len(estoque) > 0:
            valorTotal = 0
        
            for i in estoque:
                valorTotal += i['preco'] * i['quantidade']

            print(f'Valor Total em Estoque: {valorTotal}')
        else:
            print('\nEstoque vazio.')

    elif op == 4:
        if len(estoque) > 0:
            print('\nRelatório do Estoque - ')
            for produto in estoque:
                print('')
                for x, y in produto.items():
                    print(f'{x}: {y}')
        else:
            print('\nEstoque Vazio.')

    elif op == 5:
        break

    else:
        print('Opção Inválida.')

print('Glória toda a Deus!')