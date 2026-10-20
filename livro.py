# Exercício 10: Declarar um livro com dicionário e exibí-lo. Solicitar ao usuário uma atualização em algum campo do dicionário livro. Exibir o livro atualizado

livro = {
    'nome': 'Atos dos Apóstolos',
    'autor': 'Lucas',
    'anoPublicacao': 70,
    'genero': 'Aventura',
    'paginas': 38
}

print('\nLivro -')
for i, j in livro.items():
    print(f'{i}: {j}')

campo = input('\nInforme o campo para atualização: ')

if campo == 'anoPublicacao' or campo == 'paginas':
    livro[campo] = int(input(f'Informe o novo valor de {campo}:'))

else:
    livro[campo] = input(f'Informe o novo valor de {campo}: ')

print('\nLivro Atualizado -')
for i, j in livro.items():
    print(f'{i}: {j}')